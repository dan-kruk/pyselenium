import g #globs: driver, wait, wait3, FF, ...
from mwsm import nav

from g import tc
import re,time
from selenium.common.exceptions import StaleElementReferenceException as stale
from selenium.common.exceptions import WebDriverException
EC=g.EC; By=g.By; Keys=g.Keys; Alert=g.Alert #selenium statics
from selenium.webdriver.support.select import Select

#oh my ccs it is
ccs = '{ "name":"AAZ", "desc":"AAZ env" }'
ccs = g.json.loads(ccs)

#"servers":{ "ae":"Analytic Engine v10", "ae1":"","dc":"","mws":"" },
#"serversl":["Analytic Engine v9.12.0.0","ae1","dc","mws"],
#"template":["o4p","o4i"],
#"config":{
#	"default":{
#		"jndi":{ "broker":"", "factory":"", "clusterurl":"" },
#		"tsaurl":""
#	}
#	,"ae": {
#		"station":{ "saml":false, "dls":false },
#		"email":{ "server":"","templates":"res/templates.data" },
#		"eventpub":{ "kpireadings":true,"kpistats":"false","kpinames":"..." },
#		"wsactions":"res/wsactions.xml",
#		"pt":{ "inputevents":"eda|mapi","modelrefresh":300000 }
#	}
#	,"infradc": {
#		"collector":{ "pollint":2, "broker":false,"is":true },
#		"umcluster":{ "statuspoll":30,"auto":true }
#	}
#},
#"hosts":["h1","h2"],
#"mapservers":{ "ae":"h1","ae1":"h2","infradc":"h1" },
#"mapservers":"all",
#"mapendpoints": {"ae":  { "confagent":{ "protocol":"http","port":"15000", "user":"Administrator" },
#			  "jmsconn":"...",
#			  "wsregistry":{ "protocol":"http","port":"12503","path":"alt","pass":"manage" }
#			}
#		 "jms": { "protocol":"nsp","port":"9000", "user":"Administrator" },
#		 "mws": { "protocol":"https","port":"443", "user":"Administrator" }
#		},
#"mapdbpools":{ "analysis.engine.ae1":"p1","common.directory.ae1":"p2" }

def tst():
    tc('case 1')
    time.sleep(1)
    tc('case 2')
    time.sleep(2); #assert False,'oops had to quit'
    tc('case 3'); tc('','fail')
    time.sleep(.2); tc('','end')
    time.sleep(2)
    tc('case 4'); time.sleep(.1); tc('','end');
    time.sleep(3)

def create(d=ccs):
    """
    create env
    """
    tc('click add env btn')
    x="//*[@value='Add Environment...']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    tc('enter env name '+g.env.get("name","AAenv"))
    x="//*[@name='environmentName']"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x))); e.clear(); e.send_keys(d.get('name'))
    tc('enter env desc'+g.env.get("desc","AAenv desc"))
    e = g.driver.find_element(By.NAME,'environmentDesc'); e.clear(); e.send_keys(d.get('desc'))
    tc('click save env button')
    e = g.driver.find_element(By.NAME,'save').send_keys(Keys.RETURN)
    tc('check env is in list')
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,d.get('name','AAenv'))))

def envid(d={}): #u: env name, ret: envid
    u = d.get('name','AAenv')
    try: x="//*/a[text() = '"+u+"']"; e = g.driver.find_element(By.XPATH, x)
    except: print ('*no existing env '+u); return ''
    uid=re.search('.+environmentID=(\d+)',e.get_attribute('href')).group(1) #lookup env as checkbox clueless
    print ('*env id',uid)
    return uid

def delete(l=ccs):
    """
    del envs
    """
    tc('del envs')
    if type(l) is str: l=[{'name':l}]
    if type(l) is dict: l=[l]
    x="//*[@value='Add Environment...']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    for u in l:
        x="//*[@type='checkbox' and @value='"+envid(u)+"']"; e = g.driver.find_element(By.XPATH, x)
        u=u.get('name','AAenv')
        #note ff driver bug http://stackoverflow.com/questions/40080077/selenium-3-firefox-click-not-working
        if g.FF: e.send_keys(Keys.SPACE)
        else: e.click()
    x="//*[@type='button' and @value='Delete']"; e = g.driver.find_element(By.XPATH, x)
    if e.is_enabled():
        e.send_keys(Keys.RETURN)
        x="//*[@value='Delete' and @name='submitbutton']"
        #sleep(2)
        msg = Alert(g.driver).text
        #print(msg,'---')
        #assertEqual('You are about to delete 1 Environment(s). Do you want to delete these Environment(s)?', msg)
        Alert(g.driver).accept()
        print('*deleted existing envs:',l)
        try: 
            x="//*/a[text() = '"+u+"']"; e = g.driver.find_element(By.XPATH, x)
            print ('*env still seen'+u); assert False,'env steel seen!'
        except: print ('*no env seen as expected '+u)
    else: print('*no existing envs:',l)

def navenv(d=ccs):
    """
    nav to env
    """
    l = d.get('name','AAenv')
    tc('locate click env link '+l)
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,l))).send_keys(Keys.RETURN)
    x="//*[@name='environmentName']"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    
def addservers(d=ccs):

    hb=g.driver.window_handles[0]
    x="//*[contains(@name, 'addLogicalServer')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    ha=g.driver.window_handles[1]
    g.driver.switch_to_window(ha)

    x="//*[contains(@name, 's')]"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    for s in d.get('servers').values(): #multiselect
        print ('select',s)
        Select(e).select_by_value(s) 
    x="//*[@value='OK']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)

    g.driver.switch_to_window(hb)
    x="//*[contains(@name, 'addLogicalServer')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def serverids(): #ret: {} all existing server ids
        x="//*[contains(@href,'doEditLogicalServerPopup')]";
        pass

    #e=g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,c)))
    #actions = ActionChains(g.driver)
    #actions.move_to_element(e).click().perform()
    #actions.keyDown(Keys.LEFT_CONTROL)
    #for s in d.get('servers').values(): #multiselect
    #    x="//*[contains(@id,'"+u+"')]"; e = g.driver.find_element(By.XPATH, x)
    #    e.click()
    #actions.keyUp(Keys.LEFT_CONTROL)
    #actions.build()
    #actions.perform()

def toggledls (s=True):
    sx="//*[@name='samlEnforced_boolean']"
    dx="//*[@name='dlsEnabled_boolean']"
    se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx)))
    de = g.wait.until(EC.element_to_be_clickable((By.XPATH, dx)))
    s0=se.is_selected()
    d0=de.is_selected()
    if s and not s0:
        tc('toggle saml to '+str(s)+' from '+str(s0)); se.click()
    if s is not d0:
        tc('toggle dls to '+str(s)+' from '+str(d0)); de.click()
    tc('click save')
    x="//*[@value='Save' and @type='submit']"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    tc('check saved change')
    se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx))).is_selected()
    de = g.wait.until(EC.element_to_be_clickable((By.XPATH, dx))).is_selected()
    tc('saml/dls is '+str(se)+str(de))
    if s: assert se
    assert s is de
     
def togglesaml (s=True):
    sx="//*[@name='samlEnforced_boolean']"
    se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx)))
    s0=se.is_selected()
    if s is not s0:
        tc('toggle saml from '+str(s0)); se.click()
    tc('click save')
    x="//*[@value='Save' and @type='submit']"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    tc('check saved change')
    se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx))).is_selected()
    tc('saml is '+str(se))
    assert s is se

def navconfig (c):
    """take envid and config name, nav to that config"""
    tc('nav '+c)
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,c))).send_keys(Keys.RETURN)

def navtab(t):
    tc('click tab '+t)
    try: #rather than sleep and hope
        x="//*[text()='"+t+"']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
        if g.FF: x="//*[text()='"+t+"']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    except (stale,WebDriverException):
        tc('stale element retry')
        time.sleep(.5)
        e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    if t == 'Validate': #piggyback
        x="//*[@name='validateResult']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    elif t == 'Configure Servers': #click to expand tree
        x="//*/img[@title='Expand All' or @title='Collapse All']"; e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
        if e.get_attribute('title') == 'Expand All': #click if needed
            e.click()

def modmwspath(d={}):
    navtab('Map Endpoints')
    tc('locate mwspath input')
    r = d.get('mapendpoints',{}).get('mwspath',None) #if None - only check input presence
    try: #rather than sleep and hope
        x="//*[contains(@name,'MWS_path') and @type='text']"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    except stale:
        tc('stale element retry')
        time.sleep(.2)
        e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    if r == '': tc('unset mws path '+r); e.clear()
    else: tc('set mws path '+r); e.clear(); e.send_keys(r)
    tc('click save mapendpoints');
    x="//*[@type='submit' and @value='Save']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    tc('check saved mwspath')
    time.sleep(1)
    x="//*[contains(@name,'MWS_path') and @type='text']"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    assert e.get_attribute('value') == r

def validate():
    navtab('Validate')
    tc('check env is valid')
    x="//*/b[text()='Valid Configuration']"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def finish(d):
    tc('click finish')
    x="//*[@type='button' and @name='finish']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    l = d.get('name','AAenv'); tc('locate env link '+l)
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,l)))

def deploy(d,a='Deploy All'): #a: Deploy Updates | Deploy All
    e = envid(d)
    tc('deploy env '+e)
    x="//*/a[contains (@href, 'environmentID="+e+"&') and contains (@href, 'isDeployed=')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN) 
    tc('click '+a)
    x="//*[@value='"+a+"']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN) 
    tc('check deployment status')
    x="//*/b[text()='Successfully deployed environment.']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    #may check just specific server deploy status
    #x="//*/textarea[@name='deployResult']"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    #print(e.get_attribute('value'));
    #assert 'Deployed logical server \"Analytic Engine v' in e.get_attribute('value') #focus on ok for one server
         
    tc('return to env list');
    x="//*[@type='submit' and @value='Close']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    l = d.get('name','AAenv'); tc('locate env link '+l)
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,l)))
 
def mapendpoints(d):
    pass

def ccs (): #TODO - mv t/mws/bvtccs.py
    """
    complete ccs configure thing
    """
    nav("db")
    g.loadenv("db")
    createdbpools()

    nav("ccs")
    g.loadenv("ccs")
    create()
    nav()
    servers()
    config()
    hosts()
    mapservers() #mapallservers() - quick thing
    mapendpoints()
    mapdbpools()

    nav("ccs")
    checkserverstatus()

