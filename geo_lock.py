#!/usr/bin/env python
import sys
import pygeoip
acceptables=[1,2,3,4,5,6,7,8,9,0,"."]	
try:
	try:
	        ascii = """\
  ______   ________   ______         __         ______    ______   __    __ 
 /      \ /        | /      \       /  |       /      \  /      \ /  |  /  |
/$$$$$$  |$$$$$$$$/ /$$$$$$  |      $$ |      /$$$$$$  |/$$$$$$  |$$ | /$$/ 
$$ | _$$/ $$ |__    $$ |  $$ |      $$ |      $$ |  $$ |$$ |  $$/ $$ |/$$/  
$$ |/    |$$    |   $$ |  $$ |      $$ |      $$ |  $$ |$$ |      $$  $$<   
$$ |$$$$ |$$$$$/    $$ |  $$ |      $$ |      $$ |  $$ |$$ |   __ $$$$$  \  
$$ \__$$ |$$ |_____ $$ \__$$ |      $$ |_____ $$ \__$$ |$$ \__/  |$$ |$$  \ 
$$    $$/ $$       |$$    $$/______ $$       |$$    $$/ $$    $$/ $$ | $$  |
 $$$$$$/  $$$$$$$$/  $$$$$$//      |$$$$$$$$/  $$$$$$/   $$$$$$/  $$/   $$/ 
                            $$$$$$/                                         
"""
	        print (' ')
	        print ('\x1b[1;32;40m'+ascii+'\x1b[0m')
	        try:
	                ip = sys.argv[1]
	        except:
	                pass
			try:
		                ip = eval(int(raw_input('\x1b[1;33;40m'+'Input IP: '+'\x1b[0m')))
			except ValueError:
			    print ("Invalid Input")
	        gip = pygeoip.GeoIP('GeoLiteCity.dat')
	        rec = gip.record_by_addr(ip)
	        for val in rec.items():
	                print '==========================='
	                print '\x1b[1;33;40m'+'%s:''\x1b[0m''%s'%(val)
	except KeyboardInterrupt:
		print(' ')
except NameError:
	print('Exiting...')
