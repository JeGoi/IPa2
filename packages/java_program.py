#!/usr/bin/env python
"""
Title   : Java program file
Author  : JG
Date    : dec 2016
Objet   : script to create Java File Program
in      : get infos from yml
out     : print infos in java file
"""
import sys,os
import yaml
import util as u

def create_program_file(yml,isTest):
    progDir     = u.define_prog_path(isTest)
    filename    = progDir+""+u.get_program_name(yml)+".java"
    out = open(filename, 'w')
    write_header(out,yml)
    write_check_requirement(out,yml)
    write_command_line(out,yml)
    write_output_parsing(out,yml)

# ===============================================
#  SUB FUNCTIONS TO CREATE Programs File
# ===============================================
#
# Header and variables
#
def write_header(out, yml):
    out.write("/*\n"+
                "* To change this license header, choose License Headers in Project Properties.\n"+
                "* To change this template file, choose Tools | Templates\n"+
                "* and open the template in the editor.\n"+
                "* Author : "+yml['author']+"\n"+
                "* Date   : "+yml['date']+"\n"+
                "*/\n"+
                "\n"+
                "package programs;\n"+
                "\n")
    importBiologicType = {}
    for op in yml['Inputs']:
        if 'type' in op:
            importBiologicType[op['type']] = ''
    
    for op in yml['Outputs']:
        if 'type' in op:
            importBiologicType[op['type']] = ''
    
    for bio in importBiologicType:
        out.write("import biologic."+bio+";\n")
    
    if 'Docker' in yml and yml['Docker'] is not None:
        out.write("import configuration.Docker;\n")
    
    out.write("import biologic.Results;\n"+
                "import configuration.Util;\n"+
                "import java.io.File;\n"+
                "import java.util.Vector;\n"+
                "import java.util.Hashtable;\n"+
                "import java.util.Map;\n"+
                "import java.util.Iterator;\n"+
                "import program.RunProgram;\n"+
                "import static program.RunProgram.PortInputUP;\n"+
                "import static program.RunProgram.df;\n"+
                "import static program.RunProgram.status_error;\n"+
                "import workflows.workflow_properties;\n"+
                "import java.io.IOException;\n"+
                "import java.util.ArrayList;\n"+
                "import java.util.logging.Level;\n"+
                "import java.util.logging.Logger;\n"+
                "\n"+
                "\n"+
                "/**\n"+
                " *\n"+
                " * @author "+yml['author']+"\n"+
                " * @date "+yml['date']+"\n"+
                " *\n"+
                " */\n")
    write_variables(out,yml)
    out.write("\n    public "+u.get_program_name(yml)+"(workflow_properties properties){\n"+
                "        this.properties=properties;\n"+
                "        execute();\n"+
                "    }\n")

def write_variables(out, yml):
    out.write("public class "+u.get_program_name(yml)+" extends RunProgram {\n"+
                "    // CREATE VARIABLES HERE\n"
            )
    
    if 'Docker' in yml and yml['Docker'] is not None:
        if yml['Docker']['dockerName'] == None:
            yml['Docker']['dockerName'] = yml['Docker']['imageName']
        out.write("    private String doImage        = \""+yml['Docker']['imageName']+"\";\n"+
                  "    private String doPgrmPath     = \""+yml['Docker']['cmd']+"\";\n"+
                  "    private String doSharedFolder = \""+yml['Docker']['sharedFolder']+"\";\n"+
                  "    private String doName         = \""+yml['Docker']['dockerName']+"\";\n")
    # Write inputs
    out.write("    //INPUTS\n")
    if len(yml['Inputs']) > 0:
        x = 1
        for op in yml['Inputs']:
            if op['type']:
                out.write("    private String input"+str(x)+"       = \"\";\n")
                out.write("    private String inputPath"+str(x)+"   = \"\";\n")

                if 'Docker' in yml and yml['Docker'] is not None:
                    out.write("    private String inputInDo"+str(x)+"   = \"\";\n")
                    out.write("    private String inputPathDo"+str(x)+" = \"\";\n")
                x = x+1
    else:
        out.write("    //private String input1      = \"\";\n"+
                  "    //private String inputPath1  = \"\";\n")
        if 'Docker' in yml and yml['Docker'] is not None:
            out.write("    //private String inputInDo1   = \"\";\n"+
                      "    //private String inputPathDo1 = \"\";\n")
        
    # Write outputs
    out.write("    //OUTPUTS\n")
    if len(yml['Outputs']) > 0:
        x = 1
        for op in yml['Outputs']:
            if op['type']:
                out.write("    private String output"+str(x)+"       = \"\";\n")
                if 'Docker' in yml and yml['Docker'] is not None:
                    out.write("    private String outputInDo"+str(x)+"   = \"\";\n"+
                              "    private String outputPathDo"+str(x)+" = \"\";\n")
                x = x+1
    else:
        out.write("    //private String output1   =\"\";\n")
        if 'Docker' in yml and yml['Docker'] is not None:
            out.write("    //private String outputInDo1   = \"\";\n"+
                      "    //private String outputPathDo1 = \"\";\n")
    
    # Write Paths
    out.write("    //PATHS\n")
    if yml['Program']['outputPath'] is not "":
        s = u.cleanOutuptPath(yml)
        out.write("    private static final String outputPath = "+s+";\n"+
                  "    private static final String inputPath  = outputPath+File.separator+\"INPUTS\";\n\n")
    else:
        out.write("    private static final String outputPath = \".\"+File.separator+\"results\"+File.separator+\""+u.get_program_name(yml)+"\";\n"+
                  "    private static final String inputPath  = outputPath+File.separator+\"INPUTS\";\n\n")
    write_tables_of_commands_per_panel(out,yml)
# Variables sub functions
def write_tables_of_commands_per_panel(out, yml):
    for Panel in yml['Menus']:
        pName   = Panel['name']
        if 'Panel' in Panel:
            for Tab in Panel['Panel']:
                tName   = Tab['tab']
                tNameS  = u.name_without_space(tName)
                if 'Arguments' in Tab:
                    # Print tab for functions and add it
                    out.write("    private static final String[] "+tNameS+" = {\n")
                    # Print commands object name
                    cSize   = len(Tab['Arguments'])
                    x       = 0
                    for Arguments in Tab['Arguments']:
                        cName   = Arguments['name']
                        cType   = Arguments['cType']
                        c       = u.create_button_name(pName,tName,cName,cType)
                        v       = ""
                        if 'values' in Arguments and Arguments['values'] is not None:
                            vType   = Arguments['values']['vType']
                            v       = u.create_value_name(pName,tName,cName,vType)

                        out.write("        \""+c+"\"")
                        if x < (cSize-1):
                            if 'values' in Arguments and Arguments['values'] is not None:
                                out.write(",\n        //\""+v+"\",\n")
                            else:
                                out.write(",\n")
                        else:
                            if 'values' in Arguments and Arguments['values'] is not None:
                                out.write("//,\n        //\""+v+"\"\n")
                            else:
                                out.write("\n")
                        x += 1
                    out.write("    };\n\n")
#
# Check requirement
#
def write_check_requirement(out,yml):
    portToName = {
        "true":"PortInputDOWN",
        3:"PortInputUP",
        2:"PortInputDOWN",
        4:"PortInputDOWN2"
    }
    out.write("\n"+
              "    @Override\n"+
              "    public boolean init_checkRequirements(){\n"+
              "\n"+
              "        // TEST INPUT VARIABLES HERE\n"+
              "        // ports are 3-PortInputUp, 2-PortInputDOWN, 4-PortInputDOWN2\n")
    if len(yml['Inputs']) > 0:
        x = 1
        for op in yml['Inputs']:
            if op['type']:
                out.write("\n        Vector<Integer>"+op['type']+str(x)+"    = properties.getInputID(\""+op['type']+"\","+portToName[op['connector']]+");\n"+
                           "        inputPath"+str(x)+" = "+op['type']+".getVectorFilePath("+op['type']+str(x)+");\n"+
                           "        input"+str(x)+"     = Util.getFileNameAndExt(inputPath"+str(x)+");\n")
                x = x+1
    else:
        out.write("        // No imput : Example\n"+
                   "        //Vector<Integer>Fastq1    = properties.getInputID(\"FastqFile\",PortInputDOWN);\n"+
                   "        //inputPath1 = FastqFile.getVectorFilePath(Fastq1);\n"+
                   "        //input1     = Util.getFileNameAndExt(inputPath1);\n")
    write_test_inputs(out,yml)
    if 'Docker' in yml and yml['Docker'] is not None:
        write_test_Docker(out,yml)
    out.write("        return true;\n"+
              "    }\n")

# Check requirement sub functions
def write_test_inputs(out,yml):
    out.write("        //INSERT YOUR INPUT TEST HERE\n")
    if len(yml['Inputs']) > 0:
        x = 1
        for op in yml['Inputs']:
            if op['type']:
                if x==1:
                    out.write("        if ("+op['type']+str(x)+".isEmpty()||input"+str(x)+".equals(\"Unknown\")||input"+str(x)+".equals(\"\")){\n"+
                              "            setStatus(status_BadRequirements,\"No "+op['type']+" found.\");\n"+
                              "            return false;\n"+
                              "        }\n")
                else:
                    out.write("        //Check if it's else or not\n"+
                              "        //else \n"+
                              "        if ("+op['type']+str(x)+".isEmpty()||input"+str(x)+".equals(\"Unknown\")||input"+str(x)+".equals(\"\")){\n"+
                              "            setStatus(status_BadRequirements,\"No "+op['type']+" found.\");\n"+
                              "            return false;\n"+
                              "        }\n")
                x = x+1
    else:
        out.write("        // No imput : Example\n"+
                  "        //if (Fastq1.isEmpty()||input1.equals(\"Unknown\")||input1.equals(\"\")){\n"+
                  "        //    setStatus(status_BadRequirements,\"No sequence found.\");\n"+
                  "        //    return false;\n"+
                  "        }\n")
    out.write("\n")
def write_test_Docker(out,yml):
    write_test_Docker_shared_files(out,yml)
    write_clean_docker(out)
def write_test_Docker_shared_files(out,yml):
    out.write("        //INSERT DOCKER SHARED FILES COPY HERE\n"+
              "        if (!Util.CreateDir(inputPath) && !Util.DirExists(inputPath)){\n"+
              "            setStatus(status_BadRequirements,\"Not able to create INPUTS directory files\");\n"+
              "            return false;\n"+
              "        }\n"+
              "        if (!Util.CreateDir(outputPath) && !Util.DirExists(outputPath)){\n"+
              "            setStatus(status_BadRequirements,\"Not able to create OUTPUTS directory files\");\n"+
              "            return false;\n"+
              "        }\n\n")
    if len(yml['Inputs']) > 0:
        x = 1
        for op in yml['Inputs']:
            if op['type']:
                out.write("        inputPathDo"+str(x)+" = outputPath+File.separator+\"INPUTS\"+File.separator+input"+str(x)+";\n"+
                          "        if (!(Util.copy(inputPath"+str(x)+",inputPathDo"+str(x)+"))){\n"+
                          "            setStatus(status_BadRequirements,\"Not able to copy files used by docker container\");\n"+
                          "            return false;\n"+
                          "        }\n"+
                          "        inputInDo"+str(x)+" = doSharedFolder+File.separator+\"INPUTS\"+File.separator+input"+str(x)+";\n"+
                          "        input"+str(x)+" = Util.getFileName(inputPath"+str(x)+");\n\n")
                x = x+1
    else:
        out.write("        inputPathDo1 = Util.getCanonicalPath(outputPath+File.separator+input1);\n"+
                  "        if (!(Util.copy(inputPath1,inputPathDo1))){\n"+
                  "            setStatus(status_BadRequirements,\"Not able to copy files  used by docker container\");\n"+
                  "            return false;\n"+
                  "        }\n"+
                  "        inputDo1 = doSharedFolder+File.separator+input1;\n"+
                  "        input1   = Util.getFileName(inputPath1);\n\n")
    out.write("\n")
def write_clean_docker(out):
    out.write("        // TEST Docker initialisation\n"+
                "        doName = Docker.getContainersVal(doName);\n"+
                "        if (!dockerInit(outputPath,doSharedFolder,doName,doImage)){\n"+
                "            Docker.cleanContainers(doName);\n"+
                "            setStatus(status_BadRequirements,\"Not able to initiate docker container\");\n"+
                "            return false;\n"+
                "         } else {\n"+
                "            properties.put(\"DOCKERName\",doName);\n"+
                "         }\n"+
                "\n")
#
# Command line
#
def write_command_line(out,yml):
    out.write("    @Override\n"+
              "    public String[] init_createCommandLine() {\n"+
              "\n"+
              "        // In case program is started without edition\n"+
              "        pgrmStartWithoutEdition(properties);\n"+
              "\n")
    write_outputs(out,yml)
    write_options(out,yml)
    write_command_line_creation(out,yml)
# Command line sub functions
def write_outputs(out,yml):
    out.write("        //Create ouputs\n")
    outputsSize = len(yml['Outputs'])
    inputsSize = len(yml['Inputs'])
    
    inputsNames = ""
    if inputsSize > 1:
        x = 1
        for op in yml['Inputs']:
            if op['type']:
                if x < inputsSize:
                    inputsNames = inputsNames+"input"+str(x)+"+\"_\"+"
                else:
                    inputsNames = inputsNames+"input"+str(x)
                x = x+1
    else :
        inputsNames = "input1"

    if outputsSize > 0:
        x = 1
        for op in yml['Outputs']:
            if op['type']:
                out.write("        output"+str(x)+" = outputPath+File.separator+\"OutpuOf_\"+"+inputsNames+"+\""+op['extension']+"\";\n")
                if 'Docker' in yml and yml['Docker'] is not None:
                    out.write("        outputInDo"+str(x)+" = doSharedFolder+File.separator+\"OutpuOf_\"+"+inputsNames+"+\""+op['extension']+"\";\n")
                x = x+1
    else:
        out.write("        // No output : Example\n"+
                    "        //output1 = outputPath+File.separator+\"OutpuOf_\"+input1+\".outputextension\";\n")
        if 'Docker' in yml and yml['Docker'] is not None:
            out.write("        //outputInDo1 = doSharedFolder+File.separator+\"OutpuOf_\"+input1+\".outputextension\";\n")
def write_options(out,yml):
    tabPerPanel = u.get_tab_per_panel(out,yml)
    out.write("        \n"+
                "        // Program and Options\n"+
                "        String options = \"\";\n")
    if len(tabPerPanel) > 0:
        for op in tabPerPanel:
            out.write("        if (properties.isSet(\""+op+"\"))\n"+
                      "            options += Util.findOptionsNew("+op+",properties);\n")
    out.write("        \n")
def write_command_line_creation(out,yml):
    out.write("        \n"+
                "        // Command line creation\n"+
                "        String[] com = new String[30];\n"+
                "        for (int i=0; i<com.length;i++) com[i]=\"\";\n"+
                "        \n"+
                "        com[0]= \"cmd.exe\"; // Windows will de remove if another os is used\n"+
                "        com[1]= \"/C\";      // Windows will de remove if another os is used\n"+
                "        com[2]= properties.getExecutable();\n")
    i = 3
    if 'Docker' in yml and yml['Docker'] is not None:
        out.write("        com["+str(i)+"]= \"exec \"+doName+\" \"+doPgrmPath;\n")
        i += 1
    out.write("        com["+str(i)+"]= options;\n")
    
    if len(yml['Inputs']) > 0:
        x = 1
        for op in yml['Inputs']:
            if op['type']:
                i += 1
                inputName = "input"
                if 'Docker' in yml and yml['Docker'] is not None:
                    inputName = inputName+"InDo"
                else:
                    inputName = inputName+"Path"
                inputName = inputName+str(x)                
                if op['command2Call']:
                    com = op['command2Call']
                    out.write("        if ("+inputName+" != (\"Unknown\") || "+inputName+".isEmpty()) {\n"+
                              "            com["+str(i)+"]= \""+com+" \"+"+inputName+";\n"+
                              "        }\n")
                else:
                    out.write("        com["+str(i)+"]= "+inputName+"\n")
            x = x+1
    else:
        i += 1
        out.write("        com["+str(i)+"]= inputPath1;\n")
    
    if len(yml['Outputs']) > 0:
        x = 1
        for op in yml['Outputs']:
            if op['type']:
                i += 1
                if op['command2Call']:
                    com = op['command2Call']
                    out.write("        com["+str(i)+"]= \""+com+" \"+output")
                else:
                    out.write("        com["+str(i)+"]= output")
                if 'Docker' in yml and yml['Docker'] is not None:
                    out.write("InDo")
                out.write(str(x)+";\n")
            x = x+1
    else:
        i += 1
        out.write("        //com["+str(i)+"]=outputPath1;\n")
    
    out.write("        return com;\n"+
                "    }\n"+
                "\n"+
                "        // def functions for init_createCommandLine\n"+
                "        // In case program is started without edition and params need to be setted\n"+
                "        private void pgrmStartWithoutEdition (workflow_properties properties){\n")
    if len(yml['Menus'])>0:
        out.write("            if (")
        m = 0
        for op in yml['Menus']:
            if (m >0):
                out.write("                && ")
            out.write("!(properties.isSet(\""+u.name_without_space(op['name'])+"\"))\n")
            m += 1
        out.write("            ){\n"+
                  "                Util.getDefaultPgrmValues(properties,false);\n"+
                  "            }\n")
    else:
        out.write("           //if (!properties.isSet(\"\")) Util.getDefaultPgrmValues(properties, true);\n")
    out.write("        }\n")
#
# Output Parsing
#
def write_output_parsing(out, yml):
    out.write("        \n"+
              "\n"+
              "    /*\n"+
              "    * Output Parsing\n"+
              "    */\n"+
              "\n"+
              "    @Override\n"+
              "    public void post_parseOutput(){\n")
    if 'Docker' in yml and yml['Docker'] is not None:
        if 'copyDockerDir2SharedFolder' in yml['Docker'] and yml['Docker']['copyDockerDir2SharedFolder']:
            copy_docker_files(out,yml)
        remove_Docker_imputs(out)
    if 'outputFilesFromOutputPath' in yml['Program'] and yml['Program']['outputFilesFromOutputPath']:
        save_output_files(out,yml)
    write_output_results(out,yml)
# Output parsing sub functions
def copy_docker_files(out,yml):
    for op in yml['Docker']['copyDockerDir2SharedFolder']:
        if op:
            out.write("        boolean b1 = Docker.copyDockerDirToSharedDir(\""+op+"\",doSharedFolder,doName;\n"+
                      "        if (!b1) setStatus(status_BadRequirements,\"Docker Files Copy Failed\");\n")
def remove_Docker_imputs(out):
    out.write("        Util.deleteDir(inputPath);\n"+
              "        Docker.cleanContainer(doName);\n")
def save_output_files(out,yml):
    for op in yml['Program']['outputFilesFromOutputPath']:
        if op:
            out.write("        boolean b2 = Util.copyDirectory(doSharedFolder,"+op+");\n"+
                      "        if (!b2) setStatus(status_BadRequirements,\"Saved Files Copy Failed\");\n")
def write_output_results(out, yml):
    name = u.get_program_name(yml)
    if len(yml['Outputs']) > 0:
        x = 1
        for op in yml['Outputs']:
            if op['type']:
                out.write("        "+op['type']+".saveFile(properties,output"+str(x)+",\""+name+"\",\""+op['type']+"\");\n")
            else:
                out.write("        //SAMPLE OF OUTPUT as SAMFILE\n"+
                            "        //SamFile.saveFile(properties,output1,\""+name+"\",\"SamFile\");\n")
            x+=1
    out.write("        Results.saveResultsPgrmOutput(properties,this.getPgrmOutput(),\""+name+"\");\n"+
              "    }\n"+
              "}\n")
