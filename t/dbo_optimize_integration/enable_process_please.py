import g
import mwsm as m
import mws.search as s
import mws.busproc as p

#got very sick with buggy UI model enablement toggling puzzle
#this test does a "super pleasing beg" approach
#hopefully going from any state to definite enabled state
#amone analysis and execution enablement flags

try:

    proc='DBM_Process'
    m.navauth('BusinessProcesses')
    s.search(proc)

    if p.toggleexecution(proc):
        m.logout(); m.login(); s.search(proc)
        p.checkexecution(proc)

    if p.toggleanalysis(proc):
        m.logout(); m.login(); s.search(proc)
        p.checkanalysis(proc)

except:
    g.error()
finally:
    g.clean()

