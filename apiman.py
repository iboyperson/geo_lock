import urllib3
import json

headers = {'User-Agent': "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2a1pre) Gecko/20090428 Firefox/3.6a1pre"}
http = urllib3.PoolManager(headers=headers)

def ipapiload(ip):
    ipapi = http.request('GET',"http://ip-api.com/json/" + str(ip) + "?fields=262143")
    ipapi_cont = json.loads(ipapi.data.decode())
    return ipapi_cont

def freegeoipload(ip):
    freegeoip = http.request('GET',"http://freegeoip.net/json/" + str(ip))
    freegeoip_cont = json.loads(freegeoip.data.decode())
    return freegeoip_cont
