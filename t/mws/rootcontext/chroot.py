
import g
from mwsm import navauth
from mws.cluster import chroot
import mws.ccs as c

try:

    x = g.loadenv('ccs',

        {'name':'BVTEnv',
         'mapendpoints':{'mwspath':'alta'}
        }
    )

    navauth('DefineEnvironments')
    c.navenv(x)
    c.modmwspath(x)
    c.validate()
    c.finish(x)
    c.deploy(x,'Deploy Updates')
    c.nav("ClusterSettings")
    chroot(x['mapendpoints']['mwspath'])

except:
    g.error()
finally:
    g.clean()

