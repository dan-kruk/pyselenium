
import g
import mwsm as ui
import mws.processanalytics as pa
import bc.g as bc

"""
navigate from PA to BC via process or step on process diagram
"""

try:

    proc='DBM_Process'

    #nav through the process
    ui.navauth('ProcessAnalytics')
    pa.selectprocess(proc)
    pa.selectrange('4 Weeks')
    pa.selectvolumes({'level':'proc','range':'curr','status':'Completed'})
    pi = pa.piidlink(proc)
    bc.focus()
    #TODO validate things on BC
    bc.close()

    #nav through the step
    g.focus_iframe() #jump to diagram
    pa.zoomprocdiag(-8) #shrink diagram
    pa.navstep('Verify .....') #click on step
    g.focus() #back to main page from iframe
    sleep(4) #mutations on volume section
    pa.selectvolumes({'level':'step','range':'curr','status':'All'})
    pa.piidlink(proc)
    bc.focus()
    #TODO validate things on BC
    bc.close()

except:
    g.error()
finally:
    g.clean()

