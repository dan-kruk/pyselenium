import glob as g #globs: driver, wait, wait3, g.FF, ...
EC=g.EC; By=g.By; Keys=g.Keys #selenium statics

from time import sleep

"""
mws cluster settings
"""

def chroot (d={"root":"alt"}):
    """
    create/update/clear mws cluster root context; '' - clears context
    """
    if type(d) is str: d={'root':d}
    x=".//*[contains (@id, 'clusteredSetupPanel')]"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x))); e.click()
    sleep(1) #dom mutations TODO fix
    x=".//*[contains (@id, 'clusterRootcontext')]"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x))); e.clear()
    if d['root'] : e.send_keys(d.get('root'))
    x=".//*[contains (@id, 'submitButton')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    x=".//*[text()='Changes to Cluster Node roles or ports are only effective after the Node restart']"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    x=".//*[contains (@id, 'standaloneSetupPanel')]"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x))); e.click()
    sleep(1) #dom mutations TODO fix

