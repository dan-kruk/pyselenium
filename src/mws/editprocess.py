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
    #tc('check saved change')
    #se = g.wait.until(EC.element_to_be_clickable((By.XPATH, sx))).is_selected()
    #tc('saml is '+str(se))
    #assert s is se


