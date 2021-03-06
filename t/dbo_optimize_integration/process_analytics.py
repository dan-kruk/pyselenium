
import g
import mwsm as ui
import mws.processanalytics as pa
import bc.g as bc

"""
navigate from PA to BC via process or step on process diagram
"""

try:

    proc='DBO_Process'

    for r in range(1):
        #print ('====='+str(r)+'======')
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
        #bc.validateerrors({'Proc':'3','Step':'0','Stage':'3','Rule':'3'})
        bc.close()

        #pa.selectvolumes({'level':'proc','range':'curr','status':'All'})
        #pid = pa.piidlink('5')
        #bc.focus()
        #bc.validatepi(pid)
        #bc.validateerrors({'Proc':'0','Step':'1','Stage':'3','Rule':'1'})
        #bc.close()


        #nav through magglass
        pa.selectvolumes({'level':'proc','range':'curr','status':'All'})
        pid = pa.piidlink('0', False) #make sure re-read latest inst, no click
        pi = pa.magglass()
        bc.focus()
        bc.validatepi(pid)
        bc.close()

        #nav through the step
        g.focus_iframe() #jump to diagram
        #pa.zoomprocdiag(-8) #shrink diagram
        pa.navstep('Service Task 1') #click on step
        g.focus_main() #back to main page from iframe
        pa.selectvolumes({'level':'step','range':'curr','status':'All'})
        pid = pa.piidlink('2') #3nd link
        bc.focus()
        bc.validatepi(pid)
        bc.close()

        #check mag glass link nav is disabled for step
        g.focus_iframe() #jump to diagram
        #pa.zoomprocdiag(-8) #shrink diagram
        pa.navstep('Service Task 1') #click on step
        g.focus_main() #back to main page from iframe
        pa.selectvolumes({'level':'step','range':'curr','status':'All'})
        pa.magglasscheck('0',False)

except:
    g.error()
finally:
    g.clean()

