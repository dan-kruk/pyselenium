
from g import error,clean,loadenv
from mwsm import login,nav,logout
from mws.cluster import chroot
from mws.busproc import searchcnt

try:

    cnt=loadenv('checkprocs',{'cnt':5})['cnt']

    login()
    nav("BusinessProcesses")
    searchcnt(cnt) #user dkrukov can see 5 procs
    logout()
except:
    error()
finally:
    clean()

