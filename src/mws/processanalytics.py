import g #globs: driver, wait...
from g import tc
EC=g.EC; By=g.By; Keys=g.Keys #selenium statics


def selectprocess (p):
	"""
	select a process from dropdown
	"""
	tc('select '+p)
	x="//*/select[contains (@name, 'processSelectListbox')]"; g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).send_keys(p)
	t=g.wait.until(EC.element_to_be_clickable((By.XPATH, x))).text
	print(t)
	pass
	
def	selectrange(p):
	"""
	select a range from dropdown
	"""
	pass

def	selectvolume(p):
	"""
	select a range from dropdown
	"""
	tc('select volume '+p)
	pass

def	nav(p):
	"""
	click on Process Instance ID link
	"""
	pass

