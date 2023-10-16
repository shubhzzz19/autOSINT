import json
import requests


def lookup(ip):
    with requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,"
            f"regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,"
            f"hosting,query") as result:

        info = result.json()
    return print(json.dumps(info, indent=4))


while True:
    ip = input('Enter IP you want to lookup: ')
    lookup(ip)
    question = input("Would you like to keep looking up IP's? Say yes or no.")
    if question.lower() == "no":
        break
