import os
import sys
import urllib
import gzip
if sys.version_info >= (3,0):
    from pathlib import Path
else:
    from pathlib2 import Path

dl = False

ipv4_GeoLite_url = "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz"
ipv4_GeoASN_url = "http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz"
ipv6_GeoLite_url = "http://geolite.maxmind.com/download/geoip/database/GeoLiteCityv6-beta/GeoLiteCityv6.dat.gz"
ipv6_GeoASN_url = "http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNumv6.dat.gz"

ipv4_path = Path('./ipv4')
ipv6_path = Path('./ipv6')
GeoLite_path = Path('./GeoLiteCity.dat')
GeoASN_path = Path('./GeoIPASNum.dat')
GeoLite_gz_path = Path('./GeoLiteCity.dat.gz')
GeoASN_gz_path = Path('./GeoIPASNum.dat.gz')


def file_check(iptype):
    if iptype == "ipv4":
        ipv4_check()
    elif iptype == "ipv6":
        ipv6_check()
    else:
        print ('[Error: Invalid IP]')

def ipv4_check():
    if ipv4_path.exists() == False:
        os.makedirs("ipv4")
    os.chdir("ipv4")
    if GeoLite_path.exists() == False:
        urllib.urlretrieve(ipv4_GeoLite_url, "GeoLiteCity.dat.gz")
        unzip('GeoLiteCity.dat.gz', 'GeoLiteCity.dat')
    if GeoASN_path.exists() == False:
        urllib.urlretrieve(ipv4_GeoASN_url, "GeoIPASNum.dat.gz")
        unzip('GeoIPASNum.dat.gz', 'GeoIPASNum.dat')
    os.chdir("..")


def ipv6_check():
    if ipv6_path.exists() == False:
        os.makedirs("ipv6")
    os.chdir("ipv6")
    if not GeoLite_url.exists() == False:
        urllib.urlretrieve(ipv6_GeoLite_url, "GeoLiteCity.dat.gz")
        unzip('GeoLiteCity.dat.gz', 'GeoLiteCity.dat')
    if not GeoASN_path.exists() == False:
        urllib.urlretrieve(ipv6_GeoASN_url, "GeoIPASNum.dat.gz")
        unzip('GeoIPASNum.dat.gz', 'GeoIPASNum.dat')
    os.chdir("..")


def unzip(infile, outfile):
    geoin = gzip.open(infile, 'rb')
    geoout = open(outfile, 'wb')
    geoout.write(geoin.read())
    os.remove(infile)
