#!/bin/bash
function install 
{
  if [ ! -d //home/iboyperson/scripts/geo_lock/testenv/usr/share/geo_lock ]
  then
    mkdir /home/iboyperson/scripts/geo_lock/testenv/usr/share/geo_lock
  fi
  cp `pwd`/* /home/iboyperson/scripts/geo_lock/testenv/usr/share/geo_lock
  touch /home/iboyperson/scripts/geo_lock/testenv/usr/bin/geo_lock
  echo '#!/bin/bash' > geo_lock
  echo "export GEO_LOCK_HOME='/home/iboyperson/scripts/geo_lock/testenv/usr/share/geo_lock'" > geo_lock
  echo '$GEO_LOCK_HOME/geo_lock $*' > geo_lock
}

if [ $EUID != 0 ]
then
  echo 'Please run as root.'
  exit
fi

if [ -f /home/iboyperson/scripts/geo_lock/testenv/usr/bin/geo_lock ]
then
  echo 'geo_lock already installed. Do you want to uninstall? (y/n)'
else
  install
fi