
import g
import mwsm as ui
import mws.problems as p
import mws.problemdetail as pd
import mws.kpiinstdetail as kd
import bc.g as bc

"""
navigate from Problem and kpi instance detail data to BC via process instance links
validate counts in Errors section in BC
validate problem contrib event and KPI inst detail event counts (OBE-9469)
some counts are fuzzy, e.g. for rules as seen as such in Optimize
"""

try:

    proc='DBO_Process'

    ui.navauth('Problems')
    rules=['DBO_Process- Absolute Step Timeout Process','DBO_Process- Step Timeout Process','DBO order_amount by customer (KPI) pubDocDBO/customer.pubDocDBO/customer.borotuga']
    errors=[{'Proc':'3','Step':'0','Stage':'3','Rule':'3 5'},{'Proc':'0 1','Step':'1','Stage':'3','Rule':'1 2 3'},{'Proc':'0 1','Step':'0','Stage':'3','Rule':'2'}]

    for r in range(0,len(rules)):
        ui.search('"'+rules[r]+'"') #search quoted(exact in mws)
        try:
            p.descriptionlinkname(rules[r])
        except:
            g.tc('','fail','unable to see/click rule link: '+rules[r])
            continue

        pid, cnt = pd.piidlink()
        if pid == None: continue #no link seen

        g.tc('validate contrib event inst count (OBE-9469)')
        if cnt > 3:
            g.tc('','fail', 'expected/actual <4/'+str(cnt))

        bc.focus()
        bc.validatepi(pid)
        bc.validateerrors(errors[r])
        bc.close(False)
        pd.kpidetail()
        kd.viewdata()

        pid, cnt = pd.piidlink()
        if pid == None:
            ui.close(); ui.close() #restore nav
            continue
        g.tc('validate KPI inst detail event inst count (OBE-9469)')
        if cnt > 3:
            g.tc('','fail', 'expected/actual <4/'+str(cnt))

        bc.focus()
        bc.validatepi(pid)
        bc.close(False)
        ui.close()
        ui.close()

except:
    g.error()
finally:
    g.clean()

