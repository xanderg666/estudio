# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

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

print(list_objects_response.data)


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