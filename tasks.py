from microsoftbotframework import ReplyToActivity
import requests
import json

# https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment
"""
POST
https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment

Ocp-Apim-Subscription-Key:4cfe6f744f1b486db3fa83d874bafdd9
Content-Type:application/json
Accept:application/json
"""


# https://api.korbit.co.kr/v1/ticker

def echo_response(message):
    print(message)

    if message["type"] == "message":
        if "bitcoin" in message["text"]:

            r = requests.get("https://api.korbit.co.kr/v1/ticker")
            bitcoin_price = r.json()["last"]
            msg = "bitcoin price is %s" % bitcoin_price
            print(msg)
            #ReplyToActivity(fill=message, text=msg).send()
        else:
            data = {
                "documents": [
                    {
                        "language": "en",
                        "id": "81a86d6e-8ce1-4582-932d-b01c4c1adc64",
                        "text": message["text"]
                    }
                ]
            }
            headers = {'Ocp-Apim-Subscription-Key': 'a4828d6a9e65477492febf25736aa2b2',
                       'Content-Type': 'application/json',
                       'Accept': 'application/json',
                       }

            r = requests.post("https://eastus2.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment",
                              data=json.dumps(data),
                              headers=headers)
            print( r.json() )
            emo_score = r.json()["documents"][0]["score"]
            msg = "emotion score is %s\n" % emo_score

            if emo_score > 0.5:
                msg = msg + "You look happy!"
            else:
                msg = msg + "You look unhappy.."

            print(msg)

            #ReplyToActivity(fill=message, text=msg).send()

message = { "text": "bitcoin", "type": "message" }
echo_response(message)

message = { "text": "I am happy", "type": "message" }
echo_response(message)

