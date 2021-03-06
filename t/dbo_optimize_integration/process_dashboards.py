
import g
import mwsm as m
import mws.dashboards.g as d
import bc.g as bc

try:

    m.login()
    m.server('BVTEnv','Problems')
    m.logout()

    proc='DBO_Process'
    for i in range(1,3):
        print(str(i)+"==========")
        m.login()
        try:
            m.nav('ProcessDashboards')
        except:
            g.tc('','fail','process dashboards link may be missing')
            break
        try:
            d.load()
        except:
            g.tc('','fail','unable to load dashboard')
            break
        try:
            d.select_proc(proc)
        except:
            g.tc('','fail','unable to select in dropdown: '+proc)
            break
        d.select_range('1 hour')

        d.select_proc(proc)
        d.select_range('1 week')

        if i%2:
            #nav via si link
            d.navtab('Stage Instances')
            d.viewallsi()
            pid = d.clicksi()
        else:
            #nav via pi link
            d.navtab('Process Instances')
            pid = d.clickpi()
        bc.focus()
        bc.validatepi(pid)
        bc.validatestages(['Start Service Task 1 to End EG 1 Task 4',
            'Start Service Task 1 to End EG 2 Task 3',
            'Start Service Task 1 to End EG 3 Task 2' ])
        bc.close()
        #d.load()
        m.logout()

except:
    g.error()
finally:
    g.clean()

