
import g
import mwsm as ui
import mws.processanalytics as pa
import bc.g as bc

from time import sleep

"""
navigate from PA to BC via process or step on process diagram
"""

try:

    ui.navauth('ProcessAnalytics')

    for n in range(10):
        for r in ['1 Week','4 Weeks']:
            for p in ['complex','DBO_Process']:
                print ('===== '+str(n)+' '+str(r)+' '+str(p)+' ======')
                pa.selectprocess(p)
                pa.selectrange(r)
                pa.selectvolumes({'level':'proc','range':'curr','status':'All'})
                pa.magglasscheck()

except:
    g.error()
finally:
    g.clean()

