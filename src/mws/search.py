
import g
from g import tc
EC=g.EC; By=g.By
from selenium.common.exceptions import StaleElementReferenceException as stale
from time import sleep

def search(text):
    """search for text in search widgets (almost in all)"""
    tc('search '+text)
    x="//*[contains (@name,'keywordsTextInput')]";
    g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(text)
    x="//*[contains (@name,'impleSearchGoButton')]"
    #g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).click()
    g.driver.find_element(By.XPATH, x).click()
    tc('wait overlay gone') #handle overlay prog bar
    x="//*[contains(@id,'overlay')]"; 
    o=g.wait.until(EC.presence_of_element_located((By.XPATH, x)))
    g.wait.until(EC.staleness_of(o))
    sleep (1)
	#tc('check under overlay area')
    #x="//*[text()='No matches found']";
    #g.wait.until(EC.visibility_of_element_located((By.XPATH, x)))

