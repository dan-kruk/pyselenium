
import g
import mwsm as ui
import mws.problems as p
import mws.problemdetail as pd
import mws.kpiinstdetail as kd
import bc.g as bc

"""
navigate from Problem and kpi instance detail to BC via process instance link
"""

try:

    proc='DBO_Process'

    ui.navauth('Problems')
    ui.search('dbo')
    for r in range(0,2):
        print ( p.descriptionlink(r) )
        pid = pd.piidlink(r)
        bc.focus()
        bc.validatepi(pid)
        bc.close(False)
        pd.kpidetail()
        kd.viewdata()
        pid = pd.piidlink(r)
        bc.focus()
        bc.validatepi(pid)
        bc.close(False)
        ui.close()
        ui.close()

except:
    g.error()
finally:
    g.clean()

