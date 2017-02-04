import g #globs: driver, wait, wait2, FF, ...
from mwsm import nav
from g import tc
import re,time
from selenium.common.exceptions import StaleElementReferenceException as stale
from selenium.common.exceptions import WebDriverException

EC=g.EC; By=g.By; Keys=g.Keys; Alert=g.Alert; Select=g.Select #selenium statics

"""
CCS UI (aka Central Configurator)
"""

def delpools (d=[{}]):
    """
    delete 1 or many db pools
    """
    x="//*[contains (@id, 'deleteBtn')]"
    ed = g.wait.until(EC.visibility_of_element_located((By.XPATH, x)))
    if type(d) is str: d = [{'name',d}]
    for p in d:
        p = p.get('name','AApool') #default
        try:
            x="//*[contains (@onclick, '_row"+p+":selectRow')]"
            e = g.driver.find_element(By.XPATH, x)
            #time.sleep(1) #agrr unchecks after seen checked!
            if g.FF: e.send_keys(Keys.SPACE)
            else: e.click()
        except: print ('*no existing pool',p); continue
        print ('*del existing pool',p)
    if ed.is_enabled(): ed.send_keys(Keys.RETURN)
    else: print('*Delete btn is disabled'); return
    time.sleep(1) #popup on
    x="//*[contains (@id, 'deleteSubmitButton')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).\
            send_keys(Keys.RETURN)
    time.sleep(2) #popup off

def createpool (d={}):
    """
    create db pool
    """
    name = d.get('name','AApool'); desc = d.get('desc',name+'a db pool')
    x="//*[contains (@id, 'htmlCommandButton')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))\
            .send_keys(Keys.RETURN)
    x="//*[contains (@id, 'selectOneCombobox')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(name)
    x="//*[contains (@id, 'zzz13')]"
    g.driver.find_element(By.XPATH, x).send_keys(desc)
    x="//*[contains (@id, 'driverNameMenu')]"
    g.driver.find_element(By.XPATH, x).\
            send_keys( d.get('db_type','SQL Server') )
    x="//*[contains (@id, 'currentDbUrlCtrl')]"
    g.driver.find_element(By.XPATH, x)\
            .send_keys( d.get('db_url',
    'jdbc:wm:sqlserver://usvardvmden141:1433;databaseName=opt912usvardvmden141'))
    x="//*[contains (@id, 'htmlInputText6')]"
    g.driver.find_element(By.XPATH, x).send_keys ( d.get('db_user','Administrator'))
    x="//*[contains (@id, 'htmlInputSecret')]"
    e = g.driver.find_element(By.XPATH, x)
    e.clear(); e.send_keys( d.get('db_pass','optimize') )
    x="//*[contains (@id, 'htmlCommandButton2')]"
    g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    x="//*[text()='Test Passed!']"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    x="//*[contains (@id, 'zzz4')]"
    g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    #bug1: just created pool put at bottom,
    #bug2: pool order link can click 1 time only, then disabled (seen in ff)
    #bug1 workaround - renav db page:
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//*/a[text()='My Profile']"))).send_keys(Keys.RETURN)
    nav('DatabasePoolConfiguration')
    x="//*[text() = '"+name+"']"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def createpools (d=[{}]):
    """
    create many db pools
    """
    for p in d:
        print ('*creating:',p)
        createpool(p)

#defaults may arguably be here
ccs = '{ "name":"AAZ", "desc":"AAZ env" }'
ccs = g.json.loads(ccs)

def create(d=ccs):
    """
    create env
    """
    tc('click add env btn')
    x="//*[@value='Add Environment...']"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).\
            send_keys(Keys.RETURN)
    tc('enter env name '+g.env.get("name","AAenv"))
    x="//*[@name='environmentName']"
    e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    e.clear(); e.send_keys(d.get('name'))
    tc('enter env desc'+g.env.get("desc","AAenv desc"))
    e = g.driver.find_element(By.NAME,'environmentDesc')
    e.clear(); e.send_keys(d.get('desc'))
    tc('click save env button')
    e = g.driver.find_element(By.NAME,'save').send_keys(Keys.RETURN)
    tc('check env is in list')
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,
        d.get('name','AAenv'))))

def envid(d={}): #u: env name, ret: envid
    u = d.get('name','AAenv')
    try: x="//*/a[text() = '"+u+"']"; e = g.driver.find_element(By.XPATH, x)
    except: print ('*no existing env '+u); return ''
    #lookup env as checkbox clueless
    uid=re.search('.+environmentID=(\d+)',e.get_attribute('href')).group(1)
    print ('*env id',uid)
    return uid

def delete(l=ccs):
    """
    del envs
    """
    tc('del envs')
    if type(l) is str: l=[{'name':l}]
    if type(l) is dict: l=[l]
    x="//*[@value='Add Environment...']"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    for u in l:
        x="//*[@type='checkbox' and @value='"+envid(u)+"']"
        e = g.driver.find_element(By.XPATH, x)
        u=u.get('name','AAenv')
        if g.FF: e.send_keys(Keys.SPACE)
        else: e.click()
    x="//*[@type='button' and @value='Delete']"
    e = g.driver.find_element(By.XPATH, x)
    if e.is_enabled():
        e.send_keys(Keys.RETURN)
        x="//*[@value='Delete' and @name='submitbutton']"
        #time.sleep(2)
        msg = Alert(g.driver).text
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
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,l)))\
            .send_keys(Keys.RETURN)
    x="//*[@name='environmentName']"
    e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def addservers(d=ccs):

    hb=g.driver.window_handles[0]
    x="//*[contains(@name, 'addLogicalServer')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))\
            .send_keys(Keys.RETURN)
    ha=g.driver.window_handles[1]
    g.driver.switch_to_window(ha)

    x="//*[contains(@name, 's')]"
    e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    for s in d.get('servers').values(): #multiselect
        print ('select',s)
        Select(e).select_by_value(s)
    x="//*[@value='OK']"
    g.wait.until(EC.element_to_be_clickable((By.XPATH,x)))\
            .send_keys(Keys.RETURN)

    g.driver.switch_to_window(hb)
    x="//*[contains(@name, 'addLogicalServer')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

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
    #Deprecated
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
    x="//*[@value='Save' and @type='submit']"
    g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    tc('check saved change')
    se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx))).is_selected()
    de = g.wait.until(EC.element_to_be_clickable((By.XPATH, dx))).is_selected()
    tc('saml/dls is '+str(se)+str(de))
    if s: assert se
    assert s is de

def togglesaml (s=True):
    #Deprecated
    sx="//*[@name='samlEnforced_boolean']"
    se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx)))
    s0=se.is_selected()
    if s is not s0:
        tc('toggle saml from '+str(s0)); se.click()
    tc('click save')
    x="//*[@value='Save' and @type='submit']"
    g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    tc('check saved change')
    se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx))).is_selected()
    tc('act/exp saml '+str(se)+str(s))
    assert s is se

def navtab(t):
    tc('click tab '+t)
    try: #rather than sleep and hope
        x="//*[text()='"+t+"']"
        g.wait.until(EC.element_to_be_clickable((By.XPATH,
            x))).send_keys(Keys.RETURN)
        if g.FF:
            x="//*[text()='"+t+"']"
            g.wait.until(EC.element_to_be_clickable((By.XPATH,
                x))).send_keys(Keys.RETURN)
    except (stale,WebDriverException):
        tc('stale element retry')
        time.sleep(.5)
        e = g.wait.until(EC.element_to_be_clickable((By.XPATH,
            x))).send_keys(Keys.RETURN)
    if t == 'Validate': #piggyback
        x="//*[@name='validateResult']"
        g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    elif t == 'Configure Servers': #click to expand tree
        x="//*/img[@title='Expand All' or @title='Collapse All']"
        e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
        if e.get_attribute('title') == 'Expand All': #click if needed
            e.click()

def navconfig (c):
    """
    take envid and config name, nav to that config
    """
    tc('nav '+c)
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,c)))\
            .send_keys(Keys.RETURN)

def _submit_conf_settings(x='Save'): #Save|Reset
    tc('click button '+x)
    g.driver.find_element(By.XPATH,
            "//input[@value='"+x+"']").send_keys(Keys.RETURN)

def pt_settings(x={}):
    """
    configure Process Tracker settings
    """
    if x.get('mapi_eda',None):
        x['mapi_eda']={'eda':' eda'}.get(x['mapi_eda'],'mapi') #remap ' eda'
        tc('click radiobutton='+x['mapi_eda'])
        g.wait.until(EC.element_to_be_clickable((By.XPATH,
            "//input[@value='"+x[ 'mapi_eda' ]+"']"))).click()
    for x1 in ['processInstanceCacheSize','modelRefreshInterval'
        ,'maxStagingDataQueueSize','stagingDataQueueConsumptionSize'
        ,'stagingDataDelay']:
        if x.get(x1,None):
            v=str(x[x1])
            tc('input '+x1+'='+v)
            e=g.wait.until(EC.element_to_be_clickable((By.XPATH,
                "//input[@name='"+x1+"']")))
            e.clear(); e.send_keys(v)
    _submit_conf_settings()
    #TODO return {saved settings}

def station_settings (x={}):
    """
    control saml, dls, dlscache flags (Station Settings)
    """
    d=[x.get('saml',True),x.get('dls',False),x.get('dlscache',False)]
    tc('checkbox presence')
    sx="//*[@name='samlEnforced_boolean']"
    se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx)))
    for c,x in zip(d,['samlEnforced','dlsEnabled','dlsCacheEnabled']):
        sx="//*[@name='"+x+"_boolean']"
        se = g.driver.find_element(By.XPATH, sx); s0=se.is_selected()
        if c is not s0:
            tc('toggle '+x+' '+str(c)+' from '+str(s0)); se.click()
    _submit_conf_settings()
    tc('check saved change')
    sx="//*[@name='samlEnforced_boolean']"
    se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx)))
    for c,x in zip(d,['samlEnforced','dlsEnabled','dlsCacheEnabled']):
        sx="//*[@name='"+x+"_boolean']"
        se = g.driver.find_element(By.XPATH, sx); s0=se.is_selected()
        tc('act/exp '+x+' '+str(s0)+str(c))
        assert c is s0

def modmwspath(d={}):
    navtab('Map Endpoints')
    tc('locate mwspath input')
    #if None - only check input presence
    r = d.get('mapendpoints',{}).get('mwspath',None)
    try: #rather than sleep and hope
        x="//*[contains(@name,'MWS_path') and @type='text']"
        e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    except stale:
        tc('stale element retry')
        time.sleep(.2)
        e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    if r == '': tc('unset mws path '+r); e.clear()
    else: tc('set mws path '+r); e.clear(); e.send_keys(r)
    tc('click save mapendpoints');
    x="//*[@type='submit' and @value='Save']"
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        x))).send_keys(Keys.RETURN)
    tc('check saved mwspath')
    time.sleep(1)
    x="//*[contains(@name,'MWS_path') and @type='text']"
    e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    assert e.get_attribute('value') == r

def validate():
    navtab('Validate')
    tc('check env is valid')
    x="//*/b[text()='Valid Configuration']"
    e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def finish(d):
    tc('click finish')
    x="//*[@type='button' and @name='finish']"
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        x))).send_keys(Keys.RETURN)
    l = d.get('name','AAenv'); tc('locate env link '+l)
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,l)))

def deploy(d,a='Deploy All'): #a: Deploy Updates | Deploy All
    e = envid(d)
    tc('deploy env '+e)
    x="//*/a[contains (@href, 'environmentID="+e+"&')\
            and contains (@href, 'isDeployed=')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        x))).send_keys(Keys.RETURN)
    tc('click '+a)
    x="//*[@value='"+a+"']"; g.wait.until(EC.element_to_be_clickable((By.XPATH,
        x))).send_keys(Keys.RETURN)
    tc('check deployment status')
    x="//*/b[text()='Successfully deployed environment.']"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    #may check just specific server deploy status
    #x="//*/textarea[@name='deployResult']"
    #e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    #print(e.get_attribute('value'));
    #assert 'Deployed logical server \"Analytic Engine v'\
    #        in e.get_attribute('value') #focus on ok for one server
    tc('return to env list');
    x="//*[@type='submit' and @value='Close']"
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        x))).send_keys(Keys.RETURN)
    l = d.get('name','AAenv'); tc('locate env link '+l)
    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,l)))

def mapendpoints(d):
    pass

