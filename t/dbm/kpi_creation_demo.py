
import g
import mwsm as mws
import bc.g as bc
import bc.gadgets.kpi_creation as kpi
from random import choice
from time import sleep

order=[ #kpi creation flow
    'kpiName','description','process','measure','uom','kpiFormat',
    'dimension','aggregationPeriod','agg' ,'save' #,'cancel'
]

try:
        mws.navauth('bc') #login
        bc.navheadermenu('bc-label-mastheader-analytics')

        for r in range(20): #play jazz on KPI gadget

            #almost all possible inputs are range-randomized
            inputs={
                'kpiName':choice(['order amount','whatever else','dorbadug zing','zixiponga','dubaloma copra COG']),
                'description':choice(['interesting order amount','elephant tails','fortune teller','stock killer']),
                'process':'Order To Cash',
                'measure':'OrderAmount',
                #these two expose some UI BUG (show at demo)
                #'event':choice(['StepUpdate','ProcessUpdate','OrderEntry (StepUpdate)','OrderEntry (ProcessUpdate)','OrderUpdate (StepUpdate)','OrderUpdate (ProcessUpdate)']),
                #'measure':choice(['order_amount','item_count','Duration']),
                'uom':choice(['likes','hugs','kicks','tricks','blurps']),
                'kpiFormat':choice(['Dollars: \'$\'0.##','Euros: 0.## \'€\'','Milliseconds: HH:MM:SS.sss','Double: 0.00','Execution State: active/completed/suspended']),
                'dimension':['Branch','Region','Customer'],
                #'dimension':['None'],
                'aggregationPeriod':choice(['1 minute','5 minute','10 minute','30 minute','1 hour']),
                'agg':choice(['Sum','Average','Count','Maximum','Minimum','Last Value'])
            }

            kpi.clickkpisbar('create')
            kpi.create(inputs, order)   #this is 99% of navigation

            #order.reverse()             #reverse the flow
            #sleep(5)                    #just a prompt hold to see what's done
except:
    g.error()

finally:
    g.clean()

