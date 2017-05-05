
import g
import mwsm as mws
import bc.g as bc
import bc.gadgets.kpi_creation as kpi
from random import choice
from time import sleep

inputs={ #sample input needed to create KPI
    'kpiName':'order amount',
    'description':'interesting order amount',
    'process':'DBM Process',
    'event':'OrderEntry (ProcessUpdate)',
    'measure':'order_amount',
    'uom':'likes',
    'measureFormat':'Double: 0.00',
    'dimension':['Product','Region','Customer','Sales Person'],
    'interval':'15 minute',
    'agg':'Maximum'
}

order=[ #kpi creation flow
    'kpiName','description','process','event','measure','uom','measureFormat',
    'dimension','interval','agg','create','cancel'
]

try:
        mws.navauth('bc') #login
        bc.navapp('dbm')  #appspace->gadget

        for r in range(4): #play jazz on KPI gadget

            #almost all possible inputs are range-randomized
            inputs={
                'kpiName':choice(['order amount','whatever else','dorbadug zing','zixiponga','dubaloma copra COG']),
                'description':choice(['interesting order amount','elephant tails','fortune teller','stock killer']),
                'process':'DBM Process',
                #'event':'OrderEntry (ProcessUpdate)',
                #'measure':'order_amount',
                #these two expose some UI BUG (show at demo)
                'event':choice(['StepUpdate','ProcessUpdate','OrderEntry (StepUpdate)','OrderEntry (ProcessUpdate)','OrderUpdate (StepUpdate)','OrderUpdate (ProcessUpdate)']),
                'measure':choice(['order_amount','item_count','Duration']),
                'uom':choice(['likes','hugs','kicks','tricks','blurps']),
                'measureFormat':choice(['Dollars: \'$\'0.##','Euros: 0.## \'€\'','Milliseconds: HH:MM:SS.sss','Double: 0.00','Execution State: active/completed/suspended']),
                'dimension':['Product','Region','Customer','Sales Person'],
                'interval':choice(['1 minute','5 minute','10 minute','30 minute','1 hour']),
                'agg':choice(['Sum','Average','Count','Maximum','Minimum','Last Value'])
            }

            kpi.create(inputs, order)   #this is 99% of navigation
            order.reverse()             #reverse the flow
            sleep(5)                    #just a prompt hold to see what's done
except:
    g.error()

finally:
    g.clean()

