#!/usr/bin/env python

import dataman

data = dataman.getdata("70.171.231.84")

print data["ip"]
print data["host"]
print data["city"]
print data["region"]
print data["country"]
print data["continent"]
print data["geoloc"]
print data["zip"]
print data["area_code"]
print data["dma_code"]
print data["time_zone"]
print data["isp"]
print data["org"]
print data["asn"]
print data["proxy"]
print data["mobile"]
