import g
from g import tc
#from time import sleep

EC=g.EC; By=g.By; Keys=g.Keys; AC=g.ActionChains

def focus():
    tc('focus on business console')
    g.wait20.until(EC.number_of_windows_to_be(2))
    g.focus(1) #bc is an alt tab-window
    g.wait60.until(EC.presence_of_element_located((By.XPATH,
        "//div[@id='stepSummaryTable']")))

def close(refresh=True):
    #sleep(5) #tmp so page seen on demo
    tc('close business console tab/window')
    g.driver.close() #close tab-window
    g.focus()
    refresh and g.driver.refresh() #it'd be stale overwise
    g.focus_main() #back to main window

def validatepi(pid):
    """
    validate instance details by pid
    """
    tc('located pid='+pid)
    g.wait20.until(EC.presence_of_element_located((By.XPATH,
        "//td[.='"+pid+"']")))

def configure(c={}):
    """
    configs @/business.console#admin/
    """
    tc('configure bc')
    save = g.wait.until(EC.element_to_be_clickable((By.ID,
        'bc-admin-save-button')))
    for k,v in c.items():
        tc(k+' = '+v)
        e = g.driver.find_element(By.ID, k)
        e.clear()
        e.send_keys(v)
    tc('save config')
    save.click() #send_keys not working - UI bug
    g.wait.until(EC.presence_of_element_located((By.XPATH,
        "//*[text()='REST Invocation Success']")))

def validatestages(ss=[]):
    """
    check handful of instances in stage section(table)
    """
    for s in ss:
        x = "//*[@class='gantt_tree_content' and text()='"+s+"']"
        tc('check stage '+s)
        e = g.wait.until(EC.presence_of_element_located((By.XPATH, x)))
        #on some browsers only
        if g.cfg['browser'] in 'chrome':
            tc(' check tooltip')
            AC(g.driver).move_to_element(e).click().perform()
            g.wait.until(EC.presence_of_element_located((By.XPATH,
                "//div[@class='gantt_tooltip']")))

