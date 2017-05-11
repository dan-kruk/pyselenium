import g
from g import tc
import mwsm as m
import mws.search as s
from time import sleep

"""check for caf errors on business processes page after each server selection
    with and w/o search executed
    TODO: add check for >0 process count in process table/list
"""

try:

    proc='DBO_Process'
    m.navauth('BusinessProcesses')
    for server in ['BPM and BAM', 'BPM only', 'BAM only','BVTEnv']:
        m.server(server)
        sleep(1) #slight wait for error
        e = m.caf_error() #any caf errors after server select?
        if len(e) > 0:
            tc('','fail')
        s.search(proc)
        e = m.caf_error() #any caf errors after search?
        if len(e) > 0:
            tc('','fail')

except:
    g.error()
finally:
    g.clean()

