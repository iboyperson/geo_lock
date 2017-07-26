#!/usr/bin/env python
import sys
import os
import pygeoip

#My Files
import fileman
import ipman

iptype = ""

try:
	ip = str(sys.argv[1])
except:
	ip = raw_input('\x1b[1;33;40m'+'Input IP: '+'\x1b[0m')

def print_banner():
	ascii = open('banner.txt', 'r')
	asciicont = ascii.read()
	return ('\x1b[1;32;40m' + asciicont + '\x1b[0m')

iptype = ipman.ip_version(ip)
print '\x1b[1;33;40m' + '[Downloading Databases]' + '\x1b[0m'
fileman.file_check(iptype)
try:
	try:
		#Prints the GEO_LOCK ascii art
		sys.stdout.write("\x1b[1A" + print_banner() + '\n')
		#Set working directory to where db's for ip version are stored
		os.chdir(iptype)
		#Opens db's for usage
		gip = pygeoip.GeoIP('GeoLiteCity.dat')
		asnip = pygeoip.GeoIP('GeoIPASNum.dat')
		#Retrieves data for give ip
		rec = gip.record_by_addr(ip)
		asn = asnip.asn_by_addr(ip)
		#Prints the data for given ip
		print '\x1b[1;33;40m'+"City:" + '\x1b[0m' + '        ' + rec['city']
		print '\x1b[1;33;40m'+"Region:" + '\x1b[0m' + '      ' + rec['region_code']
		print '\x1b[1;33;40m'+"Area Code:" + '\x1b[0m' + '  ', rec['area_code']
		print '\x1b[1;33;40m'+"Postal Code:" + '\x1b[0m' + '', rec['postal_code']
		print '\x1b[1;33;40m'+"Time Zone:" + '\x1b[0m' + '   ' + rec['time_zone']
		print '\x1b[1;33;40m'+"DMA Code:" + '\x1b[0m' + '   ', rec['dma_code']
		print '\x1b[1;33;40m'+"Metro Code:" + '\x1b[0m' + ' ', rec['metro_code']
		print '\x1b[1;33;40m'+"County:" + '\x1b[0m'+ '      ' + rec['country_name']
		print '\x1b[1;33;40m'+"County Code:" + '\x1b[0m' + '', rec['country_code'] + "," + rec['country_code3']
		print '\x1b[1;33;40m'+"Latitude:" + '\x1b[0m' + '   ', rec['latitude']
		print '\x1b[1;33;40m'+"Longitude:" + '\x1b[0m' + ' ', rec['longitude']
		print '\x1b[1;33;40m'+"Continent:" + '\x1b[0m' + '   ' + rec['continent']
		print '\x1b[1;33;40m'+"ASN:" + '\x1b[0m' + '         ' + asn

	except KeyboardInterrupt:
		print(' ')
except NameError:
	print('Exiting...')
