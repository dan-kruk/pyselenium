from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as cpb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, sys, traceback, json

from src import res #mws page resources, links etc

#boilerplate globs
driver = wait = wait3 = ret = FF = env = None

#cfg defaults all almost
cfg = {
    'url':'http://usvardvmden141:8585',
    'browser':'firefox',
    'version':None,
    'capabilities':{'requireWindowFocus' : 'true','InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS' : 'true'},
    'remote':True,
    'hub':'http://127.0.0.1:4444/wd/hub',
    'wait':10
}

def loadenv(p, d={}): #grab json'ish env var
    global env
    v = os.environ.get(p); print ('*env:',p,'=',v)
    if v is None: return d 
    env = json.loads(v)
    return env

cfg = dict(cfg, **loadenv('cfg')) #merge env over defaults
for i in ['browser']: cfg[i] = cfg[i].lower() #normilize

def error ():
    global ret; ret = 1
    traceback.print_exc(file=sys.stdout)
    #exc_type, exc_value, exc_traceback = sys.exc_info(); print (exc_value)
    if driver is not None: driver.save_screenshot('./screenshot.png')

def prep ():
    global driver, wait, wait3, FF #globs
    if driver is not None: driver.quit(); driver = None #reenter
    print ('*cfg"',cfg)
    capabilities = {'ie':cpb.INTERNETEXPLORER,'firefox':cpb.FIREFOX,'chrome':cpb.CHROME} [cfg['browser']]
    capabilities.update(cfg['capabilities'])
    #hub or local driver
    if cfg.get('remote'): print ('*capabilities:',capabilities); driver = wd.Remote(cfg['hub'], capabilities)
    else: driver = {'firefox':wd.Firefox,'chrome':wd.Chrome,'ie': wd.Ie} [cfg['browser']] ()

    FF = True if cfg['browser'] == 'firefox' else False

    driver.maximize_window(); #max for inclusive screenshots
    wait = WebDriverWait(driver, int(cfg['wait']))
    wait3 = WebDriverWait(driver, 3)

def clean ():
    if driver is not None: driver.quit()
    sys.exit(ret)

def login ():
    if driver is None: prep()
    driver.get(cfg['url'])
    driver.find_element_by_name('username').send_keys('Administrator' + Keys.RETURN)
    driver.find_element_by_name('password').send_keys('manage' + Keys.RETURN)
    x="//*/a[contains (@title, 'Logout')]"; wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def nav(link=''): #mapped res.links or "link"
    driver.get(cfg['url']+'/'+res.links.get(link,link))

def logout ():
    x="//*/a[contains (@title, 'Logout')]"; wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    wait.until(EC.element_to_be_clickable((By.NAME, 'username')))

