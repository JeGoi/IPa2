#!/usr/bin/python
"""
Title:      Armadillo program helper
Author:     JG
Date:       fev 2017
Space used: 4
Variable:   varName
Function:   function_name()

Help:       Given by args -h or -Help
Input:      Yaml file with program information given by -y
Outputs:
    - Properties file
    - Program file
    - Editor form file
    - Editor java file

At the end if is test is used of the program, you will be able to export :
    - programName.properties    in armadillo/data/properties/
    - programName.java          in armadillo/src/programs/
    - programNameEditors.java   in armadillo/src/editors/
    - programNameEditors.form   in armadillo/src/editors/
For the editor, you will have to move buttons (reset,run,stop) to gets the right output (need to be fixed)

The explanation of yaml content is in this directory
Examples are available in the sub directory examples

"""


"""
TO DO :
- change OneConnectorOnlyFor and SolelyConnectors for true and false
- If isMenu is false, change button to box

- check if tooltype is added in editor form and file
- if imputs is empty
- Fixed to not move the buttons (reset/stop/run)
- Set selected in command
- Add other possibilities like list, textfield, directory files or file
- Add appication web services
- Check how inputs connector names are added in inputs
"""
import sys,os,getopt
import tarfile
import time
import yaml
import sub.util as u
import sub.test_yml as test
import sub.java_program as pgrm
import sub.java_properties as prop
import sub.java_file_editor as fileEdit
import sub.java_form_editor as formEdit
import os.path

author  = "J-G"
date    = (time.strftime("%d-%m-%Y"))
kword   = "armadilloWF"

def main(argv):
    inputFile = ''
    isTest    = False
    try:
        opts, args = getopt.getopt(argv,"hty:",["help"])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print_help()
            sys.exit()
        elif opt in ("-t"):
            isTest = True
        elif opt in ("-y"):
            inputFile = arg
    
    if inputFile == '':
        inputFile = 'examples/repeatMasker.yml'
        print 'WARNING =>\tThe file used will be '+inputFile
    
    if os.path.isfile(inputFile): 
        yml = yaml.safe_load("")
        with open(inputFile, 'r') as stream:
            try:
                yml = yaml.safe_load(stream)
                print('loaded')
            except yaml.YAMLError as exc:
                print(exc)
        
        if yml is not None:
            # Add in yaml
            yml['author']   = author
            yml['date']     = date
            yml['kword']    = kword
        
        
            out = test.test_yml_file(yml)
            if out == "":
                isTest = True
                u.update_command_opposites_names(yml)
                pgrm.create_program_file(yml,isTest)
                prop.create_properties_file(yml,isTest)
                fileEdit.create_java_editor_file(yml,isTest)
                formEdit.create_java_editor_form(yml,isTest)
                print('created')
            else:
                print out
                raise SystemExit
    else:
        print "File not found"
        raise SystemExit

def print_help():
    print   ('armadillo_parser.py [options]\n'+
            '[-h,--help]\tHelp\n'+
            '[-t,--test]\tAs test\n'+
            '[-y <input yanl file>]\tdirectory to yaml file\n')
            
if __name__ == '__main__': 
    if len(sys.argv)>1:
        main (sys.argv[1:])
    else:
        print_help()


"""

    u.update_command_opposites_names(yml)
    pgrm.create_program_file(yml)
    prop.create_properties_file(yml)
    fileEdit.create_java_editor_file(yml)
    formEdit.create_java_editor_form(yml)

    for Panel in yml['Menus']:
        if 'Panel' in Panel:
            for Tab in Panel['Panel']:
                if 'Arguments' in Tab:
                    print '>'+str(Tab['Arguments'])+'<\n'

    yml['dicti'] = 'noone'
    
    yml['dicti'] = {'noone':'coucou','prout':'zouzou'}

    print yml['dicti']
    
    for K in yml['dicti']:
        print K
        print yml['dicti'][K]
    
    for Panel in yml['Menus']:
        print "\t"+Panel['name']
        if 'Panel' in Panel:
            if len(yml['Menus'])>2: # Means need a tab
                print("\ttab")
            for Tab in Panel['Panel']:
                print("\t\tlen(tab) "+str(len(Tab)))
                print "\t\t"+Tab['tab']
                print "\t\tlt"+str(len(Tab))
                print "\t\tlp"+str(len(Panel['Panel']))

    for Panel in yml['Menus']:
        if 'Panel' in Panel:
            for Tab in Panel['Panel']:
                if 'Arguments' in Tab:
                    print '>'+str(Tab['Arguments'])+'<\n'
                    for commands in Tab['Arguments']:
                        if 'vValues' in commands['values']:
                            st = ', '.join(commands['values']['vValues'])
                            print '>'+st+'<\n'
                            print '>'+str(len(commands['values']['vValues']))+'<\n'
                            print '>'+str(commands['values']['vValues'])+'<\n'
                            #if commands['values']['vValues'] != None:
                            #    print commands['values']['max']

    for Panel in yml['Menus']:
        print Panel['name']
        if 'Panel' in Panel:
            if len(yml['Menus'])>2: # Means need a tab
                print("tab")
            for Tab in Panel['Panel']:
                print "\t"+Tab['tab']
                print "lt"+str(len(Tab))
                print "lp"+str(len(Panel['Panel']))
#                if 'Arguments' in Tab:
#                    for commands in Tab['Arguments']:
#                        if 'vValues' in commands['values']:
#                            st = ', '.join(commands['values']['vValues'])
#                            print '>'+st+'<\n'
                            #if commands['values']['vValues'] != None:
                            #    print commands['values']['max']

    for Panel in yml['Menus']:
        if 'Panel' in Panel:
            tLength = len(Panel['Panel'])
            print str(tLength)+"\n"


    mLen = 7
    boo = False
    for x in range(0,mLen):
        if mLen>1 and (mLen-x-1)%2==0 and mLen-x>1:
            print 'group ('+str(x)
            boo = True
        if x%2 != 0 and mLen>1 :
            print '\tadd gap'
            boo = True
        print '\t>Val start '+str(x)+''
        if boo:
            print '\t>Val middle'
        print '\t>Val end'
        if mLen>1 and (mLen-x-1)%2==1 and mLen-x>1:
            print ')close group'
        boo=False

    for Panel in yml['Menus']:
        pName   = Panel['name']
        if 'Panel' in Panel:
            pLength = len(Panel['Panel'])
            if pLength>2: # Means need a tabs
                print "tabs level one finaly always here"
            for Tab in Panel['Panel']:
                if len(Tab)>1: # Means need a tabs
                    print "yes"
                else:
                    print "non"

    for op in yml['FrameDefaultVariables']:
        print u.name_without_space(yml['FrameDefaultVariables'][op])
    #pgrm.createProgramsFile(yml)
    #prop.createPropertiesFile(yml)
    y = 7
    for x in range(0,y):
        if x%2==0:
            print '>GAPspace'
        if y>1 and (y-x-1)%2==0 and y-x>1:
            print 'group'+str(x)
        if x%2 != 0 and y>1 : #:
            print '>gap'
        print '>'+str(x)+''


    print yml['Program']
    print "\n\n\n\n"
    for Panel in yml['Docker']:
        print Panel
        #print Panel['dockerName']
    u.get_color(yml)
    print "\n\n\n\n"
    # Set docker Name if empty
    if not (yml['Docker']['dockerName']):
        yml['Docker']['dockerName'] = u.set_docker_name(yml)
    
    yml['FrameDefaultVariables'] = {
        "boxName":"jTextField"
    }




        print 'no docker name'
    #for paths in yml['Program']['Path']:
    #    print yml['Program']['Path'][paths]
    
    if not (yml['Program']['publication']):
        print 'no pub'
    else:
        print 'youy'
    if (yml['Program']['publication']):
        print yml['Program']['publication']
    else:
        print "COUC"
    
    for Panel in yml['Menus']:
        print Panel['name']
        if 'Panel' in Panel:
            for title in Panel['Panel']:
                if 'Arguments' in title:
                    for commands in title['Arguments']:
                        if 'values' in Arguments and Arguments['values'] is not None:
                            #print commands['values']['default']
                            for values in commands['values']:
                                print values.val()


from sub.prgmInput import make_input
from sub.prgmOutput import make_output
from sub.docker import make_docker
from sub.program import make_program
from sub.command import make_command
from sub.menu import make_menu, make_titles

    if yml['author']:
        print (yml['author']+"\n"+
               "hello")
    if yml['Program']['name']:
        print (yml['Program']['name'].replace (" ", "_"))
    for Inputs in yml['Inputs']:
        if Inputs['command2Call']:
            print Inputs['command2Call']
        else:
            print 'command2Call is empty'
    for Panel in yml['Menus']:
        print Panel['name']
        if 'Panel' in Panel:
            if len(Panel)>1: # Means need a tab
                print("tab")
            for title in Panel['Panel']:
                print "\t"+title['name']
                if 'Arguments' in title:
                    if len(title)>1: # Means need a tab in a tab
                        print("tab-tab")
                    for commands in title['Arguments']:
                        if 'values' not in commands:
                            print "\t\t yes\n\n\n"


    for x in range(0,mLen):
        if mLen%2 != 0:
            if mLen>1 and (mLen-x-1)%2==0 and mLen-x>1:
                print 'group ('+str(x)
                boo = True
            if x%2 != 0 and mLen>1 :
                print '\tadd gap'
                boo = True
            print '\t>Val start '+str(x)+''
            if boo:
                print '\t>Val middle'
            print '\t>Val end'
            if mLen>1 and (mLen-x-1)%2==1 and mLen-x>1:
                print ')close group'
            boo=False
        if mLen%2 == 0:
            if x%2 == 0:
                print 'group ('+str(x)
                boo = True
            if x%2 != 0 and mLen>1 :
                print '\tadd gap'
                boo = True
            print '\t>Val start '+str(x)+''
            if boo:
                print '\t>Val middle'
            print '\t>Val end'
            if x%2 != 0:
                print ')close group'
            boo=False


        if mLen%2 != 0:
            if x%2 == 0:
                print '\tadd gap'
            if mLen>1 and (mLen-x-1)%2==0 and mLen-x>1:
                print 'group ('+str(x)
            if x%2 != 0 and mLen>1 :
                print '\tadd gap'
            print '\t>Val end'
            if mLen>1 and (mLen-x-1)%2==1 and mLen-x>1:
                print ')close group'
        if mLen%2 == 0:
            if x%2 == 0:
                print '\tadd gap'
                print 'group ('+str(x)
            if x%2 != 0 and mLen>1 :
                print '\tadd gap'
            print '\t>Val end'
            if x%2 != 0:
                print ')close group'

    mLen = 5
    boo  = False
    for x in range(0,mLen):
        if mLen%2 != 0:
            if mLen>1 and (mLen-x-1)%2==0 and mLen-x>1:
                print 'group ('+str(x)
            if x%2 != 0 and mLen>1 :
                print '\tadd gap'
            print '\t>Val end'
            if mLen>1 and (mLen-x-1)%2==1 and mLen-x>1:
                print ')close group'
        if mLen%2 == 0:
            if x%2==0:
                print 'group ('+str(x)
            print '\t>Val end'
            if x%2 == 0 and mLen>1 :
                print '\tadd gap'
            if x%2 != 0:
                print ')close group'


"""
