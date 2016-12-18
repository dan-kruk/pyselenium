import g #globs: driver, wait...
from g import tc,prep,loadenv
EC=g.EC; By=g.By; Keys=g.Keys #selenium statics

from mws import res #mws page resources, links etc


cfg = loadenv('login',{'url':'http://localhost:8585','username':'Administrator','password':'manage'})

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
    tc('nav'+link)
    g.driver.get(cfg['url']+'/'+res.links.get(link,link))

def logout():
    tc('logout')
    x="//*/a[contains (@title, 'Logout')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    g.wait.until(EC.element_to_be_clickable((By.NAME, 'username')))

