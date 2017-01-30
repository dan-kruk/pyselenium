
import g
import mwsm as m
import mws.dashboards.g as d
from time import sleep

try:

    m.navauth('ProcessDashboards')
    g.focus_iframe()
    d.select_proc('complex')
    sleep(7)

except:
    g.error()
finally:
    pass
    g.clean()

