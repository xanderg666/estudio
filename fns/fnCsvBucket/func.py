#
# oci-serviceconnector-streaming-json-to-parquet-python version 1.0.
#
# Copyright (c) 2021 Oracle, Inc.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import os
import oci
import json
import requests
import logging
import base64
import gzip
import time
import pandas as pd
from fdk import response


"""
This Function converts JSON to Parquet format and uploads the file to Object storage
"""
def handler(ctx, data: io.BytesIO=None):
    logger = logging.getLogger()

    namespace = os.environ['NAME_SPACE']
    bucket_name = os.environ['BUCKET_NAME']
    file_name = os.environ['FILE_NAME'] + time.strftime("%Y%m%d%H%M%S") + '.csv'

    try:
        logs = json.loads(data.getvalue())
        logger.info('Received {} entries.'.format(len(logs)))

        for item in logs:
            if 'value' in item:
                item['value'] = base64_decode(item['value'])

            if 'key' in item:
                item['key'] = base64_decode(item['key'])

        df = pd.json_normalize(logs)
        #se crea un df vacio para llenarlo con la informacion
        dfj = pd.DataFrame(columns=['GwId', 'RxId', 'RxAntId', 'RxFw', 'Mac', 'Serv', 'Rssi', 'Fw', 'Seq',
                                    'Date', 'State', 'Error', 'Batt', 'Temp', 'AX', 'AY', 'AZ', 'GX', 'GY',
                                    'GZ', 'Len'])
        #for para recorrer la cadena de caracteres al interior de los valores del sensor
        result = df["value"].to_json(orient="split")
        parsed = json.loads(result)
        for i in range(len(parsed['data'])):
            # print (i)
            c = parsed['data'][i]
            c = json.loads(c)
            # print(type(c))
            # print(c)
            dfj = dfj.append(c, ignore_index=True)
        csv_result = dfj.to_csv(index=False)
        upload_file(namespace, bucket_name, file_name, csv_result)
        #parquet_result = df.to_parquet(index=False)
        #file_compress = gzip.compress(parquet_result)
        #upload_file(namespace, bucket_name, file_name, file_compress)
 
        return

    except (Exception, ValueError) as e:
        logger.error(str(e))
        raise


def base64_decode(encoded):
    if encoded != '' and encoded is not None:
        base64_bytes = encoded.encode('utf-8')
        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes.decode('utf-8')


def upload_file(namespace, bucket_name, file_name, f):
    assert bucket_name and file_name
    signer = oci.auth.signers.get_resource_principals_signer()
    object_storage = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
    object_storage.put_object(namespace, bucket_name, file_name, f)
    return 
