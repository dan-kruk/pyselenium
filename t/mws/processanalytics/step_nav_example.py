
import g
import mwsm as ui
import mws.processanalytics as pa

from time import sleep

"""
example navigate step on process diagram and select a volume for it
"""

try:

    #get there
    ui.navauth('ProcessAnalytics')
    pa.selectprocess('complex')
    pa.selectrange('4 Weeks')
    pa.selectvolume('All')

    #nav through the step
    g.focus_iframe() #jump to diagram
    pa.zoomprocdiag(-8) #shrink diagram
    pa.navstep('Verify Info') #click on step
    sleep(4) #mutations on volume section
    g.focus_main() #back to main page from iframe
    pa.selectvolumes({'level':'step','range':'curr','status':'All'}) #select volume for step

    #optional
    g.focus_iframe() #jump to diagram
    pa.zoomprocdiag(0) #back to 1:1 zoom

except:
    g.error()
finally:
    g.clean()

