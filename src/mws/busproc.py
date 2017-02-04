import g
from g import tc
EC=g.EC; By=g.By
from selenium.common.exceptions import StaleElementReferenceException as stale
from time import sleep
from mwsm import overlay_handler
from mws.search import search


def searchcnt(cnt=0,text=''):
    """validate count of processes, search text first, optional"""
    search(text)
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

def nav(name):
    """navigate to process model"""
    tc('click process model '+name)
    x="//*/a[contains(@id,'_"+name+"') and contains(@id, 'htmlCommandLink')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()

def toggleexecution(p,s=True):
    """enable / disable execution for model"""
    tc('enable execution for model')
    x="//*/img[contains (@id, 'executionEnabledIcon') and contains (@id, '"+p+"')]"
    se=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    s0=se.get_attribute('src')
    if 'Icon_Configured.png' in s0:
        s0=True
    else:
        s0=False
    if s is not s0:
        tc('toggle execution enabled from '+str(s0)); se.click()
        overlay_handler(.5)

def toggleanalysis(p,s=True):
    """enable / disable analysis for model"""
    tc('enable analysis for model')
    x="//*/img[contains (@id, 'analysisEnabledIcon') and contains (@id, '"+p+"')]"
    se=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    s0=se.get_attribute('src')
    if 'Icon_Configured.png' in s0:
        s0=True
    else:
        s0=False
    if s is not s0:
        tc('toggle analysis enabled from '+str(s0)); se.click()
        overlay_handler(4)

def checkexecution(p,s=True):
    """validate execution flag"""
    tc('check execution flag for model')
    x="//*/img[contains (@id, 'executionEnabledIcon') and contains (@id, '"+p+"')]"
    se=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    s0=se.get_attribute('src')
    if 'Icon_Configured.png' in s0:
        s0=True
    else:
        s0=False
    assert s is s0

def checkanalysis(p,s=True):
    """validate analysis flag"""
    tc('check analysis flag for model')
    x="//*/img[contains (@id, 'analysisEnabledIcon') and contains (@id, '"+p+"')]"
    se=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    s0=se.get_attribute('src')
    #print(s0,'-----')'''
    if 'Icon_Configured.png' in s0:
        s0=True
    else:
        s0=False
    assert s is s0

