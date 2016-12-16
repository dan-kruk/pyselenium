
from g import cfg,loadenv,prep,error,clean
from mwsm import login,nav,logout
from mws.ccs import delpools,createpools
from mws.users import createusers,delusers
from mws.cluster import chroot

try:

    #c = [] #cook some dummy user data
    #for i in range(0,3):
    #    i=str(i)
    #    c.extend([{'name':'AAAp-'+i, 'desc':'pool'+i}])

    login()
    nav('DatabasePoolConfiguration')
    x = loadenv('db')
    print (x)
    delpools(x)
    createpools(x)
    logout()

    #login()
    #nav('Users')
    #c = loadenv('users')
    #delusers(c)
    #createusers(c)
    #logout()

    #login()
    #for r in range(0,2):
    #    for b,u in zip(['ie','chrome','firefox'],['rdvmva88','usvardvmden141','rdvmden53']):
    #        print (r,b,u)
    #        cfg['browser'] = b; cfg['url'] = 'http://'+u+':8585'
    #        prep()
    #        login()
    #        nav("ClusterSettings")
    #        chroot('/altroot44')
    #        chroot('')
    #        chroot()
    #        logout()

except:
    error()
finally:
    clean()

