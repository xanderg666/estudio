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
bucket_name = "jg-bucket-df"
#nombre del objecto en el bucket
object_name = "copia_ds_2/9/22"
filename = "foo.zip"

part_size = 2 * MEBIBYTE  # part size (in bytes)
upload_manager = UploadManager(object_storage, allow_parallel_uploads=True, parallel_process_count=3)
response = upload_manager.upload_file(
    namespace, bucket_name, object_name, filename, part_size=part_size, progress_callback=progress_callback)