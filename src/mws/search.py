
import g
from g import tc
EC=g.EC; By=g.By
from selenium.common.exceptions import StaleElementReferenceException as stale
from time import sleep

def search(text):
    """
    search for text in search widgets (almost in all)
    """
    tc('search '+text)
    g.wait.until(EC.element_to_be_clickable((By.XPATH,\
        "//input[contains (@name,'keywordsTextInput')]"))).send_keys(text)
    tc('wait overlay gone') #handle overlay prog bar
    g.driver.find_element(By.XPATH,\
        "//button[contains (@name,'impleSearchGoButton')]").click()
    o=g.wait.until(EC.presence_of_element_located((By.XPATH,\
        "//*[contains(@id,'overlay')]")))
    g.wait.until(EC.staleness_of(o))
    sleep (.5) #some div overlays in chrome
	#tc('check under overlay area')
    #x="//*[text()='No matches found']";
    #g.wait.until(EC.visibility_of_element_located((By.XPATH, x)))

