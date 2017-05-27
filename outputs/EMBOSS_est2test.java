/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
* Author : J-G
* Date   : 05-02-2017
*/

package programs;

import biologic.FastaFile;
import biologic.EmblFile;
import biologic.GenomeFile;
import biologic.Est2genomeFile;
import configuration.Docker;
import biologic.Results;
import configuration.Util;
import java.io.File;
import java.util.Vector;
import java.util.Hashtable;
import java.util.Map;
import java.util.Iterator;
import program.RunProgram;
import static program.RunProgram.PortInputUP;
import static program.RunProgram.df;
import static program.RunProgram.status_error;
import workflows.workflow_properties;
import java.io.IOException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;


/**
 *
 * @author J-G
 * @date 05-02-2017
 *
 */
public class EMBOSS_est2test extends RunProgram:
    // CREATE VARIABLES HERE
    private String doImage        = "jego/emboss";
    private String doPgrmPath     = "est2genome --auto";
    private String doSharedFolder = "/data";
    private String doName         = "jego/emboss";
    //INPUTS
    private String input1       = "";
    private String inputPath1   = "";
    private String inputInDo1   = "";
    private String inputPathDo1 = "";
    private String input2       = "";
    private String inputPath2   = "";
    private String inputInDo2   = "";
    private String inputPathDo2 = "";
    private String input3       = "";
    private String inputPath3   = "";
    private String inputInDo3   = "";
    private String inputPathDo3 = "";
    //OUTPUTS
    private String output1       = "";
    private String outputInDo1   = "";
    private String outputPathDo1 = "";
    //PATHS
    private static final String outputPath = "."+File.separator+"results"+File.separator+"EMBOSS"+File.separator+"est2genome"+File.separator+"";
    private static final String inputPath  = outputPath+File.separator+"INPUTS";

    private static final String[] Other_Options_1 = {
        "OO_OO1_matchoo1_box"//,
        //"OO_OO1_matchoo1_JSpinnerValue"
    };

    private static final String[] Returned_Options_1 = {
        "RO_RO1_nomatchao1_box"//,
        //"RO_RO1_nomatchao1_JSpinnerValue"
    };

    private static final String[] Returned_Options_2 = {
        "RO_RO2_nomatchao2_box"//,
        //"RO_RO2_nomatchao2_JSpinnerValue"
    };

    private static final String[] Advanced_Options_1 = {
        "AO_AO1_matchao1_box"//,
        //"AO_AO1_matchao1_JSpinnerValue"
    };

    private static final String[] Advanced_Options_2 = {
        "AO_AO2_matchao2_box"//,
        //"AO_AO2_matchao2_JSpinnerValue"
    };

    private static final String[] Advanced_Options_3 = {
        "AO_AO3_matchao3_box"//,
        //"AO_AO3_matchao3_JSpinnerValue"
    };

    private static final String[] Advanced_Options_4 = {
        "AO_AO4_matchao4_box",
        //"AO_AO4_matchao4_JSpinnerValue",
        "AO_AO4_mismatchao4_box",
        //"AO_AO4_mismatchao4_JSpinnerValue",
        "AO_AO4_graphao4_box"//,
        //"AO_AO4_graphao4_JComboBoxValue"
    };


    public EMBOSS_est2test(workflow_properties properties){
        this.properties=properties;
        execute();
    }

    @Override
    public boolean init_checkRequirements(){

        // TEST INPUT VARIABLES HERE
        // ports are 3-PortInputUp, 2-PortInputDOWN, 4-PortInputDOWN2

        Vector<Integer>FastaFile1    = properties.getInputID("FastaFile",PortInputDOWN);
        inputPath1 = FastaFile.getVectorFilePath(FastaFile1);
        input1     = Util.getFileNameAndExt(inputPath1);

        Vector<Integer>EmblFile2    = properties.getInputID("EmblFile",PortInputDOWN);
        inputPath2 = EmblFile.getVectorFilePath(EmblFile2);
        input2     = Util.getFileNameAndExt(inputPath2);

        Vector<Integer>GenomeFile3    = properties.getInputID("GenomeFile",PortInputUP);
        inputPath3 = GenomeFile.getVectorFilePath(GenomeFile3);
        input3     = Util.getFileNameAndExt(inputPath3);
        //INSERT YOUR INPUT TEST HERE
        if (FastaFile1.isEmpty()||input1.equals("Unknown")||input1.equals("")){
            setStatus(status_BadRequirements,"No FastaFile found.");
            return false;
        }
        //Check if it's else or not
        //else 
        if (EmblFile2.isEmpty()||input2.equals("Unknown")||input2.equals("")){
            setStatus(status_BadRequirements,"No EmblFile found.");
            return false;
        }
        //Check if it's else or not
        //else 
        if (GenomeFile3.isEmpty()||input3.equals("Unknown")||input3.equals("")){
            setStatus(status_BadRequirements,"No GenomeFile found.");
            return false;
        }

        //INSERT DOCKER SHARED FILES COPY HERE
        if (!Util.CreateDir(inputPath) && !Util.DirExists(inputPath)){
            setStatus(status_BadRequirements,"Not able to create INPUTS directory files");
            return false;
        }
        if (!Util.CreateDir(outputPath) && !Util.DirExists(outputPath)){
            setStatus(status_BadRequirements,"Not able to create OUTPUTS directory files");
            return false;
        }

        inputPathDo1 = outputPath+File.separator+"INPUTS"+File.separator+input1;
        if (!(Util.copy(inputPath1,inputPathDo1))){
            setStatus(status_BadRequirements,"Not able to copy files used by docker container");
            return false;
        }
        inputInDo1 = doSharedFolder+File.separator+"INPUTS"+File.separator+input1;
        input1 = Util.getFileName(inputPath1);

        inputPathDo2 = outputPath+File.separator+"INPUTS"+File.separator+input2;
        if (!(Util.copy(inputPath2,inputPathDo2))){
            setStatus(status_BadRequirements,"Not able to copy files used by docker container");
            return false;
        }
        inputInDo2 = doSharedFolder+File.separator+"INPUTS"+File.separator+input2;
        input2 = Util.getFileName(inputPath2);

        inputPathDo3 = outputPath+File.separator+"INPUTS"+File.separator+input3;
        if (!(Util.copy(inputPath3,inputPathDo3))){
            setStatus(status_BadRequirements,"Not able to copy files used by docker container");
            return false;
        }
        inputInDo3 = doSharedFolder+File.separator+"INPUTS"+File.separator+input3;
        input3 = Util.getFileName(inputPath3);


        // TEST Docker initialisation
        doName = Docker.getContainersVal(doName);
        if (!dockerInit(outputPath,doSharedFolder,doName,doImage)){
            Docker.cleanContainers(doName);
            setStatus(status_BadRequirements,"Not able to initiate docker container");
            return false;
         } else {
            properties.put("DOCKERName",doName);
         }

        return true;
    }
    @Override
    public String[] init_createCommandLine() {

        // In case program is started without edition
        pgrmStartWithoutEdition(properties);

        //Create ouputs
        output1 = outputPath+File.separator+"OutpuOf_"input1+"_"input2+"_"input3".".est2genome";
        outputInDo1 = doSharedFolder+File.separator+"OutpuOf_"input1+"_"input2+"_"input3".".est2genome";
        
        // Program and Options
        String options = "";
        if (properties.isSet("Other_Options_1"))
            options += Util.findOptionsNew(Other_Options_1,properties);
        if (properties.isSet("Returned_Options_1"))
            options += Util.findOptionsNew(Returned_Options_1,properties);
        if (properties.isSet("Returned_Options_2"))
            options += Util.findOptionsNew(Returned_Options_2,properties);
        if (properties.isSet("Advanced_Options_1"))
            options += Util.findOptionsNew(Advanced_Options_1,properties);
        if (properties.isSet("Advanced_Options_2"))
            options += Util.findOptionsNew(Advanced_Options_2,properties);
        if (properties.isSet("Advanced_Options_3"))
            options += Util.findOptionsNew(Advanced_Options_3,properties);
        if (properties.isSet("Advanced_Options_4"))
            options += Util.findOptionsNew(Advanced_Options_4,properties);
        
        
        // Command line creation
        String[] com = new String[30];
        for (int i=0; i<com.length;i++) com[i]="";
        
        com[0]= "cmd.exe"; // Windows will de remove if another os is used
        com[1]= "/C";      // Windows will de remove if another os is used
        com[2]= properties.getExecutable();
        com[3]= "exec "+doName+" "+doPgrmPath;
        com[4]= options;
        if !(inputInDo1.equals("Unknown")||inputInDo1.equals("")) {
            com[5]= "-estsequence "+inputInDo1;
        }
        if !(inputInDo2.equals("Unknown")||inputInDo2.equals("")) {
            com[6]= "-estsequence "+inputInDo2;
        }
        if !(inputInDo3.equals("Unknown")||inputInDo3.equals("")) {
            com[7]= "-genomesequence "+inputInDo3;
        }
        com[8]= "-outfile "+outputInDo1;
        return com;
    }

        // def functions for init_createCommandLine
        // In case program is started without edition and params need to be setted
        private void pgrmStartWithoutEdition (workflow_properties properties){
            if (!(properties.isSet("Default_Options"))
                && !(properties.isSet("Other_Options"))
                && !(properties.isSet("Returned_Options"))
                && !(properties.isSet("Advanced_Options"))
            ){
                Util.getDefaultPgrmValues(properties,false);
            }
        }
        

    /*
    * Output Parsing
    */

    @Override
    public void post_parseOutput(){
        Util.deleteDir(inputPath);
        Docker.cleanContainer(doName);
        Est2genomeFile.saveFile(properties,output1,"EMBOSS_est2test","Est2genomeFile");
        Results.saveResultsPgrmOutput(properties,this.getPgrmOutput(),"EMBOSS_est2test");
    }

