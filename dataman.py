import apiman
import maxman

def getdata(ip):
    maxcity_cont = maxman.maxcityload(ip)
    maxasn_cont = maxman.maxasnload(ip)
    ipapi_cont = apiman.ipapiload(ip)
    freegeoip_cont = apiman.freegeoipload(ip)

    ipaddr = ipapi_cont["query"]
    host = ipapi_cont["reverse"]
    city = maxcity_cont["city"]
    region = ipapi_cont["regionName"] + " (" + maxcity_cont["region_code"] + ")"
    country = maxcity_cont["country_name"] + " (" + maxcity_cont["country_code"] + ")"
    continent = maxcity_cont["continent"]
    geoloc = str(maxcity_cont["latitude"]) + ", " + str(maxcity_cont["longitude"])
    zip_code = str(maxcity_cont["postal_code"])
    area_code = str(maxcity_cont["area_code"])
    dma_code = str(maxcity_cont["dma_code"])
    time_zone = maxcity_cont["time_zone"]
    isp = ipapi_cont["isp"]
    org = ipapi_cont["org"]
    asn = maxasn_cont
    proxy = str(ipapi_cont["proxy"])
    mobile = str(ipapi_cont["mobile"])

    data = {
     "ip":ipaddr,
     "host":host,
     "city":city,
     "region":region,
     "country":country,
     "continent":continent,
     "geoloc":geoloc,
     "zip_code":zip_code,
     "area_code":area_code,
     "dma_code":dma_code,
     "time_zone":time_zone,
     "isp":isp,
     "org":org,
     "asn":asn,
     "proxy":proxy,
     "mobile":mobile}
    return data
