# The OCI SDK must be installed for this example to function properly.
# Installation instructions can be found here: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/pythonsdk.htm

import requests
import oci
from oci.signer import Signer

config = oci.config.from_file("C:/Users/jorge/PycharmProjects/oci/venv/jorgeg/conf/config") # replace with the location of your oci config file
auth = Signer(
  tenancy=config['tenancy'],
  user=config['user'],
  fingerprint=config['fingerprint'],
  private_key_file_location=config['key_file'],
  pass_phrase=config['pass_phrase'])

endpoint = 'https://modeldeployment.us-ashburn-1.oci.customer-oci.com/ocid1.datasciencemodeldeployment.oc1.iad.amaaaaaau2o4l2iabemrjshhckakg5ph4e5djgukthy5qgew52s3lsazb6uq/predict'

body ={
  'Empleo': {184: 0},
 'Hermanos': {184: 0},
 'ClaseSocial': {184: 3},
 'NivelDeSatisfaccion': {184: 1},
 'EstadoCivil': {184: 2},
 'Promedio': {184: 2}
}

resu = requests.post(endpoint, json=body, auth=auth).json()

print("------------------RESULTADO-------------"+"\n")
print(resu)
if resu["prediction"][0] == 1:

    print ("\n"+'El estudiante va a desertar')
    print("\n"+"------------------FIN-------------" + "\n")
else:
    print ('Va a continuar')
    print("\n" + "------------------FIN-------------" + "\n")