
import g
import mwsm as m
import bc.g as bc
import mws.processanalytics as pa
from time import sleep
Keys=g.Keys; EC=g.EC; driver=g.driver

try:

    m.navauth('ProcessAnalytics')
    m.nav('ProcessAnalytics') #no auth when refreshing page later

    for x in range(20):
        g.tc('===='+str(x)+'====')

        pa.selectprocess('DBM_Process')
        pa.selectrange('4 Weeks')
        pa.selectvolumes()

        pa.piidlink()
        bc.focus() #focus in bc
        #do bc tests here
        bc.close() #focus back on main

        pa.selectprocess('DBM_Process')
        pa.selectrange('4 Weeks')

        g.focus_iframe()
        pa.zoomprocdiag(-8)
        pa.navstep('Service Task 1')
        g.focus()
        sleep(4) #yellow mutation
        pa.selectvolumes({'level':'step','range':'curr','status':'Completed'})
        pa.piidlink()
        bc.focus() #focus in bc
        #do bc tests here
        bc.close() #focus back on main

        #g.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

except:
    g.error()
finally:
    g.clean()

