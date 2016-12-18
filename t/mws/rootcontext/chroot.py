
import g
from g import error,clean,loadenv
from mwsm import login,nav,logout
from mws.cluster import chroot
from sketch.ccs import navenv,modmwspath,validate,finish,deploy

try:

    x = loadenv('ccs',

        {'name':'BVTEnv',
         'mapendpoints':{'mwspath':'alta'}
        }
    )

    login()
    nav('DefineEnvironments')
    navenv(x)
    modmwspath(x)
    validate()
    finish(x)
    deploy(x,'Deploy Updates')
    nav("ClusterSettings")
    chroot(x['mapendpoints']['mwspath'])
    logout()

except:
    error()
finally:
    clean()

