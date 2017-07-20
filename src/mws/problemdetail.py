
import g #globs: driver, wait...
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys; Select=g.Select #selenium statics

def piidlink(i=0):
    """click on i-th pid link in table, ret: link pid, N of links in table
        may be used on a few other pages as well
    """
    tc('click on '+str(i)+' pid link in a table')
    x = "//a[contains (@href,':viewBusinessConsoleLink')]"
    t = None
    try:
        g.wait.until(EC.element_to_be_clickable((By.XPATH,x)))
    except:
        tc('','fail','no links found to click on')
        return t, 0
    l = g.driver.find_elements_by_xpath(x)
    if len(l) < i: #friendly cause
        tc('','fail','no link to click seen, expected/actual link count '+i+'/'+len(l))
    else:
        t = l[i].text
        l[i].click()
    return t, len(l)

def kpidetail():
    """click kpi detail magglass link
    """
    tc('click kpi detail magglass')
    x = "//a[contains (@href,':viewMonitor')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        x))).send_keys(Keys.RETURN)

