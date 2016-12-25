##NAME

**pyselenium** - productive UI testing

##SETUP

```sh 
git clone http://irepo.eur.ad.sag/scm/~dkrukov/pyselenium.git
```
---

install [python 3.5](https://www.python.org/downloads)

install selenium modules `python -m pip install selenium`

_on `RH/Centos linux` may use_ `install_pyse_rh` instead of the above 2 steps

`On Windows`

prepend system env `PATH` variable with the following

`C:\Users\Administrator\AppData\Local\Programs\Python\Python35-32\Scripts\;C:\Users\Administrator\AppData\Local\Programs\Python\Python35-32\;c:\cygwin64\bin;`

install ie, firefox, chrome browsers on your node box(s)

You may also install all browsers on your laptop for local testing

---

install browser drivers and start selenium

`hub`		#hub and node

`hub hub`	#just hub

`hub node`	#just node which points to local hub

`hub node host:port`	#just node, which points remote host:port hub

_Note: stop the above selenium hub/node cmd if remote test exec is not needed_

---

Optional on `Windows`

download [cygwin](http://cygwin.com/setup-x86_64.exe)

install `setup-x86_64.exe -q -P nc,wget,vim,git,subversion,openssh` 

The above mentioned `hub` script is a nice shell script, which can now be run on windows

Or you may run hub and test suite runner scripts, using your comfort way (bas/gradle/ant/bat/jenkins whatever else)

---

##USAGE

look at well commented feature test example: [t/mws/examples/feature.py](../browse/t/mws/examples/feature.py)

run it:

```bash

export cfg='{  
	"url":"http://rdvmden40:8585",
	"browser":"chrome"
    }'

export PYTHONPATH=src PATH=drivers:$PATH

python t/mws/examples/feature.py

```

find and try lot more tests at [t/mws](../browse/t/mws)

put and run tests in bat or sh script:

`t\test.bat`

`t/test`

##DEVEL

build own tests like those seen in [t/mws](../browse/t/mws)

expand existing modules found in [src/mws](../browse/src/mws)

add your own modules in [src/mws](../browse/src/mws)

and build more cool tests in [t/mws](../browse/t/mws)

check doc at [Selenium with Python](http://selenium-python.readthedocs.io)

**"We now can**


- do lots of tests which are just as simple and informal to use as shown above

- focus on building a very specific feature tests rather than object abstruction maintanace

- start coding far deep down under well implemented thin functional layers of UI navigation

- utilize imperative/functional composition test design, rather than object oriented bloater

- do all tests tiny (a few lines), razor sharp focused on 1 thing done very well, lightning fast (run for 30-60s or so)

- no state, concurrency concerns

- enjoy breezy maintanance

- run and tune tests on all 3 (or more) browser types equally

- run and tune tests under stress load conditions on beefy hub or local -no special arrangement or effort needed

- document TC steps natural and ordered as they are rather than typical tower of object hierarchy abstraction

- bundle tests up into arbitrary sized sets, loop and run it all parallel with simple scripts

- stop using clumsy prop, csv, xls, xml, whatever config files

- pass json snippets in env vars - it just works for ~all small, complex layered or iterative config needs

- "tooling, frameworking, ide-ing, dependencies and so on" - it is all your choice and is not mandatory or pushed by any means


**"Be productive**

