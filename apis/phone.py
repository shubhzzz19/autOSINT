import requests

# API key read from hidden file not in git repository
with open("apis/.phone_veriphone_secrets", "r") as file:
    key = file.read().rstrip()

endpoint = "https://api.veriphone.io"

path = "/v2/verify"

constructed_url = endpoint + path

def phone_osint(phone: str):
    params = {"key": key, "phone": phone, "default_country": "IN"}

    request = requests.post(constructed_url, params=params)

    return request.json()
