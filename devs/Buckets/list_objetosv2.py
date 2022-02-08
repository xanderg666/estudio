import oci
import json
import requests

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
    bucket_name="ce-jagm-feediot",
    # prefix="EXAMPLE-prefix-Value",
    start="data_2022020815",#aqui poner la fecha buscada
    # end="EXAMPLE-end-Value",
    # limit=782,
    # delimiter="EXAMPLE-delimiter-Value",
    fields="timeCreated",
    # opc_client_request_id="ocid1.test.oc1..<unique_ID>EXAMPLE-opcClientRequestId-Value",
    # start_after="EXAMPLE-startAfter-Value"
    )

# print(list_objects_response.data)
lis = str(list_objects_response.data)
print(lis)












# data = list_objects_response.data
# print(data[0])

# Get the data from response
# print(list_objects_response.data)
# print(type(data))

# json_data = json.loads(list_objects_response.data)



#
# data = list_objects_response.data
# with open('data.json', 'w') as f:
#    json.dump(data, f)