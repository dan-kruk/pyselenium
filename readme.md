##NAME

**pyselenium** - get all UI test done

##SETUP

```sh 
git clone http://irepo.eur.ad.sag/scm/~dkrukov/pyselenium.git && cd pyselenium
export $PYTHONPATH=src PATH=:$PATH
```
install python:		https://www.python.org/downloads
install selenium:	`python -m pip install selenium`

_on rh linux may use:_ `install_pyse_rh` instead of the above 2 steps

`On Windows`

- prepend system env `PATH` variable with the following:
`C:\Users\Administrator\AppData\Local\Programs\Python\Python35-32\Scripts\;C:\Users\Administrator\AppData\Local\Programs\Python\Python35-32\;c:\cygwin64\bin;`


install ie, firefox, chrome on your node box(s). You may also install it on your laptop

-------------
Optional(but cool): install and start the hub/node(s) with the following command:

`hub`		#starts hub and node
`hub hub`	#starts just hub
`hub node`	#starts just node

--------------

Optional on `Windows` (to be productive):

download [cygwin](http://cygwin.com/setup-x86_64.exe) and install `setup-x86_64.exe -q -P nc,wget,vim,git,subversion,openssh` 
-------------

##SYNOPSYS

run: `demo`

##USAGE

using `demo` loop runner try any existing tests found in t/demo/... on all browsers any number of rounds

build own tests like those seen in t/...

expand existing modules found in src/...

add your own modules in src/...

and build more tests...


this is a simple instant example to embed MWS and AE change root test into any automation, jenkins job or into the superior framework - your command line :)

```bash
cd; cd pyselenium && git pull || { git clone http://irepo.eur.ad.sag/scm/~dkrukov/pyselenium.git && cd pyselenium; } 

export cfg='{  
	"url":"http://rdvmden28:8585","username":"Administrator","password":"manage",
	"browser":"ie", "remote":true,"hub":"http://usvardvmden141:4444/wd/hub","wait":10
    }'

export ccs='{
	"name":"BVTEnv",
	"mapendpoints":{"mwspath":"alta" }
    }'

export PYTHONPATH=src

time python -u t/mws/chroot.py

```

Now you can do any test(s) just as simple as such

