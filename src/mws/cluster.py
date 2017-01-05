import g #globs: driver, wait, wait3, g.FF, ...
EC=g.EC; By=g.By; Keys=g.Keys #selenium statics
from g import tc

from time import sleep
import re

"""
mws cluster settings
"""

def chroot (d='alt',feurl=False):
    """
    create/update/clear mws cluster root context and optionally front end url; d='' - clears context
    """
    tc('change mwsroot to '+d)
    x=".//*[contains (@id, 'clusteredSetupPanel')]"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x))); e.click()
    sleep(1) #dom mutations TODO fix
    x=".//*[contains (@id, 'clusterRootcontext')]"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    e.clear(); e.send_keys(d)
    if feurl: chfeurl(d)
    tc('submit and check changes')        
    x=".//*[contains (@id, 'submitButton')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    x=".//*[text()='Changes to Cluster Node roles or ports are only effective after the Node restart']"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    x=".//*[contains (@id, 'standaloneSetupPanel')]"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x))); e.click()
    sleep(1) #dom mutations TODO fix

def chfeurl(d):
    """
    change front end url
    normally don't do it unless you bounce mws right after that or UI may end up inaccessible
    """
    x=".//*[contains (@id, 'clusteredFEURL')]"; e1=g.driver.find_element(By.XPATH, x)
    fe=re.search('(.*)(//)([^/]*)(/)?(.*)', e1.get_attribute('value')).groups() #decompose url
    tc('change feurl from '+e1.get_attribute('value'))
    if len(fe) > 3:
        if d: d='/'+d 
        fe=''.join(fe[0:3])+d #compose url
        tc('change feurl to '+fe)
        e1.clear(); e1.send_keys(fe)

