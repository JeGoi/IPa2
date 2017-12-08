#!/usr/bin/env python
"""
Title   : Java program file
Author  : JG
Date    : dec 2016
Objet   : script to create Propertie File Program
in      : get infos from yml
out     : print infos in properties file
"""
import sys,os
import yaml
import util as u
from random import randint

# ===============================================
#     FUNCTION create Java File Properties
# in  : get infos from csv
# out : print infos in java file
# ===============================================
def create_properties_file(yml,armaDir):
    progDir     = u.define_prop_path(armaDir)
    filename    = progDir+""+u.get_program_name(yml)+".properties"
    out = open(filename, 'w')
    out.write("#Armadillo Workflow Platform 1.1 (c) Etienne Lord, Mickael Leclercq, Alix Boc,  Abdoulaye Banire Diallo, Vladimir Makarenkov"+
                "\n#"+yml['author']+
                "\n#"+yml['date']+
                "\n#Pgrogram info"+
                "\nName= "+yml['Program']['name']+
                "\nClassName= programs."+u.get_program_name(yml)+""+
                "\nEditorClassName= editors."+u.get_program_name(yml)+"Editors"+
                "\ndebug= false"+
                "\nfilename= C\:\\armadillo2\\data\\properties\\"+u.get_program_name(yml)+".properties")
    for paths in yml['Program']['executablePaths']:
        out.write("\n"+paths+"="+yml['Program']['executablePaths'][paths])

    out.write("\nHelpSupplementary=")
    if yml['Program']['helpSupplementary']:
        out.write(yml['Program']['helpSupplementary'])

    out.write("\nPublication= ")
    if yml['Program']['publication']:
        out.write(yml['Program']['publication'])

    out.write("\nDescription= ")
    if yml['Program']['desc']:
        out.write(yml['Program']['desc'])

    ObjectID = randint(1000000000,9999999999)
    out.write("\nObjectID="+u.get_program_name(yml)+"_"+str(ObjectID)+""+
                "\nObjectType=Program"+
                "\nNoThread=false")

    out.write("\nType=")
    if yml['Program']['menu']:
        out.write(yml['Program']['menu'])

    out.write("\nNormalExitValue=")
    if yml['Program']['exitValue'] or yml['Program']['exitValue'] == 0:
        out.write(str(yml['Program']['exitValue']))

    out.write("\nVerifyExitValue=")
    if yml['Program']['exitValue']:
        out.write('true')
    else:
        out.write('false')

    out.write("\nWebServices=")
    if yml['Program']['webServices']:
        out.write(yml['Program']['webServices'])

    out.write("\nWebsite=")
    if yml['Program']['website']:
        out.write(yml['Program']['website'])

    # Color options
    color = u.get_color(yml)
    out.write("\ncolorMode    = "+color+""+
              "\ndefaultColor = "+color+"")

    # Inputs types
    out.write("\n#INPUTS TYPES")
    if len(yml['Inputs']) > 0:
        o = ""
        s = ""
        for op in yml['Inputs']:
            if op['type']:
                out.write("\nInput"+op['type']+"=Connector"+str(op['connector']))

            if op['OneConnectorOnlyFor']:
                if o == "":
                    o = str(op['OneConnectorOnlyFor'])
                else:
                    t = str(op['OneConnectorOnlyFor'])
                    if t not in o:
                        o = o+","+t
            if op['SolelyConnectors']:
                if s == "":
                    s = str(op['SolelyConnectors'])
                else:
                    t = str(op['SolelyConnectors'])
                    if t not in o:
                        s = s+","+t
        # Inputs options
        if o != "" or s != "":
            out.write("\n#INPUTS OPTIONS")
        if o != "":
            out.write("\nOneConnectorOnlyFor="+o)
        if s != "":
            out.write("\nSolelyConnectors= "+s)
    else:
        out.write("\nNO IMPUTS ??\n")

    # Inputs Names
    out.write("\n#INPUTS Connector text")
    tab = ('2','3','4')
    for t in tab:
        c = ""
        if len(yml['Inputs']) > 0:
            for op in yml['Inputs']:
                o = str(op['connector'])
                if t in o or "true" in o:
                    if c == "":
                        c = str(op['connectorText'])
                    else:
                        s = str(op['connectorText'])
                        if s not in c:
                            c = c+", "+s
        if c != "":
            out.write("\nConnector"+t+"= "+c)

    # Number of inputs
    out.write("\nnbInput= ")
    if yml['Program']['numImputs']:
        out.write(str(yml['Program']['numImputs']))

    # Outputs values
    out.write("\n#OUTPUTS OPTIONS"+
              "\nConnector0Output=True"+
              "\nOutputResults=Connector0"+
              "\nOutputOutputText=Connector0")
    if len(yml['Outputs']) > 0:
        for op in yml['Outputs']:
            if op['type']:
                out.write("\nOutput"+op['type']+"=Connector0")

    # Default Values
    out.write("\n#DEFAULT VALUES"+
              "\ndefaultPgrmValues=")
    for Panel in yml['Menus']:
        pNameS = u.name_without_space(Panel['name'])
        if 'Panel' not in Panel:
            # Means default option
            out.write(""+pNameS+"<>true<>")
        else:
            for Tab in Panel['Panel']:

                if 'Arguments' in Tab:
                    tName   = Tab['tab']
                    for Arguments in Tab['Arguments']:
                        cName   = Arguments['name']
                        if 'values' in Arguments and \
                            Arguments['values'] is not None and \
                            Arguments['values']['vType'] is not None:
                            vType   = Arguments['values']['vType']
                            v       = u.create_value_name(pNameS,tName,cName,vType)
                            vDef    = str(Arguments['values']['vDefault'])
                            out.write(v+"<>"+vDef+"<>")

    out.write("\n#Cluster")
    if 'Cluster' in yml and yml['Cluster'] is not None:
        if 'ClusterProgramName' in yml['Cluster']:
            out.write("\nClusterProgramName="+yml['Cluster']['ClusterProgramName'])
        if 'ExecutableCluster' in yml['Cluster']:
            out.write("\nExecutableCluster="+yml['Cluster']['ExecutableCluster'])
    if 'version' in yml['Program']:
        out.write("\nVersion= "+u.get_program_version(yml)+"")

    out.write("\n#Docker")
    if 'Docker' in yml and yml['Docker'] is not None:
        if 'DockerImage' in yml['Docker']:
            out.write("\nDockerImage="+yml['Docker']['DockerImage'])
        if 'ExecutableDocker' in yml['Docker']:
            out.write("\nExecutableDocker="+yml['Docker']['ExecutableDocker'])
        if 'DockerInputs' in yml['Docker']:
            out.write("\nDockerInputs="+yml['Docker']['DockerInputs'])
        if 'DockerOutputs' in yml['Docker']:
            out.write("\nDockerOutputs="+yml['Docker']['DockerOutputs'])
