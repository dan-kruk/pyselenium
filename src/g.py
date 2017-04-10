from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as cpb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import os,sys,time,traceback,json,re
from time import sleep

#boilerplate globs
driver = wait = wait1 = wait3 = wait20 = wait60 = FF = None
#test rep stuff
tcases={}; tc_name='Begin'; tc_status='pass'; tc_time=time.time(); tcnt=0; junitfile=None
ret=0
LOGS=os.environ.get('LOGS','./logs') #LOGS=${LOGS:-${JENKINS_HOME:+$WORKSPACE/$BUILD_NUMBER}}
os.environ["PATH"] += os.pathsep + os.pathsep.join(['drivers'])
if not os.path.exists(LOGS): os.makedirs(LOGS)

JUNIT_PKG=os.environ.get('JUNIT_PKG')

MODULE=sys.argv[0].split('/')
if len(MODULE) >1:
    MODULE=(JUNIT_PKG or MODULE[-2]) + '.' + MODULE[-1].replace('.py','') #like feature.module
elif len(MODULE) == 1:
    MODULE=MODULE[0].replace('.py','') #just module

if os.environ.get('JENKINS_URL') is not None:
    junitfile = open(LOGS+'/junit-'+str(os.getpid())+'-'+MODULE+'.xml','w')
    junitfile.write('<testsuite name="'+MODULE+'">\n')

#cfg default
cfg = {
    'browser':'firefox',
    'capabilities':{},
    'remote':False,
    'hub':'http://127.0.0.1:4444/wd/hub',
    'wait':10
}
def loadenv(p, d={}):
    #$1: env var name with json'ish content, $2: default dict, ret: dict merge of var with default
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
    global driver, wait, wait1, wait3, wait20, wait60, FF #globs
    if driver is not None: driver.quit(); driver = None #reenter
    #hub or local driver
    tc('init '+cfg['browser'])
    if cfg.get('remote'):
        if cfg['browser'] == 'ie':  #ie needs some tweaks
            cfg['capabilities'].update(
                {'requireWindowFocus':'true','InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS':'true'}
        )
        capabilities = {'ie':cpb.INTERNETEXPLORER,'firefox':cpb.FIREFOX,'chrome':cpb.CHROME, 'edge':cpb.EDGE} [cfg['browser']]
        capabilities.update(cfg['capabilities'])
        print ('*capabilities:',capabilities)
        driver = wd.Remote(cfg['hub'], capabilities)
    else:
        driver = {'firefox':wd.Firefox,'chrome':wd.Chrome,'ie': wd.Ie} [cfg['browser']] ()

    FF = True if cfg['browser'] == 'firefox' else False

    tc('maximize '+cfg['browser'])
    driver.maximize_window(); #max for inclusive screenshots
    wait = WebDriverWait(driver, int(cfg['wait']))
    wait1 = WebDriverWait(driver, 1)
    wait3 = WebDriverWait(driver, 3)
    wait20 = WebDriverWait(driver, 20)
    wait60 = WebDriverWait(driver, 60)

def screenshot(act=True):
    x=LOGS+'/screenshot-'+str(os.getpid())+'-'+re.sub('[^a-zA-Z0-9-]',"_",tc_name)
    try:
        if driver is not None:
            if act:
                driver.save_screenshot(x+'.png')
                print('screenshot: '+x+'.png\n')
                #save page src as well
                f = open(x+'.html','w')
                f.write(driver.page_source); f.close()
            return x+'.png'
    except: print('screenshot failed: '+x+'\n')

def tc(tc='',s='pass'):
    """ log test case """
    now = time.time(); _s = None
    global tc_name, tc_time, tc_status, tcases, ret, tcnt
    tc = tc[:60] or tc_name #limit case name
    if s in ['fatal']:
        #if tc_status == 'fatal': return
        tc_status = s
        tcases[tc_name] = { tc_status, now - tc_time } #save previous tc
    elif s in ['fail']:
        _s=s
        tcases['pass'] = tcases.get('pass',0)-1
        screenshot()
        tcases[tc_name] = { s, now - tc_time } #save previous tc
    elif tc_status in ['pass']:
        tcases[tc_name] = { tc_status, now - tc_time } #save previous tc

    #report previous tc or this fatal
    print('*TC %-60s%6s%8.3f' % (tc_name,_s or tc_status,now - tc_time))
    tcnt+=1

    if not _s: #skip dup fail case log
        logjunit(str(tcnt).zfill(3)+': '+tc_name, _s or tc_status,
                now - tc_time)

    tcases[s] = tcases.get(s,0)+1
    tc_name = tc; tc_status = s; tc_time = now #save this tc

def focus_iframe():
    #driver.switch_to_frame(wait.until(
    #   EC.element_to_be_clickable((By.TAG_NAME, 'iframe'))))
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))
    tc('focused on iframe:'+driver.current_window_handle+' '+driver.title)

def focus_main():
    driver.switch_to.default_content()
    #print("==="+driver.title)

def focus(n=0):
    #i=0 #timeout check on nth handle presence
    #while i<5 and len(driver.window_handles)<n:
    #    print('re-focus window..'); sleep(1); i+=1
    driver.switch_to.window(driver.window_handles[n])
    tc('focused on window:'+str(n)+' '+driver.current_window_handle\
            +' '+driver.title)

def error():
    global ret; ret = 1
    print('\n'+traceback.format_exc())
    screenshot()
    tc('','fatal')

def clean():
    if ret == 0: tc()
    total = 0
    for t in ['pass','fail','fatal']:
        total+=tcases.get(t,0)
        print ('*TC %s count\t%s' % (t,tcases.get(t,0)))
    print ('*TC total count\t',total)
    print()
    ##print (tcases)
    if junitfile is not None:
        junitfile.write('</testsuite>\n'); junitfile.close()
        print('junit: '+junitfile.name)
    if driver is not None: driver.quit()
    sys.exit(ret)

def logjunit(name, status, time):
    if junitfile is None: return
    s=''
    if status in ['fail','fatal']:
        s='<failure message="error" type="'+status+'">\n'
        x=screenshot(False)
        if x: s+='\nscreenshot '+x+'\n\n'
        if not traceback.format_exc().startswith('NoneType'):
            s+=re.sub('[<>&]','~',traceback.format_exc())
        s+='</failure>\n'
    junitfile.write('<testcase classname="'+MODULE+'/'+str(os.getpid())\
        +'" name="'+re.sub('[<>&]','~',name)\
        +'" time="'+str(time)+'">\n'+s+'</testcase>\n')

