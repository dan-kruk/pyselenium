from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as cpb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import os, sys, time, traceback, json

#boilerplate globs
driver = wait = wait3 = FF = env = None
tcases = {}; tc_name = 'Begin'; tc_status = 'pass'; tc_time = time.time()
ret=0


#cfg defaults everything
cfg = {
    'url':'http://usvardvmden141:8585',
    'username':'Administrator',
    'password':'manage',
    'browser':'firefox',
    'version':None,
    'capabilities':{'requireWindowFocus':'true','InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS':'true'},
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

def prep():
    global driver, wait, wait3, FF #globs
    if driver is not None: driver.quit(); driver = None #reenter
    print ('*cfg"',cfg)
    capabilities = {'ie':cpb.INTERNETEXPLORER,'firefox':cpb.FIREFOX,'chrome':cpb.CHROME} [cfg['browser']]
    capabilities.update(cfg['capabilities'])
    #hub or local driver
    tc('init '+cfg['browser'])
    if cfg.get('remote'): print ('*capabilities:',capabilities); driver = wd.Remote(cfg['hub'], capabilities)
    else: driver = {'firefox':wd.Firefox,'chrome':wd.Chrome,'ie': wd.Ie} [cfg['browser']] ()

    FF = True if cfg['browser'] == 'firefox' else False

    tc('maximize '+cfg['browser'])
    driver.maximize_window(); #max for inclusive screenshots
    wait = WebDriverWait(driver, int(cfg['wait']))
    wait3 = WebDriverWait(driver, 3)

def tc(tc='',s='pass'):
    """ log test case """
    now = time.time()
    global tc_name, tc_time, tc_status, tcases, ret
    tc = tc[:30] or tc_name #limit name
    if s in ['fatal']: 
        if tc_status == 'fatal': return
        tc_status = s
        print('*TC %-30s%6s%8.3f' % (tc_name,tc_status,now - tc_time)) #report previous tc or this fatal
        tcases[tc_name] = { tc_status, now - tc_time } #save previous tc
    elif s in ['fail']: 
        print('*TC %-30s%6s%8.3f' % (tc_name,s,now - tc_time)) #report previous tc or this fatal
        tcases['pass'] = tcases.get('pass',0)-1
        if driver is not None: driver.save_screenshot('./screenshot-'+tc_name+'.png')
        tcases[tc_name] = { s, now - tc_time } #save previous tc
    elif tc_status in ['pass']:
        print('*TC %-30s%6s%8.3f' % (tc_name,tc_status,now - tc_time)) #report previous tc or this fatal
        tcases[tc_name] = { tc_status, now - tc_time } #save previous tc

    tcases[s] = tcases.get(s,0)+1
    tc_name = tc; tc_status = s; tc_time = now #save this tc

def error():
    global ret; ret = 1
    traceback.print_exc(file=sys.stdout)
    #exc_type, exc_value, exc_traceback = sys.exc_info(); print (exc_value)
    if driver is not None: driver.save_screenshot('./screenshot.png')
    tc('','fatal')

def clean():
    if ret == 0: tc()
    total = 0
    for t in ['pass','fail','fatal']:
        total+=tcases.get(t,0)
        print ('*TC %s count\t%s' % (t,tcases.get(t,0)))
    print ('*TC total count\t',total)
    print (tcases)
    if driver is not None: driver.quit()
    sys.exit(ret)

