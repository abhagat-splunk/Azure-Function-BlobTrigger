import logging
import json
import azure.functions as func


def main(myblob: func.InputStream) -> str:
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    logging.info(myblob.__dict__)
    blob_info = {}
    blob_info['name'] = myblob.name
    blob_info['size'] = str(myblob.length)+" bytes"
    blob_info['uri'] = myblob.uri
    blob_data = myblob.read()
    logging.info(blob_data)
    # TODO: Work on image files and other kinds later on.
    try:
        blob_info['data'] = blob_data.decode('utf-8')
    except Exception as e:
        logging.error("Exception faced: {}".format(e))
        blob_info['data'] = blob_data
    payload = json.dumps(blob_info)
    logging.info(payload)
    return payload


"""
If you want to send it to HEC directly, use the following code
"""
#     import requests
#     HEC_URL = "https://trial.splunk.com:8088/services/collector"
#     headers = {
#     "Authorization": "Splunk xyz",
#     "Content-Type": "application/json"
#     }
#     payload = {"event": json.dumps(blob_info), "sourcetype": "manual"}
#     logging.info(payload)
#     response = requests.request(
#         "POST", HEC_URL, headers=headers, data=json.dumps(payload), verify=False)
#     logging.info(response.text)
