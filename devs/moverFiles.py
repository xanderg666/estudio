from __future__ import print_function
import os
import oci
from oci.object_storage import UploadManager
from oci.object_storage.models import CreateBucketDetails
from oci.object_storage.transfer.constants import MEBIBYTE
import oci
import json
import requests

# signer = oci.auth.signers.get_resource_principals_signer()
config = oci.config.from_file()
objstore = oci.object_storage.ObjectStorageClient(config)
objstore_composite_ops = oci.object_storage.ObjectStorageClientCompositeOperations(objstore)
object_storage_client = oci.object_storage.ObjectStorageClient(config)

namespace = "idnygso6gagh"
source_bucket ="input-bucket2"
processed_bucket = "processed-bucket2"
object_name = "data_20211230164057.csv"

def move_object( namespace, source_bucket, destination_bucket, object_name):
    objstore = oci.object_storage.ObjectStorageClient(config)
    objstore_composite_ops = oci.object_storage.ObjectStorageClientCompositeOperations(objstore)
    resp = objstore_composite_ops.copy_object_and_wait_for_state(
        namespace,
        source_bucket,
        oci.object_storage.models.CopyObjectDetails(
            destination_bucket=destination_bucket,
            destination_namespace=namespace,
            destination_object_name=object_name,
            destination_region='us-ashburn-1',
            source_object_name=object_name
            ),
        wait_for_states=[
            oci.object_storage.models.WorkRequest.STATUS_COMPLETED,
            oci.object_storage.models.WorkRequest.STATUS_FAILED])
    if resp.data.status != "COMPLETED":
        raise Exception("cannot copy object {0} to bucket {1}".format(object_name,destination_bucket))
    else:
        resp = objstore.delete_object(namespace, source_bucket, object_name)
        print("INFO - Object {0} moved to Bucket {1}".format(object_name,destination_bucket), flush=True)

move_object( namespace, source_bucket, processed_bucket, object_name)