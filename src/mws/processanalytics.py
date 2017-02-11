import g #globs: driver, wait...
from g import tc
from mwsm import overlay
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

def selectvolume(p,step=False):
    """
    select a range from dropdown for process or step
    """
    #alts for process or step selector

    alt={ True:['stepVolumeValueText','step'], False:['volumeValueText','vol'] }
    x="//*/a[contains (@id, '"+alt[step][0]+"')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    if p=='All': x="//*/a[contains (@id, '"+alt[step][1]+"TotalLink')]"
    elif p=='Started': x="//*/a[contains (@id, '"+alt[step][1]+"StartLink')]"
    elif p=='In Progress': x="//*/a[contains (@id, '"+alt[step][1]+"InProgLink')]"
    elif p=='Completed': x="//*/a[contains (@id, '"+alt[step][1]+"CompLink')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()

def selectvolumes(d={'level':'proc','range':'curr','status':'All'}):
    """
    select volume for 3 different combos:
    {'level':'proc|step','range':'curr|prev','status:'All|Started|In Progress|Completed'}
    """
    tc('select volume->'+d['level']+'->'+d['range']+'->'+d['status']);
    if d['range'] == 'curr':
        level={ 'step':['stepVolumeValueText','step'],
                'proc':['volumeValueText','vol'] }
    else:
        level={ 'step':['stepVolumePreviousValueText','stepPrevious'],
                'proc':['volumePreviousValueText','volPrevious'] }
    x="//a[contains (@id, '" + level[d['level']][0] + "')]" #
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    status={'All':'TotalLink','Started':'StartedLink',
        'In Progress':'InProgressLink','Completed':'CompLink'}
    if d['level'] == 'step':
        status['Started']='StartLink'
        status['In Progress']='InProgLink'
    x="//*/a[contains (@id, '"+level[d['level']][1]+status[d['status']]+"')]"
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    overlay()

def piidlink(p='0'):
    """
    click Process Instance ID link to BC
    """
    tc('click on instance ID link for process '+p)
    x="//a[contains (@id, 'resultsTable:__row"+p+":instanceIdBCLink') or contains (@id, 'resultsTable:__row"+p+":processInstanceBCLink')]"
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    e.click()
    return e.text

def magglass(p='0'):
    """
    click magnifying glass link to BC
    """
    tc('click on magnifying glass link for process '+p)
    x="//a[contains (@id, 'resultsTable:__row"+p+":detailIconBC') or contains (@id, 'resultsTable:__row"+p+":detailBCIcon')]"
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    e.click()
    return e.text

def magglasscheck(p='0', status=True):
    """
    check status of magnifying glass link with expected status = True|False
    """
    tc('check status of magnifying glass link '+p+ ' expected ' + str(status))
    x="//a[contains (@id, 'resultsTable:__row"+p+":detailIconBC') or contains (@id, 'resultsTable:__row"+p+":detailBCIcon')]"
    e=g.wait.until(EC.presence_of_element_located((By.XPATH, x)))
    #class attr for disabled link is set (to "disabled disabled-img")
    act_status = True
    if e.get_attribute('class') == "disabled disabled-img": act_status = False
    if status != act_status:
        tc('','fail')

def navstep(step):
    #make sure to call g.focus_iframe() to focus on iframe
    tc('click step '+step+' on proc diagram')
    if step == '': #avoid blank steps
        tc('Warn: step is blank, skip')
        return
    e=g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//*/div[.='"+step+"']/preceding::div[1]/img[contains (@style,'cursor')]")))
    e.location_once_scrolled_into_view
    e.click()
    overlay()

def findsteps():
    tc('find all steps on proc diagram')
    #select all step images //*/img[contains (@style,'cursor')]
    #select all step labels (which contain their names)
    x="//*/img[contains (@style,'cursor')]/ancestor::div[2]/following-sibling::div[1]"
    es=g.driver.find_elements_by_xpath(x)
    steps=[]
    for s in es: steps.append(s.text)
    tc('found steps on proc diagram '+str(len(steps)))
    return steps

def zoomprocdiag(times):
    """
    zooms proc diagram in/reset/out times (-N/0/N)
    """
    if   times < 0: y='zoomOut'
    elif times > 0: y='zoomIn'
    else          : y='zoomReset'; times=1
    tc(y+' proc diagram '+str(times)+' times')
    for x in range(abs(times)):
        e=g.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='"+y+"']")))
        e.click()

