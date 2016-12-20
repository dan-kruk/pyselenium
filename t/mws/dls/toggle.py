
from g import error,clean,loadenv
from mwsm import login,nav,logout
from sketch.ccs import navenv,navtab,navconfig,toggledls,togglesaml,validate,finish,deploy

try:

    x = loadenv('ccs', {'name':'BVTEnv','dls':True})

    login()
    nav('DefineEnvironments')
    navenv(x)
    navtab('Configure Servers')
    navconfig('Station Settings')
    toggledls(x.get('dls',True))
    validate()
    finish(x)
    deploy(x,'Deploy Updates')
    logout()

except:
    error()
finally:
    clean()

