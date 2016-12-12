##NAME

**pyselenium** - get all UI test done

../
pyselenium/
| src/
| t/
| demo
| hub
| readme.md
| install_pyse_rh

##SETUP

```sh 
git clone http://irepo.eur.ad.sag/scm/~dkrukov/pyselenium.git && cd pyselenium
export $PYTHONPATH=src PATH=:$PATH
```
install python:		https://www.python.org/downloads

install selenium:	python -m pip install selenium

install on rh linux, may use: `install_pyse_rh`

start: `hub`

##SYNOPSYS

run: `demo`

##USAGE

using `demo` runner try any tests found in t/...

build own tests like those seen in t/...

expand existing modules found in src/...

add your own modules in src/...

