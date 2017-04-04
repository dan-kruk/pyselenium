
import g
from g import tc
EC=g.EC; By=g.By
import mwsm as m

def search(text):
    """
    search for text in search widgets (almost in all)
    """
    tc('search '+text)
    g.wait.until(EC.element_to_be_clickable((By.XPATH,\
        "//input[contains (@name,'keywordsTextInput')]"))).send_keys(text)
    g.wait.until(EC.element_to_be_clickable((By.XPATH,\
        "//button[contains (@name,'impleSearchGoButton')]"))).click()
    m.overlay_handler()

