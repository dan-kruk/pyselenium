import g
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys
from selenium.common.exceptions import StaleElementReferenceException as stale
from time import sleep


def toggleexecution(s=True):
    """enable / disable execution for model"""
    tc('enable execution for model')
    x="//*[contains (@id, 'executionEnabledCheck') and @type='checkbox']"
    se=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    s0=se.is_selected()
    if s is not s0:
        tc('toggle execution enabled from '+str(s0)); se.click()
        tc('click save')
        x="//*[contains (@id, 'saveButton')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    else: 
        tc('click cancel')
        x="//*[contains (@id, 'htmlCommandButton')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
	#tc('check saved change')
    #se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx))).is_selected()
    #tc('saml is '+str(se))
    #assert s is se

def toggleanalysis(s=True):
    """enable / disable analysis for model"""
    tc('enable analysis for model')
    x="//*[contains (@id, 'trackingEnabledCheck') and @type='checkbox']"
    se=g.wait.until(EC.element_to_be_clickable((By.XPATH, x)))
    s0=se.is_selected()
    if s is not s0:
        tc('toggle execution enabled from '+str(s0)); se.click()
        tc('click save')
        x="//*[contains (@id, 'saveButton')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
    else: 
        tc('click cancel')
        x="//*[contains (@id, 'htmlCommandButton')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)

def toggle_execution_analysis (x={}):
    """control execution and analysis enabled flags"""

    d=[x.get('execution',True),x.get('analysis',True)]

    tc('checkbox presence')
    sx="//*[contains (@id, 'executionEnabledCheck') and @type='checkbox']"; se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx)))
    for c,x in zip(d,['executionEnabledCheck','trackingEnabledCheck']):
        sx="//*[contains (@id, '"+x+"') and @type='checkbox']"; se = g.driver.find_element(By.XPATH, sx); s0=se.is_selected()
        if c is not s0:
            tc('toggle '+x+' '+str(c)+' from '+str(s0)); se.click()

    tc('click save')
    x="//*[contains (@id, 'saveButton')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)

def check_execution_analysis (x={}):
    """validate execution and analysis enabled flags"""

    d=[x.get('execution',True),x.get('analysis',True)]

    tc('check saved change')
    sx="//*[contains (@id, 'executionEnabledCheck') and @type='checkbox']"; se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx)))
    for c,x in zip(d,['executionEnabledCheck','trackingEnabledCheck']):
        sx="//*[contains (@id, '"+x+"') and @type='checkbox']"; se = g.driver.find_element(By.XPATH, sx); s0=se.is_selected()
        tc('act/exp '+x+' '+str(s0)+str(c))
        assert c is s0

    tc('click save')
    x="//*[contains (@id, 'saveButton')]"; g.driver.find_element(By.XPATH, x).send_keys(Keys.RETURN)
