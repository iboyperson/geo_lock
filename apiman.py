import requests
import json

headers = {'User-Agent': "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2a1pre) Gecko/20090428 Firefox/3.6a1pre"}

def ipapiload(ip):
    ipapi = requests.get("http://ip-api.com/json/" + str(ip) + "?fields=262143", headers=headers, verify=False)
    ipapi_cont = json.loads(ipapi.content)
    return ipapi_cont

def freegeoipload(ip):
    freegeoip = requests.get("http://freegeoip.net/json/" + str(ip), headers=headers, verify=False)
    freegeoip_cont = json.loads(freegeoip.content)
    return freegeoip_cont
