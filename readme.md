
##NAME

**pyselenium** - productive UI testing

##SETUP

---

setup on Windows:

install [python 3.5+](https://www.python.org/downloads)

install selenium module using command:
`python -m pip install selenium`

prepend system env `PATH` variable with the following:

`%HOMEDRIVE%%HOMEPATH%\AppData\Local\Programs\Python\Python36-32\Scripts\;%HOMEDRIVE%%HOMEPATH%\AppData\Local\Programs\Python\Python36-32\;c:\cygwin64\bin;`

add `PYTHONPATH=src` system env variable

---

Great way of complete setup on windows:

download cygwin:
http://cygwin.com/setup-x86_64.exe

run command in dos cmd window:
setup-x86_64.exe -q -P nc,wget,vim,git,subversion,openssh,python3

prefix windows system PATH with:
c:\cygwin64\bin;

run commands in cygwin terminal:

cd; wget http://irepo.eur.ad.sag/users/dkrukov/repos/pyselenium/raw/install_pyse_cygwin
chmod 755 install_pyse_cygwin
./install_pyse_cygwin

---

setup on RH/Centos linux:

cd; wget http://irepo.eur.ad.sag/users/dkrukov/repos/pyselenium/raw/install_pyse_rh
chmod 755 install_pyse_rh
./install_pyse_rh

---

install ie, firefox, chrome, edge browsers on your remote node machines as needed

You may also install all or needed browsers on your laptop for local testing

install browser drivers local or remote and start selenium hub if needed:

wget http://irepo.eur.ad.sag/users/dkrukov/repos/pyselenium/raw/hub && chmod 755 hub

`hub install`

`hub`		#hub and node

`hub hub`	#just hub

`hub node`	#just node which points to local hub

`hub node host:port`	#just node, which points remote host:port hub

_Note: the above hub/node cmd enters selenium service mode after installing drivers. So term it if remote test execution on a hub is not needed_

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

