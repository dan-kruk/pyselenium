
import g #globs: driver, wait, wait2, FF, ...
from g import tc
from time import sleep

EC=g.EC; By=g.By; Keys=g.Keys; Alert=g.Alert; Select=g.Select #selenium statics

"""
Process Dashboards UI fundamentals
"""

#locates 1 (visible) out if 3 tab panels (2 others are hidden)
TP="//div[@class='x-container ema-ws-container \
x-tabpanel-child x-container-default x-border-layout-ct']//"

def load():
    """
    opening dashboard initially is tricky
    """
    g.focus_iframe()
    tc('wait for frame tabs loaded')
    g.wait20.until(EC.element_to_be_clickable((By.XPATH, #tap mid tab
        "//a[.='Stage Instances']" ))).send_keys(Keys.RETURN)
    tc('wait for frame content loaded')
    g.wait60.until(EC.element_to_be_clickable((By.XPATH,
        TP+"select[@id='processSelectList']")))

def select_proc (name):
    """
    select process in dropdown
    ret Select obj
    """
    tc('select proc '+name)
    s=Select (g.wait.until(EC.element_to_be_clickable((By.XPATH,
        TP+"select[@id='processSelectList']"))))
    s.select_by_visible_text(name)
    return s

def navtab (t='Overview'):
    """
    nav tab: Overview|Stage Instances|Process Instances
    """
    tc('nav tab '+t)
    g.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.='"+t+"']" )))\
            .send_keys(Keys.RETURN)

def select_range (r,start='',end=''):
    """
    select range: Today|1 hour|1 day|1 week|4 weeks|Custom
    start/end like 01/30/2017 08:41 am - applies for Custom
    """
    tc('select range '+r)
    print (TP+"a[.='"+r+"']")
    #TODO - click does not popup the panel
    g.wait.until(EC.element_to_be_clickable((By.XPATH, TP+"a[.='"+r+"']")))\
            .click()
    if r == 'Custom':
        sleep(1)
        #input start/end
        #//*[@id='iboCustomStartTime']
        #//*[@id='iboCustomEndTime']
        g.wait.until(EC.element_to_be_clickable((By.XPATH,\
"//div[contains(@class,'ui-dialog') and contains(@style,'display: block')]//span[.='OK']"))).click()

