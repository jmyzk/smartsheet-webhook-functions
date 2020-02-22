import json

from google.cloud import pubsub_v1

project_id = "ss-api-1050012"
topic_name = "ss-webhook"

def smartsheet_webhook_responder(request):

    request_json = request.get_json()

    # for a webhook challenge, return verification
    if request.args and "challenge" in request.args:
        return 'not smartsheet challenge'
    elif request_json and "challenge" in request_json:
        return json.dumps({
            "smartsheetHookResponse": request_json['challenge']
        })

    # if this is a callback
    elif request_json and "scopeObjectId" in request_json:
        sheetid = request_json["scopeObjectId"]
        publish_sheetid(sheetid)
        return json.dumps({
             "callBackFromsmartsheetId": sheetid
        })
    else:
      	return 'neither smartsheet challenge nor callback'

def publish_sheetid(sheetid):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)
    data = str(sheetid)
    print("sheetid", sheetid)
    data = data.encode("utf-8")
    future = publisher.publish(topic_path,  data, spam='eggs')
    print(future.result())
    print("Published messages.")
