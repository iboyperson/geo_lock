#!/usr/bin/env python
import sys
import pygeoip
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
                ip = raw_input('\x1b[1;33;40m'+'Input IP: '+'\x1b[0m')
        gip = pygeoip.GeoIP('GeoLiteCity.dat')
        rec = gip.record_by_addr(ip)
        for val in rec.items():
                print '==========================='
                print '\x1b[1;33;40m'+'%s:''\x1b[0m''%s'%(val)
except KeyboardInterrupt:
    print(' ')
