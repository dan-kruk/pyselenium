##NAME

**pyselenium** - productive UI testing

##SETUP

```sh 
git clone http://irepo.eur.ad.sag/scm/~dkrukov/pyselenium.git
```
---

install [python 3.5+](https://www.python.org/downloads)

install selenium module `python -m pip install selenium`

_on `RH/Centos linux` may run_ `install_pyse_rh` instead of the above 2 steps

`On Windows`

prepend system env `PATH` variable with the following:

`%HOMEDRIVE%%HOMEPATH%\AppData\Local\Programs\Python\Python35-32\Scripts\;%HOMEDRIVE%%HOMEPATH%\AppData\Local\Programs\Python\Python35-32\;c:\cygwin64\bin;`

add `PYTHONPATH=src` system env variable

`on linux (or cygwin)`

add to ~/.bashrc: `export PYTHONPATH=src`

install ie, firefox, chrome browsers on your remote node machines

You may also install all or needed browsers on your laptop for local testing

---

install browser drivers and start selenium

`hub`		#hub and node

`hub hub`	#just hub

`hub node`	#just node which points to local hub

`hub node host:port`	#just node, which points remote host:port hub

_Note: the above hub/node cmd enters selenium service mode after installing drivers. So term it if remote test execution on a hub is not needed_

---

Optional on `Windows`

download [cygwin](http://cygwin.com/setup-x86_64.exe)

install `setup-x86_64.exe -q -P nc,wget,vim,git,subversion,openssh` 

The above mentioned `hub` script is a nice shell script, which can now be run on windows

Or you may run hub and test suite runner scripts, using your comfort way such as bat/bas/gradle/ant/jenkins etc

---

##USAGE

look at full blown well explained feature test example: [t/mws/examples/feature.py](../browse/t/mws/examples/feature.py)

run it on windows:

```bat
set cfg={ "browser":"chrome" }

set login={  "url":"http://rdvmden40:8585", ^
	"username":"Administrator","password":"manage" } 

python t/mws/examples/feature.py

```
or on linux (or cygwin) pointing to a remote browser:

```bash
export cfg="{ 'remote':'true', 'hub':'http://usvardvmden141:4444/wd/hub',
	'browser':'chrome'
    }"

export login="{ 'url':'http://rdvmden40:8585' }"

python -u t/mws/examples/feature.py

```

or run using `test.bat` on windows or `test` shell script on linux (or cygwin):

`t\test.bat`

`t/test`

_Note: use 'browser':'firefox|chrome|ie|edge(beta)' param to run on desired browser_

check and try lot more tests at [t/mws](../browse/t/mws)

##DEVEL

build own tests like those seen in [t/mws](../browse/t/mws)

expand existing modules found in [src/mws](../browse/src/mws)

add your own modules in [src/mws](../browse/src/mws)

and build more cool tests in [t/mws](../browse/t/mws)

check doc at [Selenium with Python](https://seleniumhq.github.io/selenium/docs/api/py/index.html)

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

