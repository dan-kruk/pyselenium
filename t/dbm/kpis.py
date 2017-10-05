
import g
from g import tc
import mwsm as mws
import bc.g as bc
import bc.gadgets.kpis as kpis


"""test CRUD operations on kpis and instances
    data to work on is below
"""

expkpis = {

    'measure multi dimensional illusionary realities' :
    { 'description' : 'elephant tails','process' : 'Order To Cash','measure' : 'OrderQuantity','uom' : 'kicks','kpiFormat' : 'Dollars: \'$\'0.##',
        'dimension' : ['Branch','Region','Customer'],'aggregationPeriod' : '10 minute','agg' : 'Count' },

    'observe flat 1 dimensional world' :
    { 'description' : 'I\'am not kidding','process' : 'Order To Cash','measure' : 'OrderAmount','uom' : 'hugs\'O\'bugs','kpiFormat' : 'Execution State: active/completed/suspended',
        'dimension' : ['Region'],'aggregationPeriod' : '1 hour','agg' : 'Maximum' },

#    'we must all agree upon 1 dimensional world~1' :
#    { 'description' : 'duplicate kpi name','process' : 'Order To Cash','measure' : 'OrderAmount','uom' : 'hugs\'O\'bugs','kpiFormat' : 'Execution State: active/completed/suspended',
#        'dimension' : ['Branch','Customer'],'aggregationPeriod' : '1 hour','agg' : 'Maximum' },

}

order = [ #kpi creation input flow
    'kpiName','description','process','measure','uom','kpiFormat',
    'dimension','aggregationPeriod','agg' ,'save' #,'cancel'
]

expinstances = {

    'OrderQuantity_by_Region_Branch_and_Customer' :
    [
        [ 'Region','Branch','Customer','Last Update','Sum' ],
        [ 'North East','Washington DC','Costco',r'.+?',13.33333334326744 ],
        [ 'North East','Somewhere','absolute BoguS Co',r'.+?',13.33333334326744 ],
    ],

    'OrderValue_by_Region' :
    [
        [ 'Region','Last Update','Sum' ],
        [ 'Central',r'.+?',r'\d.\d' ],  #match any date, and reading value like digit.digit
    ],

}

#the above is test data, now run it, see comment lines for the steps and flow

try:

    #get to the kpis UI
    mws.navauth('bc')
    bc.navheadermenu('bc-label-mastheader-analytics')
    bc.spinwheel()

   #create expkpis
    for name,inputs in expkpis.items():
        kpis.clickmainmenu('create')
        kpis.create(name,inputs,order)

    #validate kpis created
    kpis.clickmainmenu('refresh')
    bc.spinwheel()

    actkpis = kpis.getdetails()

    for name in expkpis:
        desc = expkpis[name]['description']
        tc('validate kpi and details: '+name)
        if name not in actkpis:
            tc('','fail','kpi not found: '+name)
        elif desc != actkpis[name][0]:
            tc('','fail','kpi descr not match expected: ' + desc + ' actual: ' + actkpis[name][0])

    #open kpi for edit, validate all attributes, resave
    for name,inputs in expkpis.items():
        kpis.clickmenu(name,'view')
        kpis.validate(name,inputs)
        kpis.clickmenu(name,'name') #toggle-collapse instances table

    #validate kpi instances
    for name in expinstances:
        try:
            kpis.clickmenu(name,'name')
            #input('cont..')
        except:
            tc('','fail','failed to nav kpi, skip it: ' + name)
            continue
        bc.spinwheel()
        kpis.validate_inst(name, expinstances[name]) #do the needful kpi instances validation
        kpis.clickmenu(name,'name') #toggle-collapse instances table


except:
    g.error()

finally:
    g.clean()

