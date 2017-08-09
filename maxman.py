import os
import pygeoip
import fileman
import ipman

iptype = ""

def maxdbcheck(ip):
    iptype = ipman.ip_version(ip)
    fileman.file_check(iptype)

def maxcityload(ip):
    iptype = ipman.ip_version(ip)
    #Set working directory to where db's for ip version are stored
    os.chdir(iptype)
    #Opens db's for usage
    gip = pygeoip.GeoIP('GeoLiteCity.dat')
    #Retrieves data for give ip
    rec = gip.record_by_addr(ip)
    #Return to default directory
    os.chdir("..")
    #Return record
    return rec

def maxasnload(ip):
    iptype = ipman.ip_version(ip)
    #Set working directory to where db's for ip version are stored
    os.chdir(iptype)
    #Opens db's for usage
    asnip = pygeoip.GeoIP('GeoIPASNum.dat')
    #Retrieves data for give ip
    asn = asnip.asn_by_addr(ip)
    #Return to default directory
    os.chdir("..")
    #Return ASN
    return asn
