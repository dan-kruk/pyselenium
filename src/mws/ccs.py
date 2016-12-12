import glob as g #globs: driver, wait, wait3, FF, ...

EC=g.EC; By=g.By; Keys=g.Keys #selenium statics

from time import sleep

"""
CCS UI (aka Central Configurator)
"""

def delpools (d=[{}]):
    """
    delete 1 or many db pools
    """
    x="//*[contains (@id, 'deleteBtn')]"; ed = g.wait.until(EC.visibility_of_element_located((By.XPATH, x)))
    if type(d) is str: d = [{'name',d}]
    for p in d:
        p = p.get('name','AApool') #default
        try:
            x="//*[contains (@onclick, '_row"+p+":selectRow')]"; e = g.driver.find_element(By.XPATH, x)
            #sleep(1) #agrr unchecks after seen checked!
            if g.FF: e.send_keys(Keys.SPACE)
            else: e.click()
        except: print ('*no existing pool',p); continue
        print ('*del existing pool',p)
    if ed.is_enabled(): ed.send_keys(Keys.RETURN) 
    else: print('*Delete btn is disabled'); return
    sleep(1) #popup on
    x="//*[contains (@id, 'deleteSubmitButton')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    sleep(2) #popup off

def createpool (d={}):
    """
    create db pool
    """
    name = d.get('name','AApool'); desc = d.get('desc',name+'a db pool')
    x="//*[contains (@id, 'htmlCommandButton')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    x="//*[contains (@id, 'selectOneCombobox')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(name)
    x="//*[contains (@id, 'zzz13')]"; g.driver.find_element(By.XPATH, x).send_keys(desc)
    x="//*[contains (@id, 'driverNameMenu')]"; g.driver.find_element(By.XPATH, x).send_keys( d.get('db_type','SQL Server') )
    x="//*[contains (@id, 'currentDbUrlCtrl')]"; g.driver.find_element(By.XPATH, x).send_keys( d.get('db_url','jdbc:wm:sqlserver://usvardvmden141:1433;databaseName=opt912usvardvmden141') ) 
    x="//*[contains (@id, 'htmlInputText6')]"; g.driver.find_element(By.XPATH, x).send_keys ( d.get('db_user','Administrator') )
    x="//*[contains (@id, 'htmlInputSecret')]"; e = g.driver.find_element(By.XPATH, x); e.clear(); e.send_keys( d.get('db_pass','optimize') )
    x="//*[contains (@id, 'htmlCommandButton2')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    x="//*[text()='Test Passed!']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    x="//*[contains (@id, 'zzz4')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    #bug1: just created pool put at bottom, bug2: pool order link can click 1 time only, then disabled (seen in ff)
    #bug1 workaround - renav db page:
    e = g.driver.find_element(By.XPATH,"//*/a[text()='My Profile']").send_keys(Keys.RETURN)
    g.nav('DatabasePoolConfiguration')
    x="//*[text() = '"+name+"']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))

def createpools (d=[{}]): 
    """
    create many db pools
    """
    for p in d:
        print ('*creating:',p)
        createpool(p)

