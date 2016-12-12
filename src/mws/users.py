import glob as g #globs: driver, wait, wait3, FF, ...
EC=g.EC; By=g.By; Keys=g.Keys #selenium statics
import re

"""
Users and roles mgmt UI
"""

def createuser (d={'user','AAuser'}):
    """
    create mws user and assign a role
    """
    print ('*creating:',d)
    x="//*[@value='Add User...']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    x="//*[@name='name']"; e = g.wait.until(EC.element_to_be_clickable((By.XPATH, x))); e.clear(); e.send_keys(d.get('user'))
    x="//*[@name='password']"; e = g.driver.find_element(By.XPATH, x); e.clear(); e.send_keys('optimize')
    x="//*[@name='password-confirm']"; e = g.driver.find_element(By.XPATH, x); e.clear(); e.send_keys('optimize')
    x="//*[@name='firstName']"; e = g.driver.find_element(By.XPATH, x); e.clear(); e.send_keys('firstName')
    x="//*[@name='lastName']"; e = g.driver.find_element(By.XPATH, x); e.clear(); e.send_keys(d.get('ln','lastName'))
    x="//*[@name='email']"; e = g.driver.find_element(By.XPATH, x); e.clear(); e.send_keys(d.get('email',d.get('user')+'@softwareag.com'))
    x="//*[@name='submitbutton']"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    x="//*[@name='name' and @type='hidden' and @value='"+d.get('user')+"']"; g.wait.until(EC.presence_of_element_located((By.XPATH, x)))
    x="//*[@name='cancelbutton']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)
    x="//*[@value='Add User...']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))) #fuzzy check, when (many) users paged off
    #x="//*/a[text() = '"+d.get('user')+"']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))  #strict check, all users on (same) page

def createusers (l=[{}]):
    """
    create users bulk
    """
    for d in l: createuser(d)

def delusers (l=[{'user':'AAuser'}]):
    """
    delete mws user or bulk of users
    """
    if type(l) is str: l=[{'user':l}] #can take user 'doe'
    x="//*[@value='Add User...']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    for u in l:
        u=u.get('user','AAuser')
        try: x="//*/a[text() = '"+u+"']"; e = g.driver.find_element(By.XPATH, x)
        except: print ('*no existing user '+u); continue
        uid=str(int ( re.search('.+/(.+)',e.get_attribute('href')).group(1) )) #lookup user as checkbox clueless
        x="//*[@type='checkbox' and @value='"+uid+"']"; e = g.driver.find_element(By.XPATH, x)
        #note ff driver bug http://stackoverflow.com/questions/40080077/selenium-3-firefox-click-not-working
        if g.FF: e.send_keys(Keys.SPACE)
        else: e.click()
    x="//*[contains(@name,'fnButton2')]"; e = g.driver.find_element(By.XPATH, x)
    if e.is_enabled():
        e.send_keys(Keys.RETURN)
        x="//*[@value='Delete' and @name='submitbutton']"; g.wait.until(EC.presence_of_element_located((By.XPATH, x))).send_keys(Keys.RETURN)
        print('*deleted existing users:',l)
    else: print('*no existing users:',l)

#def adduserstorole (l): #on user list
#    """
#    add mws users to role
#    """
#    nav("Roles")
#    g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'My webMethods Administrators'))).click()
#    g.wait.until(EC.element_to_be_clickable((By.NAME, 'Members'))).click()
#    #.//*/span[text() = 'Members']
#    x="//*[contains(@name,'editMembersButton')]"; e = g.driver.find_element(By.XPATH, x)
#    sleep(2)
#    x="//*[contains(@name,'asyncRefinedSearchGoButton')]"; e = g.driver.find_element(By.XPATH, x).click()
#    return
#    Actions actions = new Actions(g.driver)
#    actions.keyDown(Keys.LEFT_CONTROL)
#    for u in l: #multiselect
#        u = u.get('user').lower()
#        x="//*[contains(@id,'"+u+"')]"; e = g.driver.find_element(By.XPATH, x)
#        e.click()
#    actions.keyUp(Keys.LEFT_CONTROL)
#    actions.build()
#    actions.perform()
#    x="//*[@alt='Move right selected principals']"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(Keys.RETURN)


