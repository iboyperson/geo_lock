#!/usr/bin/env python
import sys
import urllib
import pygeoip

acceptables=[1,2,3,4,5,6,7,8,9,0,"."]
ascii = open('banner.txt', 'r')
asciicont = ascii.read()

#urllib.urlretrieve ("http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz", "GeoLiteCity.dat.gz")
#urllib.urlretrieve ("http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz", "GeoIPASNum.dat.gz")
try:
	try:
		print ('\x1b[1;32;40m' + asciicont + '\x1b[0m')
		ascii.close
		try:
			ip = sys.argv[1]
		except:
			pass
			try:
				ip = eval(int(raw_input('\x1b[1;33;40m'+'Input IP: '+'\x1b[0m')))
			except ValueError:
				print ("Invalid Input")
		gip = pygeoip.GeoIP('GeoLiteCity.dat')
		#asnip = pygeoip.GeoIP('GeoIPASNum.dat')
		rec = gip.record_by_addr(ip)
		
		print '\x1b[1;33;40m'+"City:" + '\x1b[0m' + '        ' + rec['city']
		print '\x1b[1;33;40m'+"Region:" + '\x1b[0m' + '      ' + rec['region_code']
		print '\x1b[1;33;40m'+"Area Code:" + '\x1b[0m' + '  ', rec['area_code']
		print '\x1b[1;33;40m'+"Postal Code:" + '\x1b[0m' + '', rec['postal_code']
		print '\x1b[1;33;40m'+"Time Zone:" + '\x1b[0m' + '   ' + rec['time_zone']
		print '\x1b[1;33;40m'+"DMA Code:" + '\x1b[0m' + '   ', rec['dma_code']
		print '\x1b[1;33;40m'+"Metro Code:" + '\x1b[0m' + ' ', rec['metro_code']
		print '\x1b[1;33;40m'+"County:" + '\x1b[0m'+ '      ' + rec['country_name']
		print '\x1b[1;33;40m'+"County Code:" + '\x1b[0m' + '', rec['country_code'] + ",", rec['country_code3']
		print '\x1b[1;33;40m'+"Latitude:" + '\x1b[0m' + '   ', rec['latitude']
		print '\x1b[1;33;40m'+"Longitude:" + '\x1b[0m' + ' ', rec['longitude']
		print '\x1b[1;33;40m'+"Continent:" + '\x1b[0m' + '   ' + rec['continent']
		
	except KeyboardInterrupt:
		print(' ')
except NameError:
	print('Exiting...')
