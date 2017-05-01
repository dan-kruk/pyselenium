
import g #globs: driver, wait...
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys; Select=g.Select #selenium statics

def piidlink(i=0):
    """click on i-th pid link in table, ret: link pid
        may be used on a few other pages as well
    """
    tc('click on '+str(i)+' pid link in a table')
    x = "//a[contains (@href,':viewBusinessConsoleLink')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH,x)))
    l = g.driver.find_elements_by_xpath(x)
    t = l[i].text
    l[i].click()
    return t

def kpidetail():
    """click kpi detail magglass link
    """
    x = "//a[contains (@href,':viewMonitor')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        x))).send_keys(Keys.RETURN)


