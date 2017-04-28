
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
    tc('wait for frame tab stage instances loaded')
    e=g.wait20.until(EC.element_to_be_clickable((By.XPATH, #tap mid tab
        "//a[.='Stage Instances']" )))
    #sleep(15) #click on tab to soon may corrupt page
    e.send_keys(Keys.RETURN)
    tc('wait for frame content loaded')
    g.wait80.until(EC.element_to_be_clickable((By.XPATH,
        TP+"select[@id='processSelectList']")))
    #sleep(1) #click on tab to soon may corrupt page

def select_proc (name):
    """
    select process in dropdown
    ret Select obj
    """
    tc('select proc '+name)
    s=Select (g.wait.until(EC.element_to_be_clickable((By.XPATH,
        TP+"select[@id='processSelectList']"))))
    sleep(1)
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
    #print (TP+"a[.='"+r+"']")
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

def clickpi(ind='1'):
    """
    click on ind'th proc inst link in table; ret: pid
    """
    tc('click on pi link '+ind)
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//table[@id='processInstancesTable']//tr[@id='"+ind+"']/td[3]/a")))
    e.click()
    return e.text

def viewallsi():
    """
    click to view all stage inst
    """
    tc('select to view all stage instances')
    e=g.wait.until(EC.presence_of_element_located((By.XPATH,
        "//div[@class='iboDialogLoading']")))
    sleep(3)
    #g.wait.until(EC.staleness_of(e))
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//input[@id='cb_stageMetricsTable']")))
    e.click()
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//button[@id='smViewInstButton']"))).click()
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//table[@id='stageInstancesTable']//tr[@id='1']/td/a[contains\
                (@href, 'siRedirectMWSProcessInstanceDetail')]"))).click()

def clicksi(ind='1'):
    """
    click on ind'th stage inst link in table; ret: pid
    """
    tc('click on stage link '+ind)
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//table[@id='stageInstancesTable']//tr[@id='"+ind+"']//td[5]/a")))
    e.click()
    return e.text

