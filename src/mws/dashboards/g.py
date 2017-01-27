
import g #globs: driver, wait, wait2, FF, ...
from g import tc

EC=g.EC; By=g.By; Keys=g.Keys; Alert=g.Alert; Select=g.Select #selenium statics

"""
Process Dashboards UI fundamentals
"""

def focus ():
    tc('focus on proc dashboard frame')
    g.driver.switch_to_frame(g.wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'iframe'))))

def select_proc (name):
    tc('select proc '+name)
    g.wait60.until(EC.element_to_be_clickable((By.ID, 'processSelectList'))).send_keys(name)

