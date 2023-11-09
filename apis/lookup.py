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
            return '\n'.join([
                f"IP Information for {ip}",
                f"Country: {info['country']} ({info['countryCode']})",
                f"Region: {info['regionName']} ({info['region']})",
                f"City: {info['city']}",
                f"Zip Code: {info['zip']}",
                f"Latitude: {info['lat']}, Longitude: {info['lon']}",
                f"Timezone: {info['timezone']} (Offset: {info['offset']})",
                f"Currency: {info['currency']}",
                f"ISP: {info['isp']}",
                f"Organization: {info['org']}",
                f"AS: {info['as']} ({info['asname']})",
                f"Reverse DNS: {info['reverse']}",
                f"Mobile: {info['mobile']}",
                f"Proxy: {info['proxy']}",
                f"Hosting: {info['hosting']}"
            ])