# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
ai_language_client = oci.ai_language.AIServiceLanguageClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
detect_language_key_phrases_response = ai_language_client.detect_language_key_phrases(
    detect_language_key_phrases_details=oci.ai_language.models.DetectLanguageKeyPhrasesDetails(
        text="RENOVACION LICENCIA ANUAL CONTPAQI XML EN LINEA"), opc_request_id="0SKY9K2TP3AZQXEDMDL2<unique_ID>")

# Get the data from response
print(detect_language_key_phrases_response.data)