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

def selectvolume(p):
    """
    select a range from dropdown
    """
    tc('select volume '+p)
    x="//*/a[contains (@id, 'volumeValueText')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    if p=='All': x="//*/a[contains (@id, 'volTotalLink')]"
    elif p=='Started': x="//*/a[contains (@id, 'volStartLink')]"
    elif p=='In Progress': x="//*/a[contains (@id, 'volInProgLink')]"
    elif p=='Completed': x="//*/a[contains (@id, 'volCompLink')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
	
def nav(p='0'):
    """
    click on Process Instance ID link
    """
    tc('nav instance '+p)
    x="//*/a[contains (@id, 'resultsTable:__row"+p+":instanceId')]"
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    e.click()
    return e.text
