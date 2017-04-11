import g
import mwsm as m
import mws.search as s
import mws.busproc as p

try:

    proc='DBO_Process'
    m.navauth('BusinessProcesses')
    s.search(proc)
    #test both enable and disable
    for i in [True,False,True]:
        #s.search(proc)
        p.toggleexecution(proc, i)
        #s.search(proc)
        p.checkexecution(proc, i)
        #s.search(proc)
        p.toggleanalysis(proc, i)
        #s.search(proc)
        p.checkanalysis(proc, i)

except:
    g.error()
finally:
    g.clean()

