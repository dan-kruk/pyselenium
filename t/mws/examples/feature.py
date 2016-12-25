
'''
this is a complete sprint feature test 
it sets mws root context, enables root context and dls in ae, deploys changes

run it as follows:

    python t/mws/examples/feature.py


How it works as 1-2-3

  *First:
    import navigation layer funcs below that are already implemented
    look at existing modules src/mws/**, they organized clean by main layers and areas of MWS UI
    if nothing fit the feature worked on, add new functions in relevant module
    or create new module if one needed is not created yet
    be super lazy - always reuse and do composition design
    avoid excess abstraction and OOP design by all means (mostly always)
'''

import g
from g import error,clean,loadenv
from mwsm import login,nav,logout
from mws.cluster import chroot
from sketch.ccs import navenv,modmwspath,validate,finish,deploy

try: #handle any rough errors

    '''
      *Second:
        most tests need 1 or more primitive or complex params, so usually they'd be json snippets
        here loadenv() loads 'ccs' env var passing composite values, and takes defaults
        be sure to provide defaults making test easy to use and portable otb
    '''
    x = loadenv('ccs',

        {'name':'BVTEnv',
         'mapendpoints':{'mwspath':'alta'},
         'dls':'true'
        }
    )

    '''
      *Third: just run your feature
              
    '''

    login()
    nav('DefineEnvironments')
    navenv(x)
    modmwspath(x)
    navtab('Configure Servers')
    navconfig('Station Settings')
    toggledls(x.get('dls',True))
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

'''Gee, that's it'''


