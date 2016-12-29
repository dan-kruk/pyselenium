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
#test rep stuff
tcases={}; tc_name='Begin'; tc_status='pass'; tc_time=time.time(); tcnt=0; junitfile=None  
ret=0
LOGS=os.environ.get('LOGS','./logs') #LOGS=${LOGS:-${JENKINS_HOME:+$WORKSPACE/$BUILD_NUMBER}}
os.environ["PATH"] += os.pathsep + os.pathsep.join(['drivers'])
if not os.path.exists(LOGS): os.makedirs(LOGS)
MODULE=os.environ.get('MODULE')
if MODULE is None:
    MODULE=sys.argv[0].split('/')
    if len(MODULE) >1:
        MODULE=MODULE[-2]+'.'+MODULE[-1].replace('.py','') #like feature.module
    elif len(MODULE) == 1:
        MODULE=MODULE[0].replace('.py','') #just module

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
    global driver, wait, wait3, FF, junitfile #globs
    if driver is not None: driver.quit(); driver = junitfile = None #reenter
    if os.environ.get('JENKINS_URL') is not None:
        junitfile = open(LOGS+'/junit-'+str(os.getpid())+'-'+MODULE+'.xml','w')
        junitfile.write('<testsuite name="'+MODULE+'">\n')
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
    now = time.time(); _s = None
    global tc_name, tc_time, tc_status, tcases, ret, tcnt
    tc = tc[:40] or tc_name #limit name
    if s in ['fatal']: 
        if tc_status == 'fatal': return
        tc_status = s
        tcases[tc_name] = { tc_status, now - tc_time } #save previous tc
    elif s in ['fail']: 
        _s=s
        tcases['pass'] = tcases.get('pass',0)-1
        if driver is not None: driver.save_screenshot(LOGS+'/screenshot-'+re.sub('[^a-zA-Z0-9]-',"_",tc_name)+'.png')
        tcases[tc_name] = { s, now - tc_time } #save previous tc
    elif tc_status in ['pass']:
        tcases[tc_name] = { tc_status, now - tc_time } #save previous tc
    
    print('*TC %-40s%6s%8.3f' % (tc_name,_s or tc_status,now - tc_time)) #report previous tc or this fatal
    tcnt+=1
    logjunit(str(tcnt).zfill(3)+': '+tc_name, _s or tc_status, now - tc_time)

    tcases[s] = tcases.get(s,0)+1
    tc_name = tc; tc_status = s; tc_time = now #save this tc

def error():
    global ret; ret = 1
    traceback.print_exc(file=sys.stdout)
    #exc_type, exc_value, exc_traceback = sys.exc_info(); print (exc_value)
    try: 
        if driver is not None: driver.save_screenshot(LOGS+'/screenshot-'+re.sub('[^a-zA-Z0-9-]',"_",tc_name)+'.png')
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
    if junitfile is not None: junitfile.write('</testsuite>\n'); junitfile.close()
    sys.exit(ret)

def logjunit(name, status, time):
    global junitfile
    s=''
    if junitfile is None: return
    #print (inspect.stack())
    if status in ['fail','fatal']:
        s='<failure message="'+status+' level error" type="reserved">\n'
        s+='\nscreenshot '+LOGS+'/screenshot-'+re.sub('[^a-zA-Z0-9-]',"_",tc_name)+'.png'+'\n\n'+traceback.format_exc()
        s+='</failure>\n'
    junitfile.write(re.sub('[<>&]','~','<testcase classname="'+MODULE+'/'+str(os.getpid())+'" name="'+name+'" time="'+str(time)+'">\n'+s+'</testcase>\n'))

