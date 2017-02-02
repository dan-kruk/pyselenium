import g
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys

def focus():
    g.focus(1) #bc is an alt tab-window
    e=g.wait20.until(EC.presence_of_element_located((By.XPATH,
        ".//*[@id='stepSummaryTable']")))

def close():
    g.driver.close() #close tab-window
    g.focus() #back to main window
    g.driver.refresh() #it'd be stale overwise


    #tc('flick the movie')
    #for i in range(1,1001):
    #    driver.switch_to_window(driver.window_handles[i%2]) #bc is an alt window

