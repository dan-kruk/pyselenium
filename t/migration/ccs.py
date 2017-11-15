
from g import error,clean,loadenv,tc
from mwsm import navauth
import mws.ccs as c

try:

    env = loadenv('env',
            {'what':'[export import deploy]','rel':'910','name':'BVTEnv',
                'exp_dir':'//rdvmva91/Downloads','migrate':True
            })

    navauth('DefineEnvironments')

    for r in range(0,1):
        for what in env.get('what'):
            if what == 'export':
                c.navenv(env, False)
                env['file'] = c.exportenv(env)
                print (env['file'])
            elif what == 'import':
                before = c.envnames()
                env['file'] = env['exp_dir']+'/ExportedEnvironments'+env['rel']+'.xml'
                #env['file'] = 'c:\\Users\\Administrator\\Downloads\\ExportedEnvironments96.xml'
                c.importenv(env)
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

