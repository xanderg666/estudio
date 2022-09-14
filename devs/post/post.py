# The OCI SDK must be installed for this example to function properly.
# Installation instructions can be found here: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/pythonsdk.htm

import requests
import oci
from oci.signer import Signer

config = oci.config.from_file("~/.oci/config") # replace with the location of your oci config file
auth = Signer(
  tenancy=config['tenancy'],
  user=config['user'],
  fingerprint=config['fingerprint'],
  private_key_file_location=config['key_file'],
  pass_phrase=config['pass_phrase'])

endpoint = 'https://modeldeployment.us-ashburn-1.oci.customer-oci.com/ocid1.datasciencemodeldeployment.oc1.iad.amaaaaaallb34niaywd7nhybewke6qt5rgnaye7ww72dvyl5jlqbcl23le3q/predict'
body = {"MSSubClass":{"7":60},"MSZoning":{"7":3},"LotFrontage":{"7":60.0},"LotArea":{"7":10382},"Street":{"7":1},"LotShape":{"7":0},"LandContour":{"7":3},"Utilities":{"7":0},"LotConfig":{"7":0},"LandSlope":{"7":0},"Neighborhood":{"7":14},"Condition1":{"7":4},"Condition2":{"7":2},"BldgType":{"7":0},"HouseStyle":{"7":5},"OverallQual":{"7":7},"OverallCond":{"7":6},"YearBuilt":{"7":1973},"YearRemodAdd":{"7":1973},"RoofStyle":{"7":1},"RoofMatl":{"7":1},"Exterior1st":{"7":6},"Exterior2nd":{"7":6},"MasVnrType":{"7":3},"MasVnrArea":{"7":240.0},"ExterQual":{"7":3},"ExterCond":{"7":4},"Foundation":{"7":1},"BsmtQual":{"7":2},"BsmtCond":{"7":3},"BsmtExposure":{"7":2},"BsmtFinType1":{"7":0},"BsmtFinSF1":{"7":859},"BsmtFinType2":{"7":1},"BsmtFinSF2":{"7":32},"BsmtUnfSF":{"7":216},"TotalBsmtSF":{"7":1107},"Heating":{"7":1},"HeatingQC":{"7":0},"CentralAir":{"7":1},"Electrical":{"7":4},"1stFlrSF":{"7":1107},"2ndFlrSF":{"7":983},"LowQualFinSF":{"7":0},"GrLivArea":{"7":2090},"BsmtFullBath":{"7":1},"BsmtHalfBath":{"7":0},"FullBath":{"7":2},"HalfBath":{"7":1},"BedroomAbvGr":{"7":3},"KitchenAbvGr":{"7":1},"KitchenQual":{"7":3},"TotRmsAbvGrd":{"7":7},"Functional":{"7":6},"Fireplaces":{"7":2},"GarageType":{"7":1},"GarageYrBlt":{"7":1973.0},"GarageFinish":{"7":1},"GarageCars":{"7":2},"GarageArea":{"7":484},"GarageQual":{"7":4},"GarageCond":{"7":4},"PavedDrive":{"7":2},"WoodDeckSF":{"7":235},"OpenPorchSF":{"7":204},"EnclosedPorch":{"7":228},"3SsnPorch":{"7":0},"ScreenPorch":{"7":0},"PoolArea":{"7":0},"MiscVal":{"7":350},"MoSold":{"7":11},"YrSold":{"7":2009},"SaleType":{"7":8},"SaleCondition":{"7":4}} # payload goes here

vv=requests.post(endpoint, json=body, auth=auth).json()
print(vv)