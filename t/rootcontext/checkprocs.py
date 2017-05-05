
from g import error,clean,loadenv
import mwsm
from mws.cluster import chroot
from mws.busproc import searchcnt

try:

    cnt=loadenv('checkprocs',{'cnt':5})['cnt']

    mwsm.navauth("BusinessProcesses")
    for i in range(0,1):

        try:
            mwsm.server('BAM only') #workaround for IS errors seen in BPM mode
        except:
            mwsm.server('BAM only') #retry occasional 404

        searchcnt(cnt) #user dkrukov can see 5 procs
        #mwsm.server('BPM and BAM')
except:
    error()
finally:
    clean()

