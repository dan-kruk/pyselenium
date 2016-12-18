from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as cpb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import os,sys,time,traceback,json,re

#boilerplate globs
driver = wait = wait3 = FF = None
tcases = {}; tc_name = 'Begin'; tc_status = 'pass'; tc_time = time.time()
ret=0


#cfg default
cfg = {
    'browser':'firefox',
    'capabilities':{},
    'remote':False,
    'hub':'http://127.0.0.1:4444/wd/hub',
    'wait':10
}

def loadenv(p, d={}): #$1: env var name with json'ish content, $2: default dict, ret: dict merge of var with default
    v = os.environ.get(p); print ('*env:',p,v)
    if v:
        # ' -> " and &apos; -> ' - allows useful shell expansions
        v=v.replace('\'','"'); v=v.replace('&apos;',"'")
        ret=dict(d, **json.loads(v))
    else: ret=d
    print ('+env:',p,ret)
    return ret

cfg = loadenv('cfg',cfg) 

for i in ['browser']: cfg[i] = cfg[i].lower() #normalize

def prep():
    global driver, wait, wait3, FF #globs
    if driver is not None: driver.quit(); driver = None #reenter
    #hub or local driver
    tc('init '+cfg['browser'])
    if cfg.get('remote'): 
        if cfg['browser'] == 'ie':  #ie needs some tweaks
            cfg['capabilities'].update(
                {'requireWindowFocus':'true','InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS':'true'}
        )
        capabilities = {'ie':cpb.INTERNETEXPLORER,'firefox':cpb.FIREFOX,'chrome':cpb.CHROME} [cfg['browser']]
        capabilities.update(cfg['capabilities'])
        print ('*capabilities:',capabilities)
        driver = wd.Remote(cfg['hub'], capabilities)
    else:
        driver = {'firefox':wd.Firefox,'chrome':wd.Chrome,'ie': wd.Ie} [cfg['browser']] ()

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
        if driver is not None: driver.save_screenshot('./screenshot-'+re.sub('[^a-zA-Z0-9]-',"_",tc_name)+'.png')
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
    try: 
        if driver is not None: driver.save_screenshot('./screenshot-'+re.sub('[^a-zA-Z0-9-]',"_",tc_name)+'.png')
    except: print(':( failed take screenshot')
    tc('','fatal')

def clean():
    if ret == 0: tc()
    total = 0
    for t in ['pass','fail','fatal']:
        total+=tcases.get(t,0)
        print ('*TC %s count\t%s' % (t,tcases.get(t,0)))
    print ('*TC total count\t',total)
    ##print (tcases)
    if driver is not None: driver.quit()
    sys.exit(ret)

