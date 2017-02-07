import g
import mwsm as m
import mws.search as s
import mws.busproc as p

try:

    proc='DBM_Process'
    m.navauth('BusinessProcesses')
    s.search(proc)
    #test both enable and disable
    for s in [True,False,True]:
        p.toggleexecution(proc, s)
        p.checkexecution(proc, s)
        p.toggleanalysis(proc, s)
        p.checkanalysis(proc, s)

except:
    g.error()
finally:
    g.clean()

