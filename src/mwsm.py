import g #globs: driver, wait...
from g import tc,prep,loadenv
EC=g.EC; By=g.By; Keys=g.Keys; Select=g.Select #selenium statics

from mws import res #mws page resources, links etc
from os import environ as e
from time import sleep

H=e.get('hostname', e.get('HOSTNAME', e.get('COMPUTERNAME','localhost'))) #guess

cfg = loadenv('login',{'url':'http://'+H+':8585',
'username':'Administrator','password':'manage'})

def login(d={}):
    global cfg
    cfg = dict(cfg, **d)
    if g.driver is None: prep()
    tc('get url '+cfg['url'])
    g.driver.get(cfg['url'])
    tc('login '+cfg['username']+'/'+cfg['password'])
    g.wait.until(EC.element_to_be_clickable((By.NAME, 'username')))\
            .send_keys(cfg['username'] + Keys.RETURN)
    g.driver.find_element_by_name('password')\
            .send_keys(cfg['password'] + Keys.RETURN)
    x="//*/a[contains (@title, 'Logout')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def nav(link=''): #mapped res.links or "link"
    tc('nav '+link)
    g.driver.get(cfg['url']+'/'+res.links.get(link,link))

def navauth(link=''): #include user/pass in url
    if g.driver is None: prep()
    tc('get url '+cfg['url'])
    tc('login '+cfg['username']+'&'+cfg['password'])
    tc('navauth '+link)
    g.driver.get(cfg['url']+'/'+res.links.get(link,link)+'?username='\
            +cfg['username']+'&password='+cfg['password'])

def logout():
    tc('logout')
    x="//*/a[contains (@title, 'Logout')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    g.wait20.until(EC.element_to_be_clickable((By.NAME, 'username')))

def overlay_handler(w=.1): #progress bar overlay
    tc('wait overlay gone')
    x="//*[contains(@id,'overlay')]"
    o=g.wait.until(EC.presence_of_element_located((By.XPATH, x)))
    g.wait20.until(EC.staleness_of(o))
    sleep(w)

def overlay(): #yellowish overlays
    try:
        tc('overlay probe')
        e=g.wait3.until(EC.element_to_be_clickable((By.XPATH,
            "//div[contains (@style,'opacity: ')]")))
        tc('overlay stale')
        g.wait.until(EC.staleness_of(e))
    except:
        tc('overlay flick')

def progressbar(): #progress bar overlays
    try:
        tc('progressbar probe')
        e=g.wait3.until(EC.element_to_be_clickable((By.XPATH,
            "//div[contains (@id,'overlay') and\
            @class='caf-progress' and @role='progressbar']")))
        tc('progressbar stale')
        g.wait20.until(EC.staleness_of(e))
    except:
        tc('progressbar flick')

def stale(e): #block until webelement is stale
        tc('stale element')
        g.wait20.until(EC.staleness_of(e))

def server(name, at=''):
    """
    select server dropdown on many optimize (usually) pages
    name: BPM and BAM|BPM only|BAM only|BVTEnv
    at:   nav to link (optional)
    """
    if at: nav(at)
    tc('select server '+name)
    x = "//select[@name='serverNameInput']"
    e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    s = Select(e)
    if s.first_selected_option.text != name:
        tc('select server from '+s.first_selected_option.text+' to '+name)
        s.select_by_visible_text(name)
        stale(e) #page flicks

def search(text):
    """
    search for text in search widgets like on Problems page
    """
    tc('search '+text)
    e = g.wait.until(EC.element_to_be_clickable((By.XPATH,\
        "//input[@name='keywords']")))
    e.clear() #input may retain
    e.send_keys(text)
    g.wait.until(EC.element_to_be_clickable((By.XPATH,\
        "//input[@name='dosearch']"))).click()
    g.wait.until(EC.staleness_of(e))

def close():
    """click close btn
    """
    x = "//input[contains(@name,'closeBtn')]"
    e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    e.send_keys(Keys.RETURN)
    g.wait.until(EC.staleness_of(e))

def caf_error():
    """check for caf errors
        @ret [caf error elements]
    """
    #x = "//*[@class='caf-error-summary']"
    tc('check for caf errors')
    try:
        e = g.driver.find_elements_by_class_name('caf-error-summary')
    except:
        pass
    return e

