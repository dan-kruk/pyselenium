##NAME

**pyselenium** - productive UI testing

##SETUP

```sh 
git clone http://irepo.eur.ad.sag/scm/~dkrukov/pyselenium.git
```
install [python 3.5](https://www.python.org/downloads)

install selenium:	`python -m pip install selenium`

_on `RH/Centos linux` may use:_ `install_pyse_rh` instead of the above 2 steps

`On Windows`

prepend system env `PATH` variable with the following:

`C:\Users\Administrator\AppData\Local\Programs\Python\Python35-32\Scripts\;C:\Users\Administrator\AppData\Local\Programs\Python\Python35-32\;c:\cygwin64\bin;`


install ie, firefox, chrome on your node box(s). You may also install these on your laptop for local work

---

Optional(but cool): install and start the hub/node(s) with the following command:

`hub`		#starts hub and node

`hub hub`	#starts just hub

`hub node`	#starts just node

---

Optional on `Windows` (for brave and productive):

download [cygwin](http://cygwin.com/setup-x86_64.exe)

and install `setup-x86_64.exe -q -P nc,wget,vim,git,subversion,openssh` 

---

##SYNOPSYS

run: `demo`

##USAGE

using `demo` loop runner try any existing tests found in t/... on all browsers with any number of rounds

build own tests like those seen in t/...

expand existing modules found in src/...

add your own modules in src/...

and build more tests in t/...


this is a simple instant example to embed MWS and AE change root test into any automation, jenkins job or just a command line :)

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

**"You now can**

- do lots of tests just as simple to use as shown

- I recommend all tests to be tiny (dozen lines), very focused on 1 thing done well and complete in ~<1min

- run and tune tests on all 3 (or more) browsers

- run and tune tests under stress load conditions on hub or local

- document TC names short and precise

- bundle up tests into sets with python or just shell scripts -it is easy clean fast w/o use of any "fancy messy frameworks"

- don't use bulky (or any at all) config files, csv, xls, xml - or you gonna start to suffer from day 1 w/o even noticing it

- json snippets passed in env vars puts all config hassle away for good

**"Be productive**


