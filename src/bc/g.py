import g
from g import tc
#from time import sleep

EC=g.EC; By=g.By; Keys=g.Keys

def focus():
    tc('focus on business console')
    #g.wait.until(EC.number_of_windows_to_be(2))
    g.focus(1) #bc is an alt tab-window
    g.wait.until(EC.presence_of_element_located((By.XPATH,
        "//div[@id='stepSummaryTable']")))

def close():
    #sleep(5) #tmp so page seen on demo
    tc('close business console tab/window')
    g.driver.close() #close tab-window
    g.focus()
    g.driver.refresh() #it'd be stale overwise
    g.focus_main() #back to main window

def validatepi(pid):
    """
    validate instance details by pid
    """
    tc('located pid='+pid)
    g.wait20.until(EC.presence_of_element_located((By.XPATH,
        "//td[.='"+pid+"']")))

