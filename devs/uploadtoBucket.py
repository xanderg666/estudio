from __future__ import print_function
import os
import oci
from oci.object_storage import UploadManager
from oci.object_storage.models import CreateBucketDetails
from oci.object_storage.transfer.constants import MEBIBYTE


def progress_callback(bytes_uploaded):
    print("{} additional bytes uploaded".format(bytes_uploaded))


config = oci.config.from_file()
compartment_id = "ocid1.compartment.oc1..aaaaaaaaerfyh5xmsg3rsmyma7kvw3mdrqxbjrepzttvfrik4o7dvrjhgwja"
object_storage = oci.object_storage.ObjectStorageClient(config)

namespace = object_storage.get_namespace().data
bucket_name = "CE_JAGM_python_sdk"
object_name = "python-sdk-example-object"

print("Creating a new bucket {!r} in compartment {!r}".format(bucket_name, compartment_id))
request = CreateBucketDetails()
request.compartment_id = compartment_id
request.name = bucket_name
bucket = object_storage.create_bucket(namespace, request)

# create example file to upload
filename = 'multipart_object_content.txt'
file_size_in_mebibytes = 10
sample_content = b'a'
with open(filename, 'wb') as f:
    while f.tell() < MEBIBYTE * file_size_in_mebibytes:
        f.write(sample_content * MEBIBYTE)

print("Uploading new object {!r}".format(object_name))

# upload manager will automatically use mutlipart uploads if the part size is less than the file size
part_size = 2 * MEBIBYTE  # part size (in bytes)
upload_manager = UploadManager(object_storage, allow_parallel_uploads=True, parallel_process_count=3)
response = upload_manager.upload_file(
    namespace, bucket_name, object_name, filename, part_size=part_size, progress_callback=progress_callback)