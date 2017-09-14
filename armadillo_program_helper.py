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
Examples are available in the sub directory ./examples

"""


"""
UPDATE:
- java_program to set to the new Dcoker template
- java_properties add ExecutableDocker from ['Docker']['cmd']

TO DO :
- change OneConnectorOnlyFor and SolelyConnectors for true and false
- If isMenu is false, change button to box

- update biologic type depending on a directory
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
import packages.util as u
import packages.test_yml as test
import packages.java_program as pgrm
import packages.java_properties as prop
import packages.java_file_editor as fileEdit
import packages.java_form_editor as formEdit
import os.path

author  = "J-G"
date    = (time.strftime("%d-%m-%Y"))
kword   = "armadilloWF"

def main(argv):
    armaDir     = ''
    inputFile   = ''
    biologicDir = ''

    try:
        opts, args = getopt.getopt(argv,"hy:d:b:",["help"])
    except getopt.GetoptError:
        u.print_help_exit()
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            u.print_help_exit()
        elif opt in ("-y"):
            inputFile = arg
        elif opt in ("-d"):
            armaDir = arg
        elif opt in ("-b"):
            biologicDir = arg

    if inputFile == '':
        inputFile = './inputs/repeatMasker.yml'
        print 'WARNING =>\tThe file used will be '+inputFile

    if os.path.isfile(inputFile):
        yml = yaml.safe_load("")
        with open(inputFile, 'r') as stream:
            try:
                yml = yaml.safe_load(stream)
                print('loaded')
            except yaml.YAMLError as exc:
                print(exc)
                raise SystemExit

        if yml is not None:
            # Add in yaml
            yml['author']   = author
            yml['date']     = date
            yml['kword']    = kword

            out = test.test_yml_file(yml)
            if out == "":
                u.update_command_opposites_names(yml)
                pgrm.create_program_file(yml,armaDir)
                prop.create_properties_file(yml,armaDir)
                fileEdit.create_java_editor_file(yml,armaDir)
                formEdit.create_java_editor_form(yml,armaDir)
                print('created')
            else:
                print out
                raise SystemExit
    else:
        print "File not found"
        raise SystemExit

if __name__ == '__main__':
    main (sys.argv[1:])
    """
    if len(sys.argv)>1:
        print 'yes1'
        main (sys.argv[1:])
    else:
        print 'yes2'
        u.print_help_exit()
    """
