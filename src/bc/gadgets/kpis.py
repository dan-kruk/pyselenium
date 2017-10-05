import g
from g import tc
import re

EC=g.EC; By=g.By; Keys=g.Keys; AC=g.ActionChains

def clickmainmenu(item='create'):
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

def getdetails():
    """ret: kpi detals {}
    """
    name = g.driver.find_elements_by_xpath(
        "//div[@ng-repeat='kpi in kpiAssets']//div[@class='hint--bottom inline ng-binding ng-scope']")
    desc = g.driver.find_elements_by_xpath(
        "//div[@ng-repeat='kpi in kpiAssets']//div[@class='hint--right inline ng-binding ng-scope']")
    tc('pulled kpi details: ' + str(len(name)))
    kpis = {}; i = 0
    for n,d in zip(name,desc):
        tmp = n.text
        while tmp in kpis:  #make up duplicate KPI names with ~NN suffix
            i+=1; tmp = n.text + '~' + str(i)
        kpis[tmp] = [d.text] #pack into {kpiname : [desc,future kpi props...]}
        #print(x.get_attribute('data-hint'));
        #print(n.text);
        #print(d.text);
        #print(kpis)
    return kpis

def create( #params with defaults
    name = 'my abc kpi',
    inputs = {
        'description' : 'elephant tails','process' : 'Order To Cash',
        'measure' : 'OrderQuantity','uom' : 'kicks','kpiFormat' : 'Dollars: \'$\'0.##',
        'dimension' : ['Branch','Region','Customer'],'aggregationPeriod' : '10 minute','agg' : 'Count'

    },
    order = [
        'kpiName','description','process','measure','uom','kpiFormat',
        'dimension','aggregationPeriod','agg','save','cancel'
    ] ):

    """
    create kpi described by @inputs using arbitrary navigation flow @order
    think the kpi create UI business navigation flow
    """

    inputs['kpiName'] = name

    for k in order:

        tc('input '+k+' : '+str(inputs.get(k,k+' element')))

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

        #the rest inputs are uniform named
        e = g.wait.until(EC.element_to_be_clickable((By.ID,
            k+'Input')))
        em = e.get_attribute('id')[:-len('Input')]
        if em in ['kpiName','description','uom']:
                e.clear()
                e.send_keys(re.sub('~\d+$','',inputs[k]))  #cutoff ~NN prefix for dup kpi names
        if em in [
                'process','measure','kpiFormat','aggregationPeriod','agg'
                ]:
                e.click()
                #print('==='+inputs[k])
                g.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,
                    inputs[k]))).click()

def clickmenu(kpiname,action='view'):
    """click on kpi @name menu @action {name,view,delete}
    """
    tc('click '+action+' kpi: '+kpiname)
    name = "//div[@class='hint--bottom inline ng-binding ng-scope' and @data-hint='" + kpiname + "']"
    root = name + "/../../../../../../table/preceding-sibling::div//"
    menu = root + "span[@class='dropdown']"
    item = root + "a[contains(@data-ng-click,'viewKpi')]"

    for xp in [ name,menu,item ]:
        #print(xp)
        g.wait.until(EC.element_to_be_clickable((By.XPATH, xp))).click()
        if action == 'name': break #click just kpi name

def validate(name,inputs):
    """validate kpi edit UI for kpi @name with @inputs{}, variation of create()
    """
    order = [
        'kpiName','description','process','measure','uom','kpiFormat',
        'dimension','aggregationPeriod','agg','cancel'
    ]

    inputs['kpiName'] = name

    for k in order:

        tc('validate '+k+' : '+str(inputs.get(k,k+' element')))

        #buttons
        if k == 'save':
            g.wait.until(EC.element_to_be_clickable((By.XPATH,
                "//button[text()='Save']"))).click()
            continue
        if k == 'cancel':
            g.wait.until(EC.element_to_be_clickable((By.XPATH,
                "//button[text()='Cancel']"))).click()
            continue

        expected = inputs.get(k,'unknown element in @inputs')
        actual = None

        if k == 'dimension':
            expected = ",".join(str(x) for x in expected) #list to string
            ex = g.driver.find_elements_by_xpath(
                    "//span[@class='dim-selected-input ng-binding ng-scope']")
            actual = ''
            for x in ex: actual+=x.text
        elif k in ['kpiName','description','uom']:
            e = g.wait.until(EC.element_to_be_clickable((By.ID,
                k+'Input')))
            actual = e.get_attribute('value')
        ##elif k in ['author', 'lastUpdated']: add these later
        else:
            e = g.wait.until(EC.element_to_be_clickable((By.ID,
                k+'Input')))
            actual = e.text

        if actual != expected:
            tc('','fail','expected: \'' + expected + '\' actual: \'' + actual + '\'')

def validate_inst(name,inputs):
    """validate kpi @name instances table for match with @inputs[[]] rows
    """
    tc('validating ' + str(len(inputs)) + ' inst for kpi: ' + name)

    #whole inst table with header row for kpi name
    xp = "//div[@id='kpi-cs-grid-" + name + "']//div[contains(@class,'slick-cell')] | //div[@id='kpi-cs-grid-" + name + "']//span"
    #print(xp)
    g.wait.until(EC.element_to_be_clickable((By.XPATH, xp))) #table is delayed to load
    ex = g.driver.find_elements_by_xpath(xp)
    tc('searching in inst table points: ' + str(len(ex)))

    for row in inputs:

        expected = ','.join(str(x) for x in row)+',' #clamp exp cols in row
        regex = re.compile(expected)
        tc('validate row: ' + expected)

        #print('>> ' + expected)
        #print(len(ex),len(row))
        notfound = True; prev = 0
        for i in range(0,len(ex)+1,len(row)): #iter actual columns with exp row size lag
            #print(i,prev)
            actual = ''
            for x in range(prev,i): #form actual row
                actual+=ex[x].text+','
            prev = i
            #print('<< ' + actual)
            if regex.match(actual):
                notfound = False
                break #found match - skip the rest of the table
        if notfound:
            tc('','fail','expected matching row not found: \'' + expected + '\'')

