
import g
from g import error,clean,loadenv
from mwsm import nav,navauth
from mws.cluster import chroot
from sketch.ccs import navenv,modmwspath,validate,finish,deploy

try:

    x = loadenv('ccs',

        {'name':'BVTEnv',
         'mapendpoints':{'mwspath':'alta'}
        }
    )

    navauth('DefineEnvironments')
    #navenv(x)
    #modmwspath(x)
    #validate()
    #finish(x)
    #deploy(x,'Deploy Updates')
    nav("ClusterSettings")
    chroot(x['mapendpoints']['mwspath'])

except:
    error()
finally:
    clean()

