
import g
import mwsm as m
import mws.dashboards.g as d
from time import sleep

try:
    m.navauth('ProcessDashboards')
    d.load()
    for p in ['complex','brancher_stages_validation']:
        d.select_proc(p)
        for t in ['Overview','Stage Instances','Process Instances']:
            d.navtab(t)
            for r in ['Today','1 hour','Custom']:
                d.select_range(r)
                sleep(3)
except:
    g.error()
finally:
    pass
    g.clean()

