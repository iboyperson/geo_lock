#!/usr/bin/env python
import sys
import maxman
import dataman


try:
	ip = str(sys.argv[1])
except:
	ip = raw_input('\x1b[1;33;40m'+'Input IP:'+'\x1b[0m' + " ")

def print_banner():
	ascii = open('banner.txt', 'r')
	asciicont = ascii.read()
	return ('\x1b[1;32;40m' + asciicont + '\x1b[0m')

maxman.maxdbcheck(ip)
print '\x1b[1;33;40m' + '[Downloading Databases]' + '\x1b[0m'
data = dataman.getdata(ip)
try:
	try:
		#Prints the GEO_LOCK ascii art
		sys.stdout.write("\x1b[1A" + print_banner() + '\n')
		print ('\x1b[1;33;40m'+"IP:" + '\x1b[0m' + '               ' + data['ip'])
		print ('\x1b[1;33;40m'+"Host:" + '\x1b[0m' + '             ' + data['host'])
		print ('\x1b[1;33;40m'+"City:" + '\x1b[0m' + '             ' + data['city'])
		print ('\x1b[1;33;40m'+"Region:" + '\x1b[0m' + '           ' + data['region'])
		print ('\x1b[1;33;40m'+"County:" + '\x1b[0m' + '           ' + data['country'])
		print ('\x1b[1;33;40m'+"Continent:" + '\x1b[0m' + '        ' + data['continent'])
		print ('\x1b[1;33;40m'+"Geo Coordinates:" + '\x1b[0m' + '  ' + data['geoloc'])
		print ('\x1b[1;33;40m'+"Postal Code:" + '\x1b[0m' + '      ' + data['zip_code'])
		print ('\x1b[1;33;40m'+"Area Code:" + '\x1b[0m' + '        ' + data['area_code'])
		print ('\x1b[1;33;40m'+"DMA Code:" + '\x1b[0m' + '         ' + data['dma_code'])
		print ('\x1b[1;33;40m'+"Time Zone:" + '\x1b[0m' + '        ' + data['time_zone'])
		print ('\x1b[1;33;40m'+"ISP:" + '\x1b[0m' + '              ' + data['isp'])
		print ('\x1b[1;33;40m'+"Organization:" + '\x1b[0m' + '     ' + data['org'])
		print ('\x1b[1;33;40m'+"ASN:" + '\x1b[0m' + '              ' + data['asn'])
		print ('\x1b[1;33;40m'+"Using Proxy?:" + '\x1b[0m' + '     ' + data['proxy'])
		print ('\x1b[1;33;40m'+"On Mobile?:" + '\x1b[0m' + '       ' + data['mobile'])

	except KeyboardInterrupt:
		print(' ')
except NameError:
	print('Exiting...')
