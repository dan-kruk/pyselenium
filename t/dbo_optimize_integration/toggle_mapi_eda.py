
import g
import mwsm as m
import mws.ccs as c

try:

    x = g.loadenv('ccs', {'name':'BVTEnv'
        ,'mapi_eda':'eda'
        })

    m.navauth('DefineEnvironments')
    c.navenv(x)
    c.navtab('Configure Servers')
    c.navconfig('Process Tracker Settings')
    c.pt_settings(x)
    c.validate()
    c.finish(x)
    c.deploy(x,'Deploy Updates')

except:
    g.error()
finally:
    g.clean()

