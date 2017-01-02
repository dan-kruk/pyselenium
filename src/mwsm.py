import g #globs: driver, wait...
from g import tc,prep,loadenv
EC=g.EC; By=g.By; Keys=g.Keys; Select=g.Select #selenium statics

from mws import res #mws page resources, links etc
from os import environ as e

H=e.get('HOSTNAME', e.get('COMPUTERNAME','localhost')) #guess

cfg = loadenv('login',{'url':'http://'+H+':8585','username':'Administrator','password':'manage'})

def login(d={}):
    global cfg
    cfg = dict(cfg, **d)
    if g.driver is None: prep()
    tc('get url '+cfg['url'])
    g.driver.get(cfg['url'])
    tc('login '+cfg['username']+'/'+cfg['password']) 
    g.driver.find_element_by_name('username').send_keys(cfg['username'] + Keys.RETURN)
    g.driver.find_element_by_name('password').send_keys(cfg['password'] + Keys.RETURN)
    x="//*/a[contains (@title, 'Logout')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def nav(link=''): #mapped res.links or "link"
    tc('nav '+link)
    g.driver.get(cfg['url']+'/'+res.links.get(link,link))

def navauth(link=''): #include user/pass in url
    if g.driver is None: prep()
    tc('get url '+cfg['url'])
    tc('login '+cfg['username']+'&'+cfg['password']) 
    tc('navauth '+link)
    g.driver.get(cfg['url']+'/'+res.links.get(link,link)+'?username='+cfg['username']+'&password='+cfg['password'])

def server(name): #BPM and BAM|BPM only|BAM only|BVTEnv
    """select server dropdown on many optimize (usually) pages"""
    tc('select server '+name)
    x="//*[@name='serverNameInput']"; e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    Select(e).select_by_visible_text(name)

def logout():
    tc('logout')
    x="//*/a[contains (@title, 'Logout')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    g.wait.until(EC.element_to_be_clickable((By.NAME, 'username')))

