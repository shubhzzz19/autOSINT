import requests

# Add your key and endpoint
with open(".secrets", "r") as file:
    key = file.read().rstrip()

endpoint = "https://api.veriphone.io"

path = "/v2/verify"

constructed_url = endpoint + path


def phone_osint(phone: str):
    params = {"key": key, "phone": phone, "default_country": "IN"}

    request = requests.post(constructed_url, params=params)

    return request.json()


if __name__ == "__main__":
    print(phone_osint("+919951563938"))
