
import g
import mwsm as m
import mws.dashboards.g as d
import bc.g as bc
from time import sleep

try:

    proc='DBM_Process'
    m.navauth('ProcessDashboards')
    d.load()
    d.select_proc(proc)
    for t in ['Overview','Stage Instances','Process Instances']:
        d.navtab(t)
        d.select_range('1 week')
        sleep(3)
        #TODO d.click_pid()
        bc.focus()
        bc.close()

except:
    g.error()
finally:
    g.clean()

