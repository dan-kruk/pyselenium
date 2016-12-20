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
    pass

def selectvolume(p):
    """
    select a range from dropdown
    """
    tc('select volume '+p)
    pass

def nav(p):
    """
    click on Process Instance ID link
    """
    pass

