import json
import requests


def lookup(ip):
    with requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,"
            f"regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,"
            f"hosting,query") as result:

        info = result.json()
    return json.dumps(info, indent=4)
