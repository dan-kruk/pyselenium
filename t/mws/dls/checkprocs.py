
from g import error,clean,loadenv
import mwsm
from mws.cluster import chroot
from mws.busproc import searchcnt

try:

    cnt=loadenv('checkprocs',{'cnt':5})['cnt']

    mwsm.navauth("BusinessProcesses")
    mwsm.server('BAM only') #workaround for IS errors seen in BPM mode
    searchcnt(cnt) #user dkrukov can see 5 procs
except:
    error()
finally:
    clean()

