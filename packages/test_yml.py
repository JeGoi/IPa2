#!/usr/bin/env python
"""
Title   : Yml file tester
Author  : JG
Date    : fev 2017
Objet   : script to validate yml file
in      : get infos from yml
out     : return out as stderr, out is empty if everything is ok
"""
import sys,os
import yaml
import util as u


war = 'WARNING : '
ne  = ' (and not empty)\n'
# ===============================================
#     FUNCTION to test yml
# ===============================================
def test_yml_file(yml):
    out = ""
    out = test_general_structure_file(out,yml)
    return out

#
# Tests for imput file
#
def test_general_structure_file(out,yml):
    out = ''
    if 'Program' not in yml:
        out = "Yaml file has no Menus"
    else:
        out = test_program(out,yml)
    if 'Docker' not in yml:
        print war+"Docker is not used for this program"
    else:
        out = test_docker(out,yml)
    # Reflechir si il n'y a pas d'inputs
    if 'Inputs' not in yml:
        out = "Yaml file has no Inputs"
    else:
        out = test_inputs(out,yml)
    if 'Outputs' not in yml:
        out = "Yaml file has no Outputs"
    else:
        out = test_outputs(out,yml)
#    if 'Menus' not in yml:
#        out += "Yaml file has no Menus"
#    else:
#        out += test_menus(out,yml)
        
    # if Program is here and not empty
    # if Docker is here (warning if not)
    # if Imputs is here and not empty
    # if Outputs is here and not empty
    # if Menu is here and not empty
    return out
    
#
# Test zone
#

def test_program(out,yml):
    op = 'Program'
    obligations = ['name','exitValue','executablePaths','menu','numImputs']
    warnings    = ['outputsPath','website','helpSupplementary','publication','desc','webServices','outputFilesFromOutputPath']

    for o in obligations:
        if o not in yml[op] or yml[op][o] == "" or yml[op][o] == None:
            out += 'Yaml '+op+' part needs "'+o+'"'+ne
    for w in warnings:
        if w not in yml[op]:
            print war+'Yaml '+op+' part may need "'+w+'"'
            yml[op][w]=""

    if "numInputs" in yml[op]:
        v = yml[op]['numInputs']
        if v < 1 and v > 3:
            print war+'Yaml Program part numInputs is setted to default 1'
            yml[op]['numInputs'] = 1
    if "executablePaths" in yml[op]:
        if "ExecutableLinux" not in yml[op]['executablePaths']:
            print war+'Yaml '+op+' executablePaths may need "ExecutableLinux"'
        if "ExecutableMacOSX" not in yml[op]['executablePaths']:
            print war+'Yaml '+op+' executablePaths may need "ExecutableMacOSX"'
        if "Executable" not in yml[op]['executablePaths']:
            print war+'Yaml '+op+' executablePaths may need "Executable" for windows'
    # the number of Inputs [1,3] If not set : default 1 (warnings)
    # all path (linux,mac,win) have a path (warnings)
    # web info exists (warnings)
    # help info exists (warnings)
    return out
    
def test_docker(out,yml):
    op = 'Docker'
    obligations = ['imageName','cmd']
    warnings    = ['dockerName','rmks','copyDockerFilesDir2SharedFolder','sharedFolder']
    
    for o in obligations:
        if o not in yml[op] or yml[op][o] == "" or yml[op][o] == None:
            out += 'Yaml '+op+' part needs "'+o+'"'+ne
    for w in warnings:
        if w not in yml[op]:
            print war+'Yaml '+op+' part may need "'+w+'"'
    
    #if 'dockerName' in yml[op]:
    #    if yml[op]['dockerName'] == "" or yml[op]['dockerName'] == None:
    #        print war+'Yaml '+op+' part may need "dockerName"'
    #        yml[op]['dockerName'] = yml[op]['imageName']
    # Image Name is define and not empty
    # Command is define and not empty
    # Docker Name is define and not empty, default = Image Name
    return out

def test_inputs(out,yml):
    op = 'Inputs'
    obligations = ['connectorText','type','connector','extension']
    warnings    = ['OneConnectorOnlyFor','SolelyConnectors','command2Call',]
    
    x=1
    for i in yml[op]:
        
        for o in obligations:
            if o not in i or i[o] == "" or i[o] == None:
                out += 'Yaml '+op+' number '+str(x)+' part needs "'+str(o)+'"'+ne

        for w in warnings:
            if w not in i:
                print war+'Yaml '+op+' number '+str(x)+' part may need "'+str(w)+'"'
        
        if "type" in i:
            v = i['type']
            if not u.isBiologicType(v):
                print war+'Yaml '+op+' number '+str(x)+' Type is not in Armadillo biologic options "'+v+'"'
                
        if "connector" in i:
            v = i['connector']
            if v < 2 and v > 4:
                print war+'Yaml Inputs number '+str(x)+' connector is setted to default 2 \n'
                i['numInputs'] = 2
        
        if 'OneConnectorOnlyFor' in i and i['OneConnectorOnlyFor'] != '' and i['OneConnectorOnlyFor'] != None:
            if str(i['connector']) not in str(i['OneConnectorOnlyFor']):
                out += war+'Yaml Inputs number '+str(x)+' connector and OneConnectorOnlyFor don\'t match \n'
        
        if 'SolelyConnectors' in i  and i['SolelyConnectors'] != '' and i['SolelyConnectors'] != None:
            if str(i['connector']) not in str(i['SolelyConnectors']):
                out += war+'Yaml Inputs number '+str(x)+' connector and SolelyConnectors don\'t match \n'
        
        x+=1
    # Name is define and not empty
    # Num is define and in [2,4] If not set : default 2 (warnings)
    # Type is define and not empty and match with a biologic type
    # extension is define and not empty
    # If solely or only are define, yes: check if same as Num
    return out
    
def test_outputs(out,yml):
    op = 'Outputs'
    obligations = ['connectorText','type','extension']
    warnings    = ['command2Call']
    
    x=1
    for i in yml[op]:
        
        for o in obligations:
            if o not in i or i[o] == "" or i[o] == None:
                out += 'Yaml '+op+' number '+str(x)+' part needs "'+str(o)+'"'+ne
        for w in warnings:
            if w not in i:
                print war+'Yaml '+op+' number '+str(x)+' part may need "'+str(w)+'"'

        if "type" in i:
            v = i['type']
            if not u.isBiologicType(v):
                print war+'Yaml '+op+' number '+str(x)+' Type is not in Armadillo biologic options "'+v+'"'
        
        x+=1
    # Name is define and not empty
    # Type is define and not empty and match with a biologic type
    # extension is define and not empty
    return out

def test_menus(out,yml):
    op = 'Menus'
    obligations = ['name','isMenu','isTab']
    warnings    = ['help']

    x   = 1
    p   = 0
    isM = 0
    least1withPanel = False
    for i in yml[op]:
        
        for o in obligations:
            if o not in i or i[o] == "" or i[o] == None:
                out += 'Yaml '+op+' number '+str(x)+' part needs "'+str(o)+'"'+ne
        for w in warnings:
            if w not in i:
                print war+'Yaml '+op+' number '+str(x)+' part may need "'+str(w)+'"'

        if "isTab" in i:
            v = i['isTab'].lower()
            if v != 'true' or v != 'false':
                print war+'Yaml '+op+' number '+str(x)+' isTab need to be true or false"'+w+'"'

        if "isMenu" in i:
            v = i['isMenu'].lower()
            if v != 'true' or v != 'false':
                print war+'Yaml '+op+' number '+str(x)+' isMenu need to be true or false"'+w+'"'
            
            if v == 'true':
                isM +=1
        if 'Panel' in i:
            p += 1
        
        x+=1
    
    if p == 0 and isM>0:
        out += 'Yaml '+op+' organization is not good. You have more than one option in your menu but none with a panel of commands inside'
        
    # Name is define and not empty
    # Panel are >= 1
    # Test if oppositeTo exist and is unique = add the var name and values like dictionnay Need to be a list

    return out

def test_titles(out,yml,x):
    op = 'Panels'
    obligations = ['tab','Arguments']
    for i in yml[op]:
        
        for o in obligations:
            if o not in i and (i[o] == "" or i[o] == None):
                out += 'Yaml '+op+' number '+str(x)+' part needs "'+str(o)+'"'+ne
        for w in warnings:
            if w not in i:
                print war+'Yaml '+op+' number '+str(x)+' part may need "'+str(w)+'"'

    # Number of name commands >= 1
    # tab is define and not empty
    # Arguments are >= 1
    # test if initials menu is unique
    return out

def test_command(out,yml,x):
    op = 'Arguments'
    obligations = ['name','cType','tooltip']
    warnings    = ['shortName','label','oppositeTo','parentOf','selected','cHelp','values']
    
    x=1
    for i in yml[op]:
        
        for o in obligations:
            if o not in i and (i[o] == "" or i[o] == None):
                out += 'Yaml '+op+' number '+str(x)+' part needs "'+str(o)+'"'+ne
        for w in warnings:
            if w not in i:
                print war+'Yaml '+op+' number '+str(x)+' part may need "'+str(w)+'"'

        if "type" in i:
            v = i['type']
            if not u.isBiologicType(v):
                print war+'Yaml '+op+' number '+str(x)+' Type is not in Armadillo biologic options" '+w+'"'
        
        x+=1
#    Name is define and not empty
#    typeButton is define and not empty
#    ValueType is define and not empty
#    vDefault Value is define and not empty
#    Test if parentOf exist and is unique = add the var name and values
#    Test if oppositeTo exist and is unique = add the var name and values like dictionnay Need to be a list
#    for Panel in yml['Menus']:
#        if 'Panel' in Panel:
#            for Tab in Panel['Panel']:
#                if 'Arguments' in Tab:
#                    for commands in Tab['Arguments']:
#                        for child in tabChild:
#                            if child == commands['name']:

    return out

def test_values(out,yml,x):
    op = 'values'
    obligations = ['vType']
    for o in obligations:
        if o not in i and (i[o] == "" or i[o] == None):
            out += 'Yaml '+op+' number '+str(x)+' part needs "'+str(o)+' "'+ne
    
#    vType   : dou
#    vType   : list
#    test_values_numbers(out,yml)
#    test_values_list(out,yml)
    return out

def test_values_numbers(out,yml):
#    vDefault: 1
#    vMin    :
#    vMax    :
#    vJump   : 1
    
    return out

def test_values_list(out,yml):
#    vDefault: ps
#    vValues :
#            - ps
#            - hpgl
#            - hp7470
#            - hp7580
    
    return out
