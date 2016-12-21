
import g #globs: driver, wait...
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys #selenium statics


def validateid(p):
    """
    click on Process Instance ID link
    """
    tc('validate instance '+p)
    x="//*/span[contains (@id, 'instanceId')]"
    t=g.wait.until(EC.visibility_of_element_located((By.XPATH, x))).text
    if t != p:
	    tc('','fail')
    