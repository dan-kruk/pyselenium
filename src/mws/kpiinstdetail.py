
import g #globs: driver, wait...
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys; Select=g.Select #selenium statics

def viewdata():
    """click view data link
    """
    #g.wait.until(EC.staleness_of(g.wait.until((EC.presence_of_element_located((By.XPATH,
    #        "//a[contains (@id,':actionMenuIcon')]"))))))
    from time import sleep
    sleep(5)
    for x in [ "//a[contains (@id,':actionMenuIcon')]",
            "//a[contains (@href,':mpViewDataLink')]" ]:
        tc('click '+x)
        g.wait.until(EC.element_to_be_clickable((By.XPATH,
            x))).send_keys(Keys.RETURN)

