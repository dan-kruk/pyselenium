
import g #globs: driver, wait...
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys; Select=g.Select #selenium statics

def viewdata():
    """click view data link
    """
    for x in [ "//a[contains (@id,':actionMenuIcon')]",
            "//a[contains (@href,':mpViewDataLink')]" ]:
        g.wait.until(EC.element_to_be_clickable((By.XPATH,
            x))).send_keys(Keys.RETURN)

