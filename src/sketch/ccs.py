import src.common as g #globs: driver, wait, wait3, FF, ...
EC=g.EC; By=g.By; Keys=g.Keys #selenium statics

#oh my, this is oopsy
ccs='{

"name":"",
"desc":"",
"servers":["ae","ae1","dc","mws"],
"serversl":["Analytic Engine v9.12.0.0","ae1","dc","mws"],
"template":["o4p","o4i"],
"config":{
	"default":{
		"jndi":{ "broker":"", "factory":"", "clusterurl":"" },
		"tsaurl":""
	}
	,"ae": {
		"station":{ "saml":false, "dls":false },
		"email":{ "server":"","templates":"res/templates.data" },
		"eventpub":{ "kpireadings":true,"kpistats":"false","kpinames":"..." },
		"wsactions":"res/wsactions.xml",
		"pt":{ "inputevents":"eda|mapi","modelrefresh":300000 }
	}
	,"infradc": {
		"collector":{ "pollint":2, "broker":false,"is":true },
		"umcluster":{ "statuspoll":30","auto":true }
	}
},
"hosts":["h1","h2"],
"mapservers":{ "ae":"h1","ae1":"h2","infradc":"h1" },
"mapservers":"all",
"mapendpoints": {"ae":  { "confagent":{ "protocol":"http","port":"15000", "user":"Administrator" },
			  "jmsconn":"...",
			  "wsregistry":{ "protocol":"http","port":"12503", "pass":"manage" }
			}
		 "jms": { "protocol":"nsp","port":"9000", "user":"Administrator" },
		 "mws": { "protocol":"https","port":"443", "user":"Administrator" }
		},
"mapdbpools":{ "analysis.engine.ae1":"p1","common.directory.ae1":"p2" },

}'

def create():
    """create env
    """
    #click  add env
    #enter n = g.env.get("name","AAenv")
    #enter g.env.get("desc",n)
    #click save
    #check in list

def nav():
    """
    nav to env
    """
    #n = g.env.get("name","AAenv")
    #click n link
    
def servers():
    #click Add..
    #fuzzy multi-select servers in alert->select input
    #click ok
    #check servers showup (fuzzy)
    #find env ids and names in server links
    #add to env: "servers_":{"ae":{"id":"1","name":"Analytic Engine v9.12.0.0"},"infradc":{}}
    #check green tag mark

def config():
    #loop over config keys -> href contains logicalServerID=2 -> text() = Collector Settings
        
def ccs ():
    """
    complete ccs configure thing
    """
    g.nav("db")
    g.loadenv("db")
    createdbpools()

    g.nav("ccs")
    g.loadenv("ccs")
    create()
    nav()
    servers()
    config()
    hosts()
    mapservers() #mapallservers() - quick thing
    mapendpoints()
    mapdbpools()

    g.nav("ccs")
    checkserverstatus()


