
from g import cfg,loadenv,prep,error,clean
from mwsm import login,nav,navauth,logout
from mws.processanalytics import selectprocess,selectrange,selectvolume,nav as panav
from mws.procinstdetail import validateid as valpidetail
import bc.steps as bc
from mws.search import search
import mws.busproc as bp
import mws.editprocess as ep
from time import sleep


try:

    #c = [] #cook sos mase dummy user data
    #for i in range(0,3):
    #    i=str(i)
    #    c.extend([{'name':'AAAp-'+i, 'desc':'pool'+i}])

	#x = loadenv('process')
	
	x = {'execution':False,'analysis':False}
	#y = {'execution':True,'analysis':True}

	
	navauth('BusinessProcesses')
	search('DBM_Process')
	bp.nav('DBM_Process')
	ep.toggle_execution_analysis ()
	search('DBM_Process')
	bp.nav('DBM_Process')
	ep.check_execution_analysis ()
	
	'''search('DBM_Process')
	bp.nav('DBM_Process')
	ep.toggle_execution_analysis (x)
	search('DBM_Process')
	bp.nav('DBM_Process')
	ep.check_execution_analysis (x)

	search('DBM_Process')
	bp.nav('DBM_Process')
	ep.toggle_execution_analysis ()
	search('DBM_Process')
	bp.nav('DBM_Process')
	ep.check_execution_analysis ()'''
		
	#bp.toggleexecution()
	#bp.nav('DBM_Process')
	#ep.toggleanalysis()
	
	#navauth('BusinessProcesses')
	#search('DBM_Process')
	#bp.nav('DBM_Process')
	#ep.toggleexecution()
	#bp.nav('DBM_Process')
	#ep.toggleanalysis()
	
	#nav('ProcessAnalytics')
	#selectprocess('OTC_Bus_Designer')
	#selectrange('4 Weeks')
	#selectvolume('All')
	#pi=panav()
	#valpidetail(pi)
	
	#nav('ProcessAnalytics')
	#selectprocess('complex')
	#selectrange('4 Weeks')
	#selectvolume('All')
	#pi=panav()
	#valpidetail(pi)

	#nav('ProcessAnalytics')
	#selectprocess('DBM_Process')
	#selectrange('4 Weeks')
	#selectvolume('All')
	#pi=panav()
	#bc.check()
	
	#logout()

except:
    error()
finally:
    clean()

