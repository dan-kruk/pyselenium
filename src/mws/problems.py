
import g #globs: driver, wait...
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys; Select=g.Select #selenium statics

def descriptionlink(i=0):
    """click on i-th problem desc link in problems table, ret: link descr
    """
    tc('click on '+str(i)+' problem in problems list')
    x = "//a[contains (@href,':viewDetail')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH,x)))
    l = g.driver.find_elements_by_xpath(x)
    t = l[i*2].text
    l[i*2].send_keys(Keys.RETURN) #every other link is magglass
    return t

def clicklink(x=0, y=0):
    """TODO click link row x, col y in problems table
    """
    yx = [ "//a[contains (@href,':viewDetail')]" ]

def descriptionlinkname(name):
    tc('click on '+name)
    g.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,name))).send_keys(Keys.RETURN)
