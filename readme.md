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


install ie, firefox, chrome on your node box(s)

You may also install all browsers on your laptop for local testing

---

Optional: install and start the hub/node(s) with the following command:

`hub`		#starts hub and node

`hub hub`	#starts just hub

`hub node`	#starts just node

---

Optional on `Windows`:

download [cygwin](http://cygwin.com/setup-x86_64.exe)

and install `setup-x86_64.exe -q -P nc,wget,vim,git,subversion,openssh` 

The above `hub` script and some demo test runner scripts are shell scripts.

You may do it - script runners etc, some other funny way

---

##SYNOPSYS

run: `demo`

##USAGE

using `demo` loop runner try any existing tests found in t/... on all browsers with any number of rounds

build own tests like those seen in t/...

expand existing modules found in src/...

add your own modules in src/...

and build more tests in t/...


this is a simple instant example to embed MWS and AE change root test into any automation, jenkins job or just a cmd line :)

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

python -u t/mws/chroot.py

```

take a look at t/mws/chroot.py and just a several functions it refers to
it is a full blown, well focused, complex test - all is tiny, thin, dry

**"We now can**


- do lots of tests just as simple to use as shown above

- focus on building a very specific tests starting far deep down under well implemented thin functional layers of UI navigation

- utilize clean functional composition test design, rather than object oriented bloater

- do all tests tiny (dozen lines), razor sharp focused on 1 thing done very well, lightning fast (run for 30-60s or so)

- enjoy breezy maintanance

- run and tune tests on all 3 (or more) browser types equally

- run and tune tests under stress load conditions on beefy hub or local w/o any special arrangement or effort

- document TC names natural as they are rather than typical tower of object hierarchy abstraction

- bundle tests up into arbitrary sized sets and loop, run it all parallel with python and/or just shell scripts

- the above is easy-clean-fast w/o use of any so-called "tooling, frameworking, dependencies etc etc etc"

- stop using bulky (or any at all) prop, csv, xls, xml, whatever config files

- ..or me gonna start to suffer from day 1 w/o even noticing it

- pass json snippets in env vars - it just works for ~all small or tough layered config needs


**"Be productive**


