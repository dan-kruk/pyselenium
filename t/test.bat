
set PATH=drivers;%PATH%
set PYTHONPATH=src

set cfg={ "browser":"chrome" }

set login={  "url":"http://rdvmden40:8585", ^
	"username":"Administrator","password":"manage" } 

python t/mws/examples/feature.py

