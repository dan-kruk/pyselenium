
from g import cfg,loadenv,prep,error,clean
from mwsm import login,nav,navauth,logout
from mws.processanalytics import selectprocess,selectrange,selectprocessvolume,processpiidlink,processmagglasslink,selectstepinmodel,selectstepvolume,steppiidlink,stepmagglasslink
from mws.procinstdetail import validateid as valpidetail
import bc.steps as bc
from mws.search import search
import mws.busproc as bp
import mws.editprocess as ep
import mws.overviewdashboard as od
import mws.stageinstancesdashboard as sid
import mws.processinstancesdashboard as pid
from time import sleep


try:

    #c = [] #cook sos mase dummy user data
    #for i in range(0,3):
    #    i=str(i)
    #    c.extend([{'name':'AAAp-'+i, 'desc':'pool'+i}])

	#x = loadenv('process')
	
	x = {'execution':False,'analysis':False}
	#y = {'execution':True,'analysis':True}

	
	'''navauth('BusinessProcesses')
	search('DBM_Process')
	bp.nav('DBM_Process')
	ep.toggle_execution_analysis ()
	search('DBM_Process')
	bp.nav('DBM_Process')
	ep.check_execution_analysis ()'''
	
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

	'''nav('ProcessAnalytics')'''
	#navauth('BusinessProcesses')
	#search('DBM_Process')
	#bp.toggleexecution('DBM_Process')
	#bp.checkexecution('DBM_Process')
	#bp.toggleanalysis('DBM_Process')
	#bp.checkanalysis('DBM_Process')
	'''navauth('ProcessAnalytics')
	selectprocess('DBM_Process')
	selectrange('4 Weeks')'''
	#selectprocessvolume('All')
	#processpiidlink()
	#processmagglasslink()
	'''selectstepinmodel()
	selectstepvolume('All')
	steppiidlink()'''
	#stepmagglasslink()
	#pi=processpiidlink()
	#bc.check()
	
	navauth('ProcessDashboards')
	sleep(60)
	od.selectprocess('DBM_Process')	
	od.selectinterval('4 weeks')
	sid.navsidashboard()
	pid.navpidashboard()
	pid.piidlink()
	
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
	#pi=processpiidlink()
	#valpidetail(pi)
	
	#nav('ProcessAnalytics')
	#selectprocess('complex')
	#selectrange('4 Weeks')
	#selectvolume('All')
	#pi=processpiidlink()
	#valpidetail(pi)

	#logout()

except:
    error()
finally:
    clean()

