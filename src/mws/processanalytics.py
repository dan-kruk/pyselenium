import g #globs: driver, wait...
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys #selenium statics
from selenium.webdriver.support.select import Select
from time import sleep


def selectprocess (p):
    """
    select a process from dropdown
    """
    tc('select '+p)
    x="//*/select[contains (@name, 'processSelectListbox')]"
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    select=Select(e)
    select.select_by_visible_text(p)
    sleep(2) #ugly page mutation
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    select=Select(e)
    if select.first_selected_option.text != p:
        tc('','fail')
    #for opt in select.all_selected_options:
    #    print(opt.text)
    #for opt in select.options:
    #    print(opt.text)

def selectrange(p):
    """
    select a range from dropdown
    """
    tc('select '+p)
    x="//*/select[contains (@name, 'dateRangeDropdown')]"
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    select=Select(e)
    select.select_by_visible_text(p)
    sleep(2) #ugly page mutation
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    select=Select(e)
    if select.first_selected_option.text != p:
        tc('','fail')

def selectprocessvolume(p):
    """
    select a process volume option
    """
    tc('select process volume '+p)
    x="//*/a[contains (@id, 'volumeValueText')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    if p=='All': x="//*/a[contains (@id, 'volTotalLink')]"
    elif p=='Started': x="//*/a[contains (@id, 'volStartLink')]"
    elif p=='In Progress': x="//*/a[contains (@id, 'volInProgLink')]"
    elif p=='Completed': x="//*/a[contains (@id, 'volCompLink')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
	
def processpiidlink(p='0'):
    """
    click Process Instance ID link to BC
    """
    tc('click on instance ID linkfor process '+p)
    x="//*/a[contains (@id, 'resultsTable:__row"+p+":instanceIdBCLink')]"
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    sleep(1)  #element obscured issue on edge
    e.click()
    return e.text

def processmagglasslink(p='0'):
    """
    click magnifying glass link to BC
    """
    tc('click on magnifying glass link for process '+p)
    x="//*/img[contains (@id, 'resultsTable:__row"+p+":detailIconBC')]"
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    sleep(1)  #element obscured issue on edge
    e.click()
    return e.text

def selectstepinmodel():
    """
    click on Service Task 1 step
    """
    tc('click on Service Task 1 step')
    x="//*/img[contains(@src, 'images/icons/')]"
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    e.click()

def selectstepvolume(s):
    """
    select a step volume option
    """
    tc('select step volume '+s)
    x="//*/a[contains (@id, 'stepVolumeValueText')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    if s=='All': x="//*/a[contains (@id, 'stepTotalLink')]"
    elif s=='Started': x="//*/a[contains (@id, 'stepStartedLink')]"
    elif s=='In Progress': x="//*/a[contains (@id, 'stepInProgressLink')]"
    elif s=='Completed': x="//*/a[contains (@id, 'stepCompLink')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()

def steppiidlink(s='0'):
    """
    click Process Instance ID link to BC
    """
    tc('click on instance ID link for step '+s)
    x="//*/a[contains (@id, 'resultsTable:__row"+s+":processInstanceBCLink')]"
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    sleep(1)  #element obscured issue on edge
    e.click()
    return e.text

def stepmagglasslink(s='0'):
    """
    click magnifying glass link to BC
    """
    tc('click on magnifying glass link for step '+s)
    x="//*/img[contains (@id, 'resultsTable:__row"+s+":detailBCIcon')]"
    #MUST VALIDATE HERE THAT THE MAGNIFYING GLASS LINK TO BUSINESS CONSOLE IS DISABLED
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    sleep(1)  #element obscured issue on edge
    e.click()
    return e.text
	
	