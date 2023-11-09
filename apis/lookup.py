import json
import requests

def lookup(ip):
    with requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,"
            f"regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,"
            f"hosting,query") as result:
        info = result.json()

        if info['status'] == 'fail':
            print(f"IP Lookup for {ip} failed with the message: {info['message']}")
        else:
            print(f"IP Information for {ip}:")
            print(f"Country: {info['country']} ({info['countryCode']})")
            print(f"Region: {info['regionName']} ({info['region']})")
            print(f"City: {info['city']}")
            print(f"Zip Code: {info['zip']}")
            print(f"Latitude: {info['lat']}, Longitude: {info['lon']}")
            print(f"Timezone: {info['timezone']} (Offset: {info['offset']})")
            print(f"Currency: {info['currency']}")
            print(f"ISP: {info['isp']}")
            print(f"Organization: {info['org']}")
            print(f"AS: {info['as']} ({info['asname']})")
            print(f"Reverse DNS: {info['reverse']}")
            print(f"Mobile: {info['mobile']}")
            print(f"Proxy: {info['proxy']}")
            print(f"Hosting: {info['hosting']}")

while True:
    ip = input('Enter IP you want to lookup: ')
    lookup(ip)
    question = input("Would you like to keep looking up IPs? Say yes or no: ")
    if question.lower() == "no":
        break