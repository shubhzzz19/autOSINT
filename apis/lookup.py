import json
import requests

def lookup(ip):
    with requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,"
            f"regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,"
            f"hosting,query") as result:
        info = result.json()

        if info['status'] == 'fail':
            return (f"IP Lookup for {ip} failed with the message: {info['message']}")
        else:
            return {"ip": ip,
            "country": info['country'],
            "countryCode": info['countryCode'],
            "region": info['region'],
            "regionName": info['regionName'],
            "city": info['city'],
            "zip": info['zip'],
            "lat": info['lat'],
            "lon": info['lon'],
            "timezone": info['timezone'],
            "offset": info['offset'],
            "currency": info['currency'],
            "isp": info['isp'],
            "org": info['org'],
            "as": info['as'],
            "asname": info['asname'],
            "reverse": info['reverse'],
            "mobile": info['mobile'],
            "proxy": info['proxy'],
            "hosting": info['hosting']
            }