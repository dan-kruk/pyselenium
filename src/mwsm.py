import g #globs: driver, cfg, wait, wait3, FF, ...
from g import tc,prep
EC=g.EC; By=g.By; Keys=g.Keys #selenium statics

from mws import res #mws page resources, links etc

def login():
    if g.driver is None: prep()
    tc('get url '+g.cfg['url'])
    g.driver.get(g.cfg['url'])
    tc('login '+g.cfg['username']+'/'+g.cfg['password']) 
    g.driver.find_element_by_name('username').send_keys(g.cfg['username'] + Keys.RETURN)
    g.driver.find_element_by_name('password').send_keys(g.cfg['password'] + Keys.RETURN)
    x="//*/a[contains (@title, 'Logout')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def nav(link=''): #mapped res.links or "link"
    tc('nav'+link)
    g.driver.get(g.cfg['url']+'/'+res.links.get(link,link))

def logout():
    tc('logout')
    x="//*/a[contains (@title, 'Logout')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    g.wait.until(EC.element_to_be_clickable((By.NAME, 'username')))

