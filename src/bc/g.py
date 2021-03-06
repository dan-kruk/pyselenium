import g
from g import tc
from selenium.webdriver.support.ui import WebDriverWait
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

def validateerrors(counts={}):
    """
    validate counts in Errors section @counts={'Proc|Step|Stage|Rule':'count'}
    count can be fuzzy - just a list of numbers
    """
    tc('validate error counts')
    for k,v in counts.items():
        tc(k+' = '+v)
        try:
            e = g.driver.find_element(By.XPATH, ".//div[@data-target='#"+k+"AlarmsMenu']/span")
            val = e.text #read text once, saw inconsistency on later access
            if val not in v:
                tc('','fail','incorrect count for: '+k+' expected/actual: |'+v+'/'+val+'|')
        except:
            tc('','fail','missing element: '+k)

def configure(c={}):
    """
    configs @/business.console#admin/
    """
    tc('configure bc')
    save = g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//button[@id='bc-admin-save-button' and text()='Save']")))
    for k,v in c.items():
        tc(k+' = '+v)
        e = g.driver.find_element(By.ID, k)
        e.clear()
        e.send_keys(v)
    tc('save config')
    save.click() #send_keys not working - UI bug
    g.wait.until(EC.presence_of_element_located((By.XPATH,
        "//*[text()='REST Invocation Success' or text()='Success']")))

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

def navapp(name):
    """
    navigate app spaces menu item @name
    """
    tc('nav app space menu -> '+name)
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//li[contains(@data-hint,'AppSpace')]/div[@class='inline ng-binding']"))).click()
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        ".//li[@class='dropdown cp hint--right ng-scope open']//a[@role='menuitem' and text()='"+name+"']"))).click()

def navheadermenu(name):
    """
    navigate header menu item @name
    """
    tc('nav header menu -> '+name)
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//a[contains(@id,'"+name+"')]"))).click()

def spinwheel(timeout=20):
    """block on progress bar (aka spinning wheel) up to @timeout
    """
    spins = False
    xp = "//img[contains(@class,'case-loader-img') and not (contains(@class,'ng-hide'))]"
    try:
        tc('spin wheel probe')
        e=g.wait3.until(EC.element_to_be_clickable((By.XPATH,xp)))
        tc('spin wheel spins'); spins =True
    except:
        tc('spin wheel not seen')
    if spins:
        e=WebDriverWait(g.driver, timeout).until_not(EC.element_to_be_clickable((By.XPATH,xp)))


