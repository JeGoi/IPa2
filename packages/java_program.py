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

def create_program_file(yml,armaDir):
    progDir     = u.define_prog_path(armaDir)
    filename    = progDir+""+u.get_program_name(yml)+".java"
    out = open(filename, 'w')
    write_begin(out,yml)
    write_check_requirement(out,yml)
    write_command_line(out,yml)
    write_output_parsing(out,yml)
    write_end(out, yml)

# ===============================================
#  SUB FUNCTIONS TO CREATE Programs File
# ===============================================

#
# Header and variables
#
def write_begin(out, yml):
    write_begin_start(out,yml)
    write_import_class(out,yml)
    write_author_date(out,yml)
    write_variables(out,yml)
    write_tables_of_commands_per_panel(out,yml)
    write_begin_end(out,yml)
#
# Header and variables
#

def write_begin_start(out, yml):
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

def write_import_class(out,yml):
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
              "import biologic.Unknown;\n"+
              "import configuration.Cluster;\n"+
              "import configuration.Util;\n"+
              "import program.RunProgram;\n"+
              "import static program.RunProgram.df;\n"+
              "import static program.RunProgram.PortInputUP;\n"+
              "import static program.RunProgram.status_error;\n"+
              "import static program.RunProgram.status_running;\n"+
              "import workflows.workflow_properties;\n"+
              "import java.io.IOException;\n"+
              "import java.io.File;\n"+
              "import java.util.ArrayList;\n"+
              "import java.util.Arrays;\n"+
              "import java.util.concurrent.TimeUnit;\n"+
              "import java.util.HashMap;\n"+
              "import java.util.Hashtable;\n"+
              "import java.util.Iterator;\n"+
              "import java.util.logging.Level;\n"+
              "import java.util.logging.Logger;\n"+
              "import java.util.Map;\n"+
              "import java.util.Vector;\n"+
              "import org.apache.commons.lang.StringUtils;\n"+
              "\n")

def write_author_date(out,yml):
    out.write("/**\n"+
                " *\n"+
                " * @author "+yml['author']+"\n"+
                " * @date "+yml['date']+"\n"+
                " *\n"+
                " */\n")

def write_variables(out, yml):
    out.write("public class "+u.get_program_name(yml)+" extends RunProgram {\n"+
                "    // CREATE VARIABLES HERE\n"
            )

    if 'Docker' in yml and yml['Docker'] is not None:
        doName = u.set_docker_name(yml)
        yml['Docker']['dockerName'] = doName
        
        out.write("    private String allDoInputs    = \"\";\n"+
                  "    private HashMap<String,String> sharedFolders = new HashMap<String,String>();\n")
    # Write inputs
    out.write("    //INPUTS\n")
    if len(yml['Inputs']) > 0:
        x = 1
        for op in yml['Inputs']:
            if op['type']:
                out.write("    private String input"+str(x)+"       = \"\";\n")
                out.write("    private String inputId"+str(x)+"   = \"\";\n")
                out.write("    private String inputPath"+str(x)+"   = \"\";\n")
                x = x+1
    else:
        out.write("    //private String input1      = \"\";\n"+
                  "    //private String inputPath1  = \"\";\n")

    # Write outputs
    out.write("    //OUTPUTS\n")
    if len(yml['Outputs']) > 0:
        x = 1
        for op in yml['Outputs']:
            if op['type']:
                out.write("    private String output"+str(x)+"       = \"\";\n")
                if 'Docker' in yml and yml['Docker'] is not None:
                    out.write("    private String outputInDo"+str(x)+"   = \"\";\n")
                out.write("    private String outputInCl"+str(x)+"   = \"\";\n")
                x = x+1
    else:
        out.write("    //private String output1   =\"\";\n")
        if 'Docker' in yml and yml['Docker'] is not None:
            out.write("    //private String outputInDo1   = \"\";\n")

    out.write("    \n"+
              "    // If an input has several links from different capsules at the same time, you can use\n"+
              "    //private String[] inputsPathXX= {};\n"+
              "    //private String[] inputsIDsXX = {};\n"+
              "    \n")


    # Write Paths
    out.write("    //PATHS\n")
    if yml['Program']['outputsPath'] is not "" and yml['Program']['outputsPath'] is not None:
        s = u.cleanOutuptPath(yml)
        out.write("    private static final String outputsPath = "+s+";\n")
    else:
        out.write("    private static final String outputsPath = \"\";\n")
        #out.write("    private static final String outputsPath = \".\"+File.separator+\"results\"+File.separator+\""+u.get_program_name(yml)+"\";\n")
        #out.write("    private static final String inputPath  = outputsPath+File.separator+\"INPUTS\";\n\n")

    

# Variables sub functions
def write_tables_of_commands_per_panel(out, yml):
    for Panel in yml['Menus']:
        pName   = Panel['name']
        pNameS = u.name_without_space(Panel['name'])
        if 'Panel' in Panel:
            out.write("    private static final String[] "+pNameS+" = {\n")
            y = 0
            for Tab in Panel['Panel']:
                tName   = Tab['tab']
                if 'Arguments' in Tab:
                    # Print tab for functions and add it
                    # Print commands object name
                    cSize   = len(Tab['Arguments'])
                    x       = 0
                    for Arguments in Tab['Arguments']:
                        cName   = Arguments['name']
                        cType   = Arguments['cType']
                        c       = u.create_button_name(pName,tName,cName,cType)
                        v       = ""
                        if 'values' in Arguments and \
                            Arguments['values'] is not None and \
                            Arguments['values']['vType'] is not None:
                            vType   = Arguments['values']['vType']
                            v       = u.create_value_name(pName,tName,cName,vType)

                        out.write("        \""+c+"\"")
                        if x < (cSize-1):
                            if 'values' in Arguments and \
                                Arguments['values'] is not None and \
                                Arguments['values']['vType'] is not None:
                                out.write(",\n        //\""+v+"\",\n")
                            else:
                                out.write(",\n")
                        else:
                            if 'values' in Arguments and \
                                Arguments['values'] is not None and \
                                Arguments['values']['vType'] is not None:
                                out.write("//,\n        //\""+v+"\"")
                            else:
                                out.write("")
                        x += 1
                if (y<len(Panel['Panel'])-1):
                    out.write(",\n")
                else:
                    out.write("\n")
                y+=1
            out.write("    };\n\n")

def write_begin_end(out,yml):
    out.write("\n    public "+u.get_program_name(yml)+"(workflow_properties properties){\n"+
                "        this.properties=properties;\n"+
                "        execute();\n"+
                "    }\n")

#
# Check requirement
#
def write_check_requirement(out,yml):
    write_check_requirement_start(out,yml)
    write_get_inputs(out,yml)
    write_test_inputs(out,yml)
    write_prepare_outputs_path(out,yml)
    if 'Docker' in yml and yml['Docker'] is not None:
        write_test_docker_variables_from_properties(out,yml)
        write_extract_dockerinfo_from_properties(out,yml)
    write_outputs(out,yml)
    if 'Docker' in yml and yml['Docker'] is not None:
        write_test_Docker(out,yml)
    write_check_requirement_end(out,yml)
    write_start_without_edition(out,yml)
#
# Check requirement
#

def write_check_requirement_start(out,yml):
    out.write("\n"+
              "    @Override\n"+
              "    public boolean init_checkRequirements(){\n"+
              "\n"+
              "        // In case program is started without edition\n"+
              "        pgrmStartWithoutEdition(properties);\n"+
              "\n")


# Prepare inputs data
def write_prepare_outputs_path(out,yml):
    out.write("\n        // TEST OUTPUT PATH\n"+
              "        String specificId = Util.returnRandomAndDate();\n"+
              "        if (properties.isSet(\"ObjectID\")) {\n"+
              "            String oId = properties.get(\"ObjectID\");\n"+
              "            oId = Util.replaceSpaceByUnderscore(oId);\n"+
              "            specificId = specificId+\"_\"+oId;\n"+
              "        }\n")
    if yml['Program']['outputsPath'] is "":
        out.write("        outputsPath=Util.getParentOfFile(inputPath1);\n")
    out.write("        String specificPath = outputsPath+specificId;\n"+
              "        if (!Util.CreateDir(specificPath) && !Util.DirExists(specificPath)){\n"+
              "            setStatus(status_BadRequirements,\"Not able to access or create OUTPUTS directory files\");\n"+
              "            return false;\n"+
              "        }\n\n"+
              "        \n")

# Prepare inputs data
def write_get_inputs(out,yml):
    portToName = {
        "true":"PortInputDOWN",
        3:"PortInputUP",
        2:"PortInputDOWN",
        4:"PortInputDOWN2"
    }
    out.write("        // TEST INPUT VARIABLES HERE\n"+
              "        // ports are 3-PortInputUp, 2-PortInputDOWN, 4-PortInputDOWN2\n")
    if len(yml['Inputs']) > 0:
        x = 1
        for op in yml['Inputs']:
            if op['type']:
                out.write("\n        Vector<Integer>"+op['type']+str(x)+"    = properties.getInputID(\""+op['type']+"\","+portToName[op['connector']]+");\n"+
                           "        inputPath"+str(x)+" = Unknown.getVectorFilePath("+op['type']+str(x)+");\n"+
                           "        inputId"+str(x)+" = Unknown.getVectorFileId("+op['type']+str(x)+");\n"+
                           "        input"+str(x)+"     = Util.getFileNameAndExt(inputPath"+str(x)+");\n")
                x = x+1
    else:
        out.write("        // No imput : Example\n"+
                  "        //Vector<Integer>Fastq1    = properties.getInputID(\"FastqFile\",PortInputDOWN);\n"+
                  "        //inputPath1 = Unknown.getVectorFilePath(Fastq1);\n"+
                  "        //inputId1   = Unknown.getVectorFileId(Fastq1);\n"+
                  "        //input1     = Util.getFileNameAndExt(inputPath1);\n")
    out.write("        \n"+
              "        // If an input has several links from different capsules at the same time, you can use\n"+
              "        // inputsPathXX = Unknown.getAllVectorFilePath(UnknownXX);\n"+
              "        // inputsIDsXX  = Unknown.getVectorFileIds(UnknownXX);\n"+
              "        \n")


# Check requirement sub functions
def write_test_inputs(out,yml):
    out.write("        \n"+
              "        //INSERT YOUR INPUT TEST HERE\n")
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
                    out.write("        // Please, check if it's \"else if\" or it's a real \"if\"\n"+
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
                  "        }\n    \n")
    out.write("\n")

def write_test_docker_variables_from_properties(out,yml):
    out.write("        // Test Docker Variables presence\n"+
              "        if (Docker.areDockerVariablesNotInProperties(properties)){\n"+
              "            setStatus(status_BadRequirements,Util.BRDockerVariables());\n"+
              "            return false;\n"+
              "        }\n    \n")

def write_extract_dockerinfo_from_properties(out,yml):
    out.write("        // Extract Docker Variables\n"+
              "        String doInputs = properties.get(\"DockerInputs\");\n"+
              "        String doOutputs = properties.get(\"DockerOutputs\");\n"+
              "        }\n    \n")

def write_outputs(out,yml):
    out.write("        // Prepare ouputs\n")
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
                com = ""
                if op['command2Call']:
                    com = op['command2Call']
                out.write("        output"+str(x)+" = specificPath+File.separator+\"OutputOf_\"+input"+str(x)+"+\""+op['extension']+"\";\n"+
                          "        output"+str(x)+" = Util.onlyOneOutputOf(output"+str(x)+");\n")
                if 'Docker' in yml and yml['Docker'] is not None:
                    out.write("        outputInDo"+str(x)+" = doOutputs+\"OutputOf_\"+input"+str(x)+"+\""+op['extension']+"\";\n"+
                              "        outputInDo"+str(x)+" = Util.onlyOneOutputOf(outputInDo"+str(x)+");\n")
                x = x+1
    else:
        out.write("        // No output : Example\n"+
                  "        //output1 = specificPath+File.separator+\"OutputOf_\"+input1+\".outputextension\";\n"+
                  "        //output"+str(x)+" = Util.onlyOneOutputOf(output1);\n")
        if 'Docker' in yml and yml['Docker'] is not None:
            out.write("        //outputInDo1 = doOutputs+\"OutputOf_\"+input1+\".outputextension\";\n")
            out.write("        //outputInDo1 = Util.onlyOneOutputOf(outputInDo1);\n")
    
    out.write("        \n"+
              "        // You may link output type with options\n"+
              "        // if (properties.isSet(\"OPTION_NAME\")) {\n"+
              "        //     output1 = specificPath+File.separator+\"OutputOf_\"+input3+\".vcf\";\n"+
              "        //     outputInDo1 = doOutputs+\"OutputOf_\"+input3+\".vcf\";\n"+
              "        // } else if (properties.isSet(\"ANOTHER_OPTION\")) {\n"+
              "        //     output1 = specificPath+File.separator+\"OutputOf_\"+input3+\".bcf\";\n"+
              "        //     outputInDo1 = doOutputs+\"OutputOf_\"+input3+\".bcf\";\n"+
              "        // }\n")

    out.write("        \n")

def write_test_Docker(out,yml):
    write_prepare_Docker_shared_folders(out,yml)
    write_prepare_Docker_allDoInputs(out,yml)
    write_docker_init(out)

def write_prepare_Docker_shared_folders(out,yml):
    allInputsPath = u.get_all_inputspath(yml)
    allInputsID   = u.get_all_inputsId(yml)
    out.write("        // Prepare shared folders\n"+
              "        String[] simplePath = {"+allInputsPath+"};\n"+
              "        // If an input (or several) as multiple inputs add\n"+
              "        //String[] allInputsPath = Util.merge2TablesWithoutDup(simplePath, inputsPathXX);\n"+
              "        String[] simpleId = {"+allInputsID+"};\n"+
              "        // If an input (or several) as multiple inputs add\n"+
              "        //String[] allInputsId = Util.merge2TablesWithoutDup(simpleId, inputsIDsXX);\n"+
              "        \n"+
              "        // Prepare Relations local distant (Docker and Cluster)\n"+
              "        sharedFolders = Docker.createSharedFolders(simplePath,simpleId,doInputs);\n"+
              "        // If multiple Inputs\n"+
              "        //sharedFolders = Docker.createSharedFolders(allInputsPath,allInputsId,doInputs);\n"+
              "        sharedFolders = Docker.addInSharedFolder(sharedFolders,specificPath,doOutputs);\n"+
              "        Cluster.createLinkDockerClusterInputs(properties,simplePath,simpleId,doInputs);\n"+
              "        // If multiple Inputs\n"+
              "        //Cluster.createLinkDockerClusterInputs(properties,allInputsPath,allInputsId,doInputs);\n"+
              "        Cluster.createLinkDockerClusterOutput(properties,output1,outputInDo1);\n"+
              "        \n        \n")
              
def write_prepare_Docker_allDoInputs(out,yml):
    out.write("        // Prepare allDoInputs\n"+
              "        HashMap<String,String> pathAndArg = new HashMap<String,String>();\n")
    if len(yml['Inputs']) > 0:
        x = 1
        for op in yml['Inputs']:
            if op['type']:
                s = ""
                if 'command2Call' in op and op['command2Call'] is not None:
                    s = op['command2Call']
                out.write("        pathAndArg.put(inputPath"+str(x)+",\""+s+"\");\n")
                x = x+1
    out.write("        // For multiple inputs use this to set their argument\n"+
              "        //for (String st:inputsPathXX){\n"+
              "        //    if (allInputsPathArg.get(st)==null)\n"+
              "        //        allInputsPathArg.put(st,"");\n"+
              "        //}\n"+
              "        \n")

    out.write("        allDoInputs = Docker.createAllDockerInputs(pathAndArg,allInputsPath,simpleId,doInputs);\n"+
              "\n")

def write_docker_init(out):
    out.write("        // DOCKER INIT\n"+
              "        if (Docker.isDockerHere()){\n"+
              "            long duration = Docker.prepareContainer(properties,sharedFolders);\n"+
              "            if (!Docker.isDockerContainerIDPresentIn(properties)){\n"+
              "                setStatus(status_BadRequirements,Util.BRDockerInit());\n"+
              "                return false;\n"+
              "            }\n"+
              "            setStatus(status_running,Util.RUNDockerDuration(\"launch\",duration));\n"+
              "        } else {\n"+
              "            setStatus(status_BadRequirements,Util.BRDockerNotFound());\n"+
              "            return false;\n"+
              "        }\n"+
              "\n")


def write_check_requirement_end(out,yml):
    out.write("        return true;\n"+
              "    }\n"+
              "    \n")

def write_start_without_edition(out,yml):
    out.write("        // In case program is started without edition and params need to be setted\n"+
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
    out.write("        }\n"+
              "    \n")

#
# Command line
#
def write_command_line(out,yml):
    write_command_line_start(out,yml)
    write_options(out,yml)
    if 'Docker' in yml and yml['Docker'] is not None:
        write_docker_command_line_creation(out,yml)
    write_command_line_creation(out,yml)
#
# Command line
#


def write_command_line_start(out,yml):
    out.write("    @Override\n"+
              "    public String[] init_createCommandLine() {\n"+
              "        \n")

# Command line sub functions
def write_options(out,yml):
    tabPerPanel = u.get_tab_per_panel(out,yml)
    out.write("        // Program and Options\n"+
              "        String options = \"\";\n")
    if len(tabPerPanel) > 0:
        for op in tabPerPanel:
            out.write("        if (properties.isSet(\""+op+"\"))\n"+
                      "            options += Util.findOptionsNew("+op+",properties);\n")
    out.write("        \n")

def write_docker_command_line_creation(out,yml):
    out.write("        // Pre command line\n"+
              "        String preCli = options+" "+allDoInputs+" > "+outputInDo1;\n"+
              "        \n"+
              "        // Docker command line\n"+
              "        String dockerCli = properties.get(\"ExecutableDocker\")+\" \"+preCli;\n"+
              "        long duration = Docker.prepareDockerBashFile(properties,dockerCli);\n"+
              "        setStatus(status_running, \"\t<TIME> Time to prepare docker bash file is >\"+duration+\" s\");\n"+
              "        setStatus(status_running,\"Docker CommandLine: \n$ \"+dockerCli);\n"+
              "        \n"+
              "        // Cluster\n"+
              "        String clusterCli = properties.get(\"ExecutableCluster\")+" "+preCli;\n"+
              "        Cluster.createClusterRunningCLiFromDocker(properties, clusterCli);\n"+
              "\n")        
        
# REMOVE DOCKER REFERENCE
def write_command_line_creation(out,yml):
    if 'Docker' in yml and yml['Docker'] is not None:
        out.write("        \n"+
                  "        // Command line\n"+
                  "        String[] com = {\"\"};\n")
    else:
        out.write("        \n"+
                  "        // Command line creation\n"+
                    "        String[] com = new String[30];\n"+
                    "        for (int i=0; i<com.length;i++) com[i]=\"\";\n"+
                    "        \n"+
                    "        com[0]= \"cmd.exe\"; // For Windows, will de remove if another os is used\n"+
                    "        com[1]= \"/C\";      // For Windows, will de remove if another os is used\n"+
                    "        com[2]= properties.getExecutable();\n")
        i = 3
        out.write("        com["+str(i)+"]= options;\n")

        if len(yml['Inputs']) > 0:
            x = 1
            for op in yml['Inputs']:
                if op['type']:
                    i += 1
                    inputName = "inputPath"+str(x)
                    if op['command2Call']:
                        com = op['command2Call']
                        out.write("        if ("+inputName+" != (\"Unknown\") || "+inputName+".isEmpty()) {\n"+
                                  "            com["+str(i)+"]= \""+com+" \"+"+inputName+";\n"+
                                  "        }\n")
                    else:
                        out.write("        com["+str(i)+"]= "+inputName+";\n")
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
                    out.write(str(x)+";\n")
                x = x+1
        else:
            i += 1
            out.write("        //com["+str(i)+"]=outputsPath1;\n")

    out.write("        return com;\n"+
                "    }\n"+
                "\n")
                




#
# Output Parsing
#
def write_output_parsing(out, yml):
    write_output_parsing_start(out, yml)
    if 'Docker' in yml and yml['Docker'] is not None:
        write_docker_out(out,yml)
    write_output_results(out,yml)
    write_output_parsing_end(out,yml)
#
# Output Parsing
#

def write_output_parsing_start(out, yml):
    out.write("        \n"+
              "\n"+
              "    /*\n"+
              "    * Output Parsing\n"+
              "    */\n"+
              "\n"+
              "    @Override\n"+
              "    public void post_parseOutput(){\n")

def write_docker_out(out, yml):
    out.write("        // Stop Docker container\n"+
              "        long duration = Docker.removeContainer(properties);\n"+
              "        setStatus(status_running, Util.RUNDockerDuration(\"stop and remove\",duration));\n"+
              "        \n")


def write_output_results(out, yml):
    out.write("        // Save outputs\n")
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
              "\n")

def write_output_parsing_end(out, yml):
    out.write("    }\n"+
              "\n")
              
#
# Close the file
#
def write_end(out, yml):
    out.write("}\n"+
              "\n")
#
# Close the file
#
