
'''
this is my complete, real and very focused sprint feature test 
it sets mws root context, enables root context and saml/dls in AE, deploys CCS changes
as a bonus it then reverts all the root context changes and re-deploys CCS

run it as follows:

    export login="{ 'url':'http://<mwshost>:8585' }" #optional

    python t/mws/examples/feature.py

How it works as 1-2-3

  First:
    import navigation layer funcs below that are already implemented
    look at existing modules src/mws/**, they organized clean by main layers and areas of MWS UI
    if nothing fit the feature worked on, add new functions in relevant module
    or create new module if one needed is not created yet
    be super lazy - always reuse and do composition design
    avoid excess abstraction and OOP design by all means (mostly always)
'''

import g
from g import error,clean,loadenv
from mwsm import login,nav,navauth,logout
from mws.cluster import chroot
import sketch.ccs as ccs

try: #handle any rough errors

    '''
      Second:
        most tests need 1 or more primitive or complex params, so usually they'd be json snippets
        here loadenv() loads 'ccs' env var passing composite values, and takes defaults
        be sure to provide defaults making test easy to use and portable otb
    '''
    x = loadenv('ccs',

        {'name':'BVTEnv',
         'mapendpoints':{'mwspath':'alta'},
         'dls':True
        }
    )

    '''
      Third: just run your feature
              
    '''
    #run rootcontext feature tests
    login()
    nav('DefineEnvironments')
    ccs.navenv(x)
    ccs.modmwspath(x)
    ccs.navtab('Configure Servers')
    ccs.navconfig('Station Settings')
    ccs.toggledls(x.get('dls',True))
    ccs.validate()
    ccs.finish(x)
    ccs.deploy(x,'Deploy Updates')
    nav("ClusterSettings")
    chroot(x['mapendpoints']['mwspath'])
    logout()

    #reverse above dls/rootcontext changes
    x = {'name':'BVTEnv',
         'mapendpoints':{'mwspath':''},
         'dls':False
        }
    navauth('DefineEnvironments') #this does login and nav in 1 step
    ccs.navenv(x)
    ccs.modmwspath(x)
    ccs.navtab('Configure Servers')
    ccs.navconfig('Station Settings')
    ccs.toggledls(x.get('dls',True))
    ccs.validate()
    ccs.finish(x)
    ccs.deploy(x,'Deploy Updates')
    nav("ClusterSettings")
    chroot(x['mapendpoints']['mwspath'])

except:
    error()
finally:
    clean()

'''Gee, that's it
    an entire tough nut feature is covered w/o mess'''

