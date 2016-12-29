import g
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys
from time import sleep

def check():

    tc('bc step summary table displayed')
    g.driver.switch_to_window(g.driver.window_handles[1]) #bc is an alt window

    x=".//*[@id='stepSummaryTable']"; e=g.wait.until(EC.presence_of_element_located((By.XPATH, x)))

    #tc('flick the movie')
    #for i in range(1,1001):
    #    g.driver.switch_to_window(g.driver.window_handles[i%2]) #bc is an alt window

