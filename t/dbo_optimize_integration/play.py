
import g
import mwsm as ui
import mws.processanalytics as pa

from time import sleep

"""
Process analytics experimentation
"""

try:

    ui.navauth('ProcessAnalytics')
    pa.selectprocess('complex')
    #pa.selectrange('4 Weeks')
    #pa.selectvolume('All')

    zoom=8                 #diagram shrink factor
    g.focus_iframe() #jump to diagram

    pa.zoomprocdiag(-zoom) #shrink diagram
    steps=pa.findsteps()     #find steps or list steps:
    pa.zoomprocdiag(zoom) #shrink diagram

    #steps=['Verify Info','Send Notice']

    for x in range(2):
        g.tc('==round '+str(x))
        pa.zoomprocdiag(-zoom) #shrink diagram
        for step in steps:
            pa.navstep(step)
            g.focus()
            pa.selectvolumes({'level':'step','range':'prev','status':'Completed'})
            pa.selectvolumes({'level':'step','range':'curr','status':'All'})
            #sleep(2)
            g.focus_iframe() #jump to diagram
        steps.reverse()     #steps in backward order just for fun
        sleep(2)
        pa.zoomprocdiag(zoom) #blowup diagram just for fun

except:
    g.error()
finally:
    g.clean()

