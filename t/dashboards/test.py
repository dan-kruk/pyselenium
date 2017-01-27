
from g import tc,error,clean
from mwsm import navauth
import mws.dashboards.g as d
#from time import sleep

try:

    navauth('ProcessDashboards')
    d.focus()
    d.select_proc('complex')
    #sleep(5)

except:
    error()
finally:
    pass
    clean()

