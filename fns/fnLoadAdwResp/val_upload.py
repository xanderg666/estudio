import json
from datetime import date
import oci
import pandas as pd

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# https://docs.oracle.com/en-us/iaas/tools/python/2.53.1/api/object_storage/client/oci.object_storage.ObjectStorageClient.html#oci.object_storage.ObjectStorageClient.list_objects
# for more info
config = oci.config.from_file()

# Initialize service client with default config file
object_storage_client = oci.object_storage.ObjectStorageClient(config)

# Send the request to service, some parameters are not required, see API
# doc for more info
list_objects_response = object_storage_client.list_objects(
    namespace_name="idnygso6gagh",
    bucket_name="input-bucket",
    # prefix="EXAMPLE-prefix-Value",
    # start="EXAMPLE-start-Value",
    # end="EXAMPLE-end-Value",
    # limit=782,
    # delimiter="EXAMPLE-delimiter-Value",
    fields="timeCreated",
    # opc_client_request_id="ocid1.test.oc1..<unique_ID>EXAMPLE-opcClientRequestId-Value",
    # start_after="EXAMPLE-startAfter-Value"
    )
lis = str(list_objects_response.data)
# Convert the response to a json string
a = json.loads(str(list_objects_response.data))
# print("My json string response: ", json_response)

#crea la lista para extraer la info del JSON
def listado_files():
    l = []
    for obj in a['objects']:
    #     print (obj['name'],obj['time_created'])
        l.append([obj['name'],obj['time_created']])

    df = pd.DataFrame (l, columns = ['name','time'])
    # extraer la fecha de la cadena
    df['fecha1'] = df['time'].str.slice(0, 10)
    # convertir a fecha
    df['date'] = pd.to_datetime(df['fecha1'], format='%Y-%m-%d').dt.strftime('%Y%m%d')
    # el dia actual
    df['hoy'] = date.today().strftime("%Y%m%d")
    # convertir a fecha
    df[["date", "hoy"]] = df[["date", "hoy"]].apply(pd.to_datetime)
    # dias de diferencia a cargar
    df['flag'] = (df['hoy'] - df['date']).dt.days
    # flag true
    df.loc[df['flag'] > 0, 'flag'] = 'True'
    # filtrar
    df = df.loc[df['flag'] == 'True']
    # archivos a eliminar
    df = df['name']
    return df

#https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/object_storage/client/oci.object_storage.ObjectStorageClientCompositeOperations.html#oci.object_storage.ObjectStorageClientCompositeOperations.copy_object_and_wait_for_state
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

files = listado_files()
print(files)

#mover los objectos
namespace = "idnygso6gagh"
source_bucket ="input-bucket2"
processed_bucket = "processed-bucket2"
object_name = "data_20211230164057.csv"

#mover objectos
objstore = oci.object_storage.ObjectStorageClient(config)
objstore_composite_ops = oci.object_storage.ObjectStorageClientCompositeOperations(objstore)

#ejecutar la funcion
move_object( namespace, source_bucket, processed_bucket, object_name)