
import g
import mwsm as ui
import mws.processanalytics as pa
import bc.g as bc

from time import sleep

"""
navigate from PA to BC via process or step on process diagram
"""

try:

    proc='DBM_Process'

    #get there
    ui.navauth('ProcessAnalytics')
    ui.nav('ProcessAnalytics')
    pa.selectprocess(proc)
    pa.selectrange('4 Weeks')

    ##nav through the process
    pa.selectvolumes({'level':'proc','range':'curr','status':'All'})
    pa.magglasscheck()
    pid = pa.piidlink()
    bc.focus()
    bc.validatepi(pid)
    bc.close()

    #nav through magglass
    pa.selectvolumes({'level':'proc','range':'curr','status':'All'})
    pi = pa.magglass()
    bc.focus()
    bc.validatepi(pid)
    bc.close()

    #nav through the step
    g.focus_iframe() #jump to diagram
    pa.zoomprocdiag(-8) #shrink diagram
    pa.navstep('Service Task 1') #click on step
    g.focus_main() #back to main page from iframe
    sleep(4) #mutations on volume section
    pa.selectvolumes({'level':'step','range':'curr','status':'All'})
    pa.piidlink()
    bc.focus()
    bc.validatepi(pid)
    bc.close()

    #check mag glass link nav is disabled for step
    g.focus_iframe() #jump to diagram
    pa.zoomprocdiag(-8) #shrink diagram
    pa.navstep('Service Task 1') #click on step
    g.focus_main() #back to main page from iframe
    sleep(4) #mutations on volume section
    pa.selectvolumes({'level':'step','range':'curr','status':'All'})
    pa.magglasscheck('0',False)

except:
    g.error()
finally:
    g.clean()

