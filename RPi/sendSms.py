import requests


def sendSms(text="Hello from python"):
    api_key = "7ce8c8a7"
    api_secret = "a74be2d6ef30ae6c"
    to_number = "+38162687777"


    data = {
        "api_key" : api_key,
        "api_secret" : api_secret,
        "from" : "NEXMO",
        "to" : to_number,
        "text" : text

    }

    r = requests.get("https://rest.nexmo.com/sms/json", params=data)