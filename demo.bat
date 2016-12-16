
rem cd /D C:\cygwin64\home\Administrator\pyselenium

set cfg={  "url":"http://rdvmden28:8585","username":"Administrator","password":"manage", ^
	"browser":"chrome", "remote":true,"hub":"http://usvardvmden141:4444/wd/hub","wait":10  }

set ccs={ "name":"BVTEnv", ^
	"mapendpoints":{"mwspath":"alta" } }

set PYTHONPATH=src

python -u t/mws/chroot.py

