
from g import error,clean,loadenv,tc
from mwsm import navauth
import mws.ccs as c

try:

    op = loadenv('op',{'what':'export import deploy','rel':'910'})
    env={'name':'BVTEnv','#migrate':True}

    navauth('DefineEnvironments')

    for r in range(0,1):
        for what in op.get('what').split():
            if what == 'export':
                c.navenv(env, False)
                env['file'] = c.exportenv(env['name'],op['rel'])
                #print (env['file'])
            elif what == 'import':
                before = c.envnames()
                c.importenv(env)
                name = None
                for k in c.envnames().keys():
                    if k not in before:
                        env['name'] = k
            elif what == 'deploy':
                c.navenv(env)
                #TODO - validate misc settings in CCS
                c.navtab('Configure Servers')
                c.navconfig('Station Settings')
                #c.station_settings(x)
                c.validate()
                c.finish(env)
                c.deploy(env)
            else:
                raise Exception('fail test param check')

except:
    error()
finally:
    clean()

