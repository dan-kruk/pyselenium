import g
from g import tc
EC=g.EC; By=g.By
from selenium.common.exceptions import StaleElementReferenceException as stale
from time import sleep

def searchcnt(cnt=0,text=None):
    """validate count of processes, search text first, optional"""
    if text:
        tc('search '+text)
        x="//*[contains (@name,'keywordsTextInput')]";
        g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(text)
        x="//*[contains (@name,'asyncSimpleSearchGoButton')]"
        g.driver.find_element(By.XPATH, x).click()
    tc('check proc cnt in list')
    x="//*[contains(@id,'dataTotal__primary')]"
    sleep(.1)
    try:
        e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
        a=e.text.split() #paged table cnt str
    except stale:
        tc('stale elem retry')
        sleep(1)
        tc('check proc cnt in list')
        e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
        a=e.text.split()
    if len(a) == 1: c=0 #Empty
    elif len(a) == 3: c=int(a[2]) #N of M
    elif len(a) == 5: c=int(a[4]) #N - M of X
    tc('act/exp proc list '+str(c)+' '+str(cnt))
    if cnt != c: tc('','fail')