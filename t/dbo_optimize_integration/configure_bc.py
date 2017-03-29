
import g
import mwsm as m
import mws.dashboards.g as d
import bc.g as bc

try:
        m.login()
        m.nav('bcadmin')
        bc.configure( {
            'bc-ae-url-text':'http://localhost:12503',
            'bc-ae-uname-text':'Administrator',
            'bc-ae-upass-text':'manage'
            } )
except:
    g.error()
finally:
    g.clean()

