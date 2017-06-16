
import g
import mwsm as ui
import mws.problems as p
import mws.problemdetail as pd
import mws.kpiinstdetail as kd
import bc.g as bc

"""
navigate from Problem and kpi instance detail to BC via process instance links
validate counts in Errors section in BC
"""

try:

    proc='DBO_Process'

    ui.navauth('Problems')
    ui.search('dbo')
    rules=['DBO_Process- Absolute Step Timeout Process','DBO_Process- Step Timeout Process','DBO order_amount by customer (KPI)']
    errors=[{'Proc':'3','Step':'0','Stage':'3','Rule':'3'},{'Proc':'0','Step':'1','Stage':'3','Rule':'1'},{'Proc':'0','Step':'0','Stage':'3','Rule':'1'}]

    for r in range(0,len(rules)):
        p.descriptionlinkname(rules[r])
        pid = pd.piidlink(r)
        bc.focus()
        bc.validatepi(pid)
        try:
            bc.validateerrors(errors[r])
        except:
            g.tc('','fail')
        bc.close(False)
        pd.kpidetail()
        kd.viewdata()
        try:
            pid = pd.piidlink(r)
        except:
            g.tc('','fail')
            ui.close(); ui.close() #restore nav
            continue
        bc.focus()
        bc.validatepi(pid)
        bc.close(False)
        ui.close()
        ui.close()

except:
    g.error()
finally:
    g.clean()

