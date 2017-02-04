
from g import error,clean,loadenv
from mwsm import navauth
import mws.ccs as ccs

try:

    x = loadenv('ccs', {'name':'BVTEnv'})

    navauth('DefineEnvironments')
    ccs.navenv(x)
    ccs.navtab('Configure Servers')
    ccs.navconfig('Station Settings')
    ccs.station_settings(x)
    ccs.validate()
    ccs.finish(x)
    ccs.deploy(x,'Deploy Updates')

except:
    error()
finally:
    clean()

