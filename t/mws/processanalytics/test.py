
from g import cfg,loadenv,prep,error,clean
from mwsm import login,nav,logout
from mws.processanalytics import selectprocess,selectrange,selectvolume,nav as pa_nav
from mws.procinstdetail import validateid as val_piinstdetail
#from mws.busconsole import validateid as val_pibusconsole
from time import sleep


try:

    #c = [] #cook sos mase dummy user data
    #for i in range(0,3):
    #    i=str(i)
    #    c.extend([{'name':'AAAp-'+i, 'desc':'pool'+i}])

	#x = loadenv('process')
	
	login()

	nav('ProcessAnalytics')
	selectprocess('OTC_Bus_Designer')
	selectrange('4 Weeks')
	selectvolume('All')
	pi=pa_nav()
	val_piinstdetail(pi)
	
	nav('ProcessAnalytics')
	selectprocess('complex')
	selectrange('4 Weeks')
	selectvolume('All')
	pi=pa_nav()
	val_piinstdetail(pi)

	nav('ProcessAnalytics')
	#selectprocess('ipe')
	#selectrange('4 Weeks')
	#selectvolume('All')
	#pi=pa_nav()
	#val_pibusconsole(pi)
	
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

