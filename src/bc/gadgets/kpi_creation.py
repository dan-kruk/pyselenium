import g
from g import tc

EC=g.EC; By=g.By; Keys=g.Keys; AC=g.ActionChains


def clickkpisbar(item='create'):
    """click + icon on KPIs list bar
    """
    tc('click '+item+' on kpibar')
    xp = { 'create':'Create KPI',
            #this is menu 'settings':"//div[@data-hint='']/...']",
            'refresh':'Refresh',
            'expand':'Expand/Collapse View'
            }
    g.wait.until(EC.element_to_be_clickable((By.XPATH,
        "//div[@data-hint='"+xp[item]+"']/img"))).click()

def create(

    inputs={
    'kpiName':'order amount',
    'description':'interesting order amount',
    'process':'Order To Cash',
    'measure':'OrderAmount',
    'uom':'likes',
    'kpiFormat':'Double: 0.00',
    'dimension':['Product'],
    'aggregationPeriod':'15 minute',
    'agg':'Maximum'
    },

    order=[
    'kpiName','description','process','measure','uom','kpiFormat',
    'dimension','aggregationPeriod','agg','save','cancel'
    ]):


    """
    create kpi described by @inputs using arbitrary navigation flow @order
    think the gadget business navigation flow
    """

    for k in order:

        tc('meet '+k+' : '+str(inputs.get(k,'whitespace - missing inpit to click!')))

        #dimensions
        if k == 'dimension':
            g.wait.until(EC.element_to_be_clickable((By.ID,
                'dimensionSelectButton'))).click()
            ex = g.driver.find_elements_by_xpath( #what is selected
            "//*[@class='glyphicon glyphicon-remove dim-selected-item-remove']")
            for e in ex: #del 'em
                e.click()
            for e in inputs[k]:
                tc('  dim '+e)
                g.wait.until(EC.element_to_be_clickable((By.ID,
                    'dimOptsBtn'))).click()
                g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,
                    e))).click()
            continue

        #buttons
        if k == 'save':
            g.wait.until(EC.element_to_be_clickable((By.XPATH,
                "//button[text()='Save']"))).click()
            continue
        if k == 'cancel':
            g.wait.until(EC.element_to_be_clickable((By.XPATH,
                "//button[text()='Cancel']"))).click()
            continue

        #the rest inputs are uniform named (I wish all UI guts impl consistent like that)
        e = g.wait.until(EC.element_to_be_clickable((By.ID,
            k+'Input')))
        em = e.get_attribute('id')[:-len('Input')]
        if em in ['kpiName','description','uom']:
                e.clear()
                e.send_keys(inputs[k])
        if em in [
                'process','measure','kpiFormat','aggregationPeriod','agg'
                ]:
                e.click()
                print('==='+inputs[k])
                g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,
                    inputs[k]))).click()


