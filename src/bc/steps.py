import g
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys
from time import sleep

def check():
    tc('bc step summary table displayed')
    x="//*[@id='stepSummaryTable']"
    sleep(3)
    e=g.wait.until(EC.presence_of_element_located((By.XPATH, x)))
