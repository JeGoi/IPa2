#!/usr/bin/env python
"""
Title   : Java file editor
Author  : JG
Date    : dec 2016
Objet   : script to create Editor Java File
in      : get infos from yml
out     : print infos in java file
"""
import sys,os
import yaml
import util as u

# ===============================================
#     FUNCTION create Java File Editor
# ===============================================
def create_java_editor_file(yml,armaDir):
    progDir     = u.define_edit_path(armaDir)
    filename    = progDir+""+u.get_program_name(yml)+"Editors.java"
    out = open(filename, 'w')

    yml['FrameDefaultVariables'] = {
        "name"  : "jTextField",
        "rename": "jButton",
        "reset" : "jButton",
        "close" : "jButton",
        "stop"  : "jButton",
        "run"   : "jButton"
    }

    write_header_file(out,yml)
    write_setDefaultCloseOperation(out,yml)
    write_events(out,yml)
    write_functions(out,yml)
    write_bottom_variables(out,yml)


# ===============================================
# Header File
# ===============================================
def write_header_file(out,yml):
    out.write("/**\n"+
                "* To change this license header, choose License Headers in Project Properties.\n"+
                "* To change this template file, choose Tools | Templates\n"+
                "* and open the template in the editor.\n"+
                "*/\n"+
                "package editors;\n"+
                "\n"+
                "import configuration.Config;\n"+
                "import configuration.Util;\n"+
                "import editor.EditorInterface;\n"+
                "import java.awt.Dimension;\n"+
                "import java.awt.Frame;\n"+
                "import java.awt.Robot;\n"+
                "import java.awt.Toolkit;\n"+
                "import java.awt.image.BufferedImage;\n"+
                "import java.io.File;\n"+
                "import javax.imageio.ImageIO;\n"+
                "import javax.swing.JFileChooser;\n"+
                "import java.util.ArrayList;\n"+
                "import java.util.HashMap;\n"+
                "import javax.swing.JCheckBox;\n"+
                "import javax.swing.JComboBox;\n"+
                "import javax.swing.JFileChooser;\n"+
                "import javax.swing.JRadioButton;\n"+
                "import javax.swing.JSpinner;\n"+
                "import javax.swing.JTextField;\n"+
                "import program.*;\n"+
                "import workflows.armadillo_workflow;\n"+
                "import workflows.workflow_properties;\n"+
                "import workflows.workflow_properties_dictionnary;\n"+
                "\n"+
                "/**\n"+
                " *\n"+
                " * @author : "+yml['author']+"\n"+
                " * @Date   : "+yml['date']+"\n"+
                " */\n"+
                "\n"+
                "public class "+u.get_program_name(yml)+"Editors extends javax.swing.JDialog implements EditorInterface {\n"+
                "\n"+
                "    /**\n"+
                "     * Creates new form "+u.get_program_name(yml)+"Editors\n"+
                "     */\n"+
                "    Config config=new Config();\n"+
                "    //ConnectorInfoBox connectorinfobox;\n"+
                "    workflow_properties_dictionnary dict=new workflow_properties_dictionnary();\n"+
                "    String selected = \"\";             // Selected properties\n"+
                "    Frame frame;\n"+
                "    workflow_properties properties;\n"+
                "    armadillo_workflow  parent_workflow;\n"+
                "\n"+
                "    public final String defaultNameString=\"Name\";\n"+
                "    static final boolean default_map=true;\n")
    p = 0
    for Panel in yml['Menus']:
        if 'Panel' in Panel:
            if Panel['isMenu']:
                out.write("    public static HashMap<JCheckBox,JSpinner> DictMenuCBS"+str(p)+" = new HashMap<JCheckBox,JSpinner>();\n"+
                          "    public static HashMap<JCheckBox,JTextField> DictMenuCBT"+str(p)+" = new HashMap<JCheckBox,JTextField>();\n"+
                          "    public static HashMap<JCheckBox,JComboBox> DictMenuCBC"+str(p)+" = new HashMap<JCheckBox,JComboBox>();\n"+
                          "    public static HashMap<JRadioButton,JSpinner> DictMenuRBS"+str(p)+" = new HashMap<JRadioButton,JSpinner>();\n"+
                          "    public static HashMap<JRadioButton,JTextField> DictMenuRBT"+str(p)+" = new HashMap<JRadioButton,JTextField>();\n"+
                          "    public static ArrayList<HashMap> listDictsMenu"+str(p)+" = new ArrayList<HashMap>();\n")
            else:
                out.write("    public static HashMap<JCheckBox,JSpinner> DictCBS"+str(p)+" = new HashMap<JCheckBox,JSpinner>();\n"+
                          "    public static HashMap<JCheckBox,JTextField> DictCBT"+str(p)+" = new HashMap<JCheckBox,JTextField>();\n"+
                          "    public static HashMap<JCheckBox,JComboBox> DictCBC"+str(p)+" = new HashMap<JCheckBox,JComboBox>();\n"+
                          "    public static HashMap<JRadioButton,JSpinner> DictRBS"+str(p)+" = new HashMap<JRadioButton,JSpinner>();\n"+
                          "    public static HashMap<JRadioButton,JTextField> DictRBT"+str(p)+" = new HashMap<JRadioButton,JTextField>();\n"+
                          "    public static ArrayList<HashMap> listDicts"+str(p)+" = new ArrayList<HashMap>();\n")
            p += 1
    out.write("\n"+
              "    public "+u.get_program_name(yml)+"Editors(java.awt.Frame parent, armadillo_workflow parent_workflow){\n"+
              "        super(parent, false);\n"+
              "        this.parent_workflow=parent_workflow;\n"+
              "        //--Set variables and init\n"+
              "        frame=parent;\n")
    if p>0:
        for x in range(1,p):
            out.write("        //listDicts"+str(x)+" = Util.createListDict(DictBoxSpinner"+str(x)+",DictBoxTextField"+str(x)+",DictBoxComboBox"+str(x)+",DictRadioButtonSpinner"+str(x)+",DictRadioButtonTextField"+str(x)+");\n")
    out.write("    }\n"+
              "    \n"+
              "\n")
    write_header_variables(out,yml)

def write_header_variables(out,yml):
    out.write("\n"+
                "    /**\n"+
                "     * This method is called from within the constructor to initialize the form.\n"+
                "     * WARNING: Do NOT modify this code. The content of this method is always\n"+
                "     * regenerated by the Form Editor.\n"+
                "     */\n"+
                "    @SuppressWarnings(\"unchecked\")\n"+
                "    // <editor-fold defaultstate=\"collapsed\" desc=\"Generated Code\">//GEN-BEGIN:initComponents\n"+
                "    private void initComponents(){\n"+
                "    \n"+
                "        Menu_Buttons = new javax.swing.ButtonGroup();\n")
    if 'Docker' in yml and yml['Docker'] is not None:
        out.write("        docker_jButton = new javax.swing.JButton();\n")

    out.write("        how_jButton      = new javax.swing.JButton();\n"+
              "        "+u.get_program_name(yml)+"_tab = new javax.swing.JTabbedPane();\n"+
              "        general_jPanel1  = new javax.swing.JPanel();\n"+
              "        name_jLabel      = new javax.swing.JLabel();\n"+
              "        name_jTextField  = new javax.swing.JTextField();\n"+
              "        rename_jButton   = new javax.swing.JButton();\n"+
              "        reset_jButton    = new javax.swing.JButton();\n"+
              "        close_jButton    = new javax.swing.JButton();\n"+
              "        stop_jButton     = new javax.swing.JButton();\n"+
              "        run_jButton      = new javax.swing.JButton();\n")
    write_java_variables(out,yml,"header")

def write_setDefaultCloseOperation(out,yml):
    out.write("\n        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);\n\n")
    write_boxes_buttons_values(out,yml)
    write_organize_boxes_buttons_values(out,yml)
    write_general_panel(out,yml)
    write_program_overview(out,yml)
    write_nested_tabs(out,yml)
    out.write("\n"+
              "        pack();\n"
              "    }\n")

def write_boxes_buttons_values(out,yml):

    if 'Docker' in yml and yml['Docker'] is not None:
        write_box_and_button(out,"docker_jButton","Docker Editor",'JButton','Access to the docker editor')

    out.write("        "+u.get_program_name(yml)+"_tab.addComponentListener(new java.awt.event.ComponentAdapter() {\n"+
                "            public void componentShown(java.awt.event.ComponentEvent evt) {\n"+
                "                "+u.get_program_name(yml)+"_tab_ComponentShown(evt);\n"+
                "            }\n"+
                "        });\n"+
                "\n"+
                "        general_jPanel1.setName(\"general_jPanel1\");\n"+
                "        general_jPanel1.setPreferredSize(new java.awt.Dimension(459, 400));\n"+
                "\n")

    write_specific_button(out,"stop_jButton","Stop",'JButton','Stop this box','91','255, 0, 0')
    write_specific_button(out,"reset_jButton","Reset",'JButton','Reset to default values','91','255, 116, 0')
    write_specific_button(out,"run_jButton","Run",'JButton','Run this box','91','0, 255, 3')
    write_specific_button(out,"how_jButton","?",'JButton','About this box','51','255, 0, 255')
    write_specific_button(out,"close_jButton","Close",'JButton','Close this box','91','0, 0, 255')

    write_box_and_button(out,"name_jLabel","(re)Name",'label','Name Box')
    write_box_and_button(out,"name_jTextField","Name",'txt','Rename the box here')

    for Panel in yml['Menus']:
        if Panel['isMenu']:
            write_menu_options(out,Panel['name'])

    # Add panels and commands data
    write_pgrm_box_and_button(out,yml)

def write_pgrm_box_and_button(out,yml):
    for Panel in yml['Menus']:
        pName =  Panel['name']
        pNameI = u.create_initials(pName)
        if 'Panel' in Panel:
            for Tab in Panel['Panel']:
                tName = Tab['tab']
                tNameI = u.create_initials(tName)
                if not Panel['isTab']:
                    write_box_and_button(out,pNameI+"_"+tNameI+"_JLabel",tName,'label','Sub Items')
                if 'Arguments' in Tab:
                    for Arguments in Tab['Arguments']:
                        cName   = Arguments['name']
                        cType   = Arguments['cType']
                        cText   = u.remove_hyphen(cName)
                        cHelp   = str(Arguments['tooltip'])

                        c       = u.create_button_name(pName,tName,cName,cType)
                        v       = ""

                        write_box_and_button(out,c,cText,cType,cHelp)

                        if 'values' in Arguments and \
                            Arguments['values'] is not None and \
                            Arguments['values']['vType'] is not None:
                            vCom    = Arguments['values']
                            vType   = vCom['vType']
                            v       = u.create_value_name(pName,tName,cName,vType)
                            write_connected_value(out,v,cText,vType,cHelp,vCom)

def write_connected_value(out,v,cText,vType,cHelp,vCom):
    isSpin  = u.is_a_spinner(vType)
    isText  = u.is_a_text(vType)
    isLabel = u.is_a_label(vType)
    isCombo = u.is_a_combo(vType)
    val     = ""

    if isSpin:
        vDefault    = vCom['vDefault']
        vMin        = vCom['vMin']
        vMax        = vCom['vMax']
        vJump       = vCom['vJump']
        val         = u.return_range_value(vType,vDefault,vMin,vMax,vJump,False)
        out.write("        "+v+".setModel(new javax.swing.SpinnerNumberModel("+val+"));\n")
    if isCombo:
        val         = "\""+'", "'.join(vCom['vValues'])+"\""
        out.write("        "+v+".setModel(new javax.swing.DefaultComboBoxModel(new String[] { "+val+" }));\n")
    if isText or isLabel:
        val         = str(vCom['vValues'])
        out.write("        "+v+".setText(\""+val+"\");\n")

    out.write("        "+v+".setName(\""+v+"\"); // NOI18N\n"+
              "        "+v+".getAccessibleContext().setAccessibleDescription(\""+cHelp+"\");\n")

    if isSpin or isText or isLabel:
        out.write("        "+v+".setPreferredSize(new java.awt.Dimension(")
        if isSpin:
            out.write("115")
        if isText or isLabel:
            out.write("220")
        out.write(", 28));\n")

    if isText:
        out.write("        "+v+".addFocusListener(new java.awt.event.FocusAdapter() {\n"+
                  "            public void focusLost(java.awt.event.FocusEvent evt) {\n"+
                  "                "+v+"_FocusLost(evt);\n"+
                  "            }\n"+
                  "        });\n")
    if isSpin:
        out.write("        "+v+".addChangeListener(new javax.swing.event.ChangeListener() {\n"+
                  "            public void stateChanged(javax.swing.event.ChangeEvent evt) {\n"+
                  "                "+v+"_StateChanged(evt);\n"+
                  "            }\n"+
                  "        });\n")

    if isCombo or isText:
        out.write("        "+v+".addActionListener(new java.awt.event.ActionListener() {\n"+
                  "            public void actionPerformed(java.awt.event.ActionEvent evt) {\n"+
                  "                "+v+"_ActionPerformed(evt);\n"+
                  "            }\n"+
                  "        });\n")
    out.write("\n")

def write_box_and_button(out,cName,cText,cType,cHelp):
    isLabel = u.is_a_label(cType)
    out.write("        "+cName+".setText(\""+cText+"\");\n"+
              "        "+cName+".setName(\""+cName+"\"); // NOI18N\n")
    if isLabel:
        out.write("        "+cName+".setFont(new java.awt.Font(\"Ubuntu\", 3, 15)); // NOI18N\n")
    if cHelp != "" or cHelp is not "None":
        out.write("        "+cName+".getAccessibleContext().setAccessibleDescription(\""+cHelp+"\");\n")
    if not isLabel:
        isText = u.is_a_text(cType)
        if isText:
            out.write("        "+cName+".addFocusListener(new java.awt.event.FocusAdapter() {\n"+
                      "             public void focusLost(java.awt.event.FocusEvent evt) {\n"+
                      "                 "+cName+"_FocusLost(evt);\n"+
                      "             }\n"+
                      "        });\n")
        out.write("        "+cName+".addActionListener(new java.awt.event.ActionListener(){\n"+
                  "            public void actionPerformed(java.awt.event.ActionEvent evt){\n"+
                  "                "+cName+"_ActionPerformed(evt);\n"+
                  "            }\n"+
                  "        });\n")
    out.write("\n")

def write_specific_button(out,cName,cText,bType,bHelp,bLength,bColor):
    # look how merge it with function: add_box_and_button
    out.write("        "+cName+".setText(\""+cText+"\");\n"+
              "        "+cName+".setName(\""+cName+"\"); // NOI18N\n"+
              "        "+cName+".setMaximumSize(new java.awt.Dimension("+bLength+",29));\n"+
              "        "+cName+".setMinimumSize(new java.awt.Dimension("+bLength+",29));\n"+
              "        "+cName+".setPreferredSize(new java.awt.Dimension("+bLength+",29));\n"+
              "        "+cName+".setForeground(new java.awt.Color("+bColor+"));\n"+
              "        "+cName+".getAccessibleContext().setAccessibleDescription(\""+bHelp+"\");\n"+
              "        "+cName+".addActionListener(new java.awt.event.ActionListener(){\n"+
              "            public void actionPerformed(java.awt.event.ActionEvent evt){\n"+
              "                "+cName+"_ActionPerformed(evt);\n"+
              "            }\n"+
              "        });\n")

def write_menu_options(out,mName):
    mNameS = u.name_without_space(mName)
    out.write(  "        Menu_Buttons.add("+mNameS+");\n"+
                "        "+mNameS+".setText(\""+mName+"\");\n"+
                "        "+mNameS+".setName(\""+mNameS+"\"); // NOI18N\n"+
                "        "+mNameS+".addActionListener(new java.awt.event.ActionListener(){\n"+
                "            public void actionPerformed(java.awt.event.ActionEvent evt){\n"+
                "                "+mNameS+"_ActionPerformed(evt);\n"+
                "            }\n"+
                "        });\n")

def write_organize_boxes_buttons_values(out,yml):
    for Panel in yml['Menus']:
        pName  =  Panel['name']
        pLen   = 0
        if 'Panel' in Panel:
            if not Panel['isTab']:
                write_jPanel(out,pName,Panel['Panel'])

            if Panel['isTab']:
                pLen = len(Panel['Panel'])
                for Tab in Panel['Panel']:
                    tName = Tab['tab']
                    if 'Arguments' in Tab:
                        write_jPanel_isTab(out,pName,tName,Tab['Arguments'],pLen)

        if pLen > 1 and Panel['isTab']: # Means need a tabs
            pNameI = u.create_initials(pName)
            tmName = pNameI+"_"+pNameI
            write_tab_in_jPanel(out,pNameI,tmName)

def write_tab_in_jPanel(out,pNameI,tmName):
    out.write(  "        javax.swing.GroupLayout "+pNameI+"_Layout = new javax.swing.GroupLayout("+pNameI+"_JPanel);\n"+
                "        "+pNameI+"_JPanel.setLayout("+pNameI+"_Layout);\n"+
                "        "+pNameI+"_Layout.setHorizontalGroup(\n"+
                "            "+pNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
                "            .addComponent("+tmName+"_JTabbedPane)\n"+
                "        );\n"+
                "        "+pNameI+"_Layout.setVerticalGroup(\n"+
                "            "+pNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
                "            .addGroup("+pNameI+"_Layout.createSequentialGroup()\n"+
                "                .addComponent("+tmName+"_JTabbedPane)\n"+
                "                .addContainerGap())\n"+
                "        );\n"+
                "\n")

def write_jPanel(out,pName,Panel):
    (tabBV,dictBV,infB,infV) = u.refactor_components_notTab(pName,Panel)

    pNameI  = u.create_initials(pName)
    out.write(  "        javax.swing.GroupLayout "+pNameI+"_Layout = new javax.swing.GroupLayout("+pNameI+"_JPanel);\n"+
                "        "+pNameI+"_JPanel.setLayout("+pNameI+"_Layout);\n"+
                "        "+pNameI+"_Layout.setHorizontalGroup(\n"+
                "            "+pNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
                "                .addGroup("+pNameI+"_Layout.createSequentialGroup()\n"+
                "                    .addContainerGap()\n")
    out.write(  "                    .addGroup("+pNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n")
    for bv in tabBV:
        out.write(  "                        .addComponent("+bv+")\n")
    out.write(  "                    )\n"+
                "                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)\n"+
                "                    .addGroup("+pNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)\n")
    for bv in tabBV:
        if dictBV[bv] != "":
            out.write(  "                        .addComponent("+dictBV[bv]+", javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)\n")
    out.write(  "                    )\n"+
                "                    .addContainerGap() \n"+
                "                )\n"+
                "        );\n"+
                "        "+pNameI+"_Layout.setVerticalGroup(\n"+
                "            "+pNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
                "             .addGroup("+pNameI+"_Layout.createSequentialGroup()\n"+
                "                .addContainerGap()\n")
    x = 1
    l = len(tabBV)
    for bv in tabBV:
        out.write(  "                    .addGroup("+pNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)\n"+
                    "                        .addComponent("+bv+")\n")
        if dictBV[bv] != "":
            out.write(  "                        .addComponent("+dictBV[bv]+", javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)\n")
        out.write(  "                    )\n")
        if x < l :
            out.write(  "                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)\n")
        x+=1
    out.write(  "                 .addContainerGap()\n"+
                "             )\n"+
                "        );\n"+
                "\n")

def write_jPanel_isTab(out,pName,tName,Tab,pLen):
    dictBV   = {}
    tabBV    = []
    (tabBV,dictBV) = u.refactor_components_Tab(pName,tName,Tab)

    pNameI = u.create_initials(pName)
    tNameI = pNameI+"_"+u.create_initials(tName)
    out.write(  "        javax.swing.GroupLayout "+tNameI+"_Layout = new javax.swing.GroupLayout("+tNameI+"_JPanel);\n"+
                "        "+tNameI+"_JPanel.setLayout("+tNameI+"_Layout);\n"+
                "        "+tNameI+"_Layout.setHorizontalGroup(\n"+
                "            "+tNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
                "                .addGroup("+tNameI+"_Layout.createSequentialGroup()\n"+
                "                    .addContainerGap()\n"+
                "                    .addGroup("+tNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n")
    for bv in tabBV:
        out.write(  "                        .addComponent("+bv+")\n")
    out.write(  "                        )\n"+
                "                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)\n"+
                "                    .addGroup("+tNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)\n")
    for bv in tabBV:
        if dictBV[bv] != "":
            out.write(  "                        .addComponent("+dictBV[bv]+", javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)\n")
    out.write(  "                        )\n"+
                "                    .addContainerGap()) \n"+#)\n"+
                "        );\n"+
                "        "+tNameI+"_Layout.setVerticalGroup(\n"+
                "            "+tNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
                "             .addGroup("+tNameI+"_Layout.createSequentialGroup()\n"+
                "                .addContainerGap()\n")
    x = 1
    l = len(tabBV)
    for bv in tabBV:
        out.write(  "                    .addGroup("+tNameI+"_Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)\n"+
                    "                        .addComponent("+bv+")\n")
        if dictBV[bv] != "":
            out.write(  "                        .addComponent("+dictBV[bv]+", javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)\n")
        out.write(  "                    )\n")
        if x < l :
            out.write(  "                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)\n")
        x+=1

    out.write(  "                    .addContainerGap()) \n"+#)\n"+
                "        );\n"+
                "\n")

def write_general_panel(out,yml):
    out.write(  "        general_jPanel1.setName(\"general_jPanel1\"); // NOI18N\n"+
                "        general_jPanel1.setPreferredSize(new java.awt.Dimension(459, 400));\n"+
                "        javax.swing.GroupLayout general_jPanel1Layout = new javax.swing.GroupLayout(general_jPanel1);\n"+
                "        general_jPanel1.setLayout(general_jPanel1Layout);\n"+
                "        general_jPanel1Layout.setHorizontalGroup(\n"+
                "            general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
                "                .addGroup(general_jPanel1Layout.createSequentialGroup()\n"+
                "                    .addGroup(general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)\n"+
                "                       .addComponent(reset_jButton, javax.swing.GroupLayout.PREFERRED_SIZE, 95, javax.swing.GroupLayout.PREFERRED_SIZE)\n"+
                "                       .addGap(18, 18, 18)\n"+
                "                       .addComponent(stop_jButton, javax.swing.GroupLayout.PREFERRED_SIZE, 95, javax.swing.GroupLayout.PREFERRED_SIZE)\n"+
                "                       .addGap(18, 18, 18)\n"+
                "                       .addComponent(run_jButton, javax.swing.GroupLayout.PREFERRED_SIZE, 95, javax.swing.GroupLayout.PREFERRED_SIZE))\n"+
                "                    .addGroup(general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)\n"+
                "                        .addComponent(name_jLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 95, javax.swing.GroupLayout.PREFERRED_SIZE)\n"+
                "                        .addGap(18, 18, 18)\n"+
                "                        .addComponent(name_jTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 204, javax.swing.GroupLayout.PREFERRED_SIZE))\n")

    allMenu = []
    for Panel in yml['Menus']:
        if Panel['isMenu']:
            allMenu.append(u.name_without_space(Panel['name']))

    mLen = len(allMenu)
    x = 0
    if mLen>1:
        out.write(  "                    .addGroup(general_jPanel1Layout.createSequentialGroup()\n")
    for menu in allMenu:
        if mLen%2 != 0:
            if mLen>1 and (mLen-x-1)%2==0 and mLen-x>1:
                out.write(  "                        .addGroup(general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)\n    ")
            if x%2 != 0 and mLen>1 :
                out.write(  "                    .addGap(18, 18, 18)\n    ")
            out.write(  "                        .addComponent("+menu+")\n")
            if mLen>1 and (mLen-x-1)%2==1 and mLen-x>1:
                out.write(  "                        )\n")
        if mLen%2 == 0:
            if x%2==0:
                out.write(  "                        .addGroup(general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)\n    ")
            out.write(  "                        .addComponent("+menu+")\n")
            if x%2 == 0 and mLen>1 :
                out.write(  "                    .addGap(18, 18, 18)\n    ")
            if x%2 != 0:
                out.write(  "                        )\n")
        x+=1
    if mLen>1:
        out.write(  "                    )\n")
    out.write(  "                    .addComponent(main_jScroll))\n"+
                "        );\n"+
                "        general_jPanel1Layout.setVerticalGroup(\n"+
                "            general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
                "            .addGroup(general_jPanel1Layout.createSequentialGroup()\n"+
                "                .addContainerGap()\n"+
                "                .addGroup(general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)\n"+
                "                    .addComponent(stop_jButton, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)\n"+
                "                    .addComponent(reset_jButton)\n"+
                "                    .addComponent(run_jButton, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))\n"+
                "                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)\n"+
                "                .addGroup(general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)\n"+
                "                    .addComponent(name_jLabel)\n"+
                "                    .addComponent(name_jTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))\n")

    x = 0
    for menu in allMenu:
        if mLen%2 != 0:
            if x%2 == 0:
                out.write("                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)\n")
            if mLen>1 and (mLen-x-1)%2==0 and mLen-x>1:
                out.write("                .addGroup(general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)\n    ")
            if x%2 != 0 and mLen>1 :
                out.write("    ")
            out.write("                        .addComponent("+menu+")\n")
            if mLen>1 and (mLen-x-1)%2==1 and mLen-x>1:
                out.write(  "                        )\n")
        if mLen%2 == 0:
            if x%2 == 0:
                out.write("                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)\n")
                out.write("                .addGroup(general_jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)\n    ")
            if x%2 != 0 and mLen>1 :
                out.write("    ")
            out.write("                        .addComponent("+menu+")\n")
            if x%2 != 0:
                out.write(  "                        )\n")
        x+=1


    out.write(  "                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)\n"+
                "                .addComponent(main_jScroll, javax.swing.GroupLayout.PREFERRED_SIZE, 266, javax.swing.GroupLayout.PREFERRED_SIZE)\n"+
                "                .addContainerGap())\n"+
                "        );\n"+
                "\n")

def write_program_overview(out,yml):
    out.write("        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());\n"+
              "        getContentPane().setLayout(layout);\n"+
              "        layout.setHorizontalGroup(\n"+
              "            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
              "            .addGroup(layout.createSequentialGroup()\n"+
              "                .addComponent(close_jButton, javax.swing.GroupLayout.PREFERRED_SIZE, 95, javax.swing.GroupLayout.PREFERRED_SIZE)\n"+
              "                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)\n")
    if 'Docker' in yml and yml['Docker'] is not None:
        out.write("                .addComponent(docker_jButton)\n"+
                  "                .addGap(18, 18, 18)\n")

    out.write("                .addComponent(how_jButton, javax.swing.GroupLayout.PREFERRED_SIZE, 95, javax.swing.GroupLayout.PREFERRED_SIZE))\n"+
              "                .addComponent("+u.get_program_name(yml)+"_tab, javax.swing.GroupLayout.PREFERRED_SIZE, 308, javax.swing.GroupLayout.PREFERRED_SIZE)\n"+
              "        );\n"+
              "        layout.setVerticalGroup(\n"+
              "            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)\n"+
              "                .addGroup(layout.createSequentialGroup()\n"+
              "                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)\n")
    if 'Docker' in yml and yml['Docker'] is not None:
        out.write("                    .addComponent(docker_jButton)\n")

    out.write("                    .addComponent(close_jButton, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)\n"+
              "                    .addComponent(how_jButton, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))\n"+
              "                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)\n"+
              "                    .addComponent("+u.get_program_name(yml)+"_tab, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))\n"+
              "        );\n"+
              "\n"+
              "        "+u.get_program_name(yml)+"_tab.getAccessibleContext().setAccessibleName(\""+u.get_program_name(yml)+"\");\n"+
              "        "+u.get_program_name(yml)+"_tab.addTab(\""+u.get_program_name(yml)+"\", general_jPanel1);\n"+
              "        "+u.get_program_name(yml)+"_tab.addTab(\""+u.get_program_name(yml)+"\", general_jPanel1);\n"+
              "        "+u.get_program_name(yml)+"_tab.addComponentListener(new java.awt.event.ComponentAdapter() {\n"+
              "            public void componentShown(java.awt.event.ComponentEvent evt) {\n"+
              "                "+u.get_program_name(yml)+"_tab_ComponentShown(evt);\n"+
              "            }\n"+
              "        });\n"+
              "        main_jScroll.setViewportView(options_tab_panel);\n")

def write_nested_tabs(out,yml):
    for Panel in yml['Menus']:
        pNameI = u.create_initials(Panel['name'])
        if 'Panel' in Panel:
            out.write("        options_tab_panel.addTab(\""+pNameI+"\","+pNameI+"_JPanel);\n")
            for Tab in Panel['Panel']:
                if 'Arguments' in Tab:
                    pLen   = len(Panel['Panel'])
                    if pLen> 1 and Panel['isTab']: # Means need a tabs
                        # Create a panel to insert Arguments
                        tmName = pNameI+"_"+pNameI
                        tName  = pNameI+"_"+u.create_initials(Tab['tab'])
                        out.write("        "+tmName+"_JTabbedPane.addTab(\""+Tab['tab']+"\","+tName+"_JPanel);\n")

# ===============================================
#     def FUNCTION OF createJavaEditorFile
# in  : get spinner or text informations from csv file
# out : print infos of panel creation in java file
# ===============================================
def write_events(out,yml):
    out.write(  "    // </editor-fold>//GEN-END:initComponents\n"+
                "\n"+
                "    private void "+u.get_program_name(yml)+"_tab_ComponentShown(java.awt.event.ComponentEvent evt){//GEN-FIRST:event_"+u.get_program_name(yml)+"_tab_ComponentShown\n"+
                "        // TODO add your handling code here:\n"+
                "    }//GEN-LAST:event_"+u.get_program_name(yml)+"_tab_ComponentShown\n"+
                "    \n"+
                "    private void how_jButton_ActionPerformed(java.awt.event.ActionEvent evt){//GEN-FIRST:event_how_jButton_ActionPerformed\n"+
                "        // TODO add your handling code here:\n"+
                "        HelpEditor help = new HelpEditor(this.frame, false, properties);\n"+
                "        help.setVisible(true);\n"+
                "    }//GEN-LAST:event_how_jButton_ActionPerformed\n"+
                "\n"+
                "    private void close_jButton_ActionPerformed(java.awt.event.ActionEvent evt){//GEN-FIRST:event_close_jButton_ActionPerformed\n"+
                "        // TODO add your handling code here:\n"+
                "        this.setVisible(false);\n"+
                "    }//GEN-LAST:event_close_jButton_ActionPerformed\n"+
                "\n"+
                "    private void run_jButton_ActionPerformed(java.awt.event.ActionEvent evt){//GEN-FIRST:event_run_jButton_ActionPerformed\n"+
                "        // TODO add your handling code here:\n"+
                "        if (this.properties.isSet(\"ClassName\")){\n"+
                "            this.parent_workflow.workflow.updateDependance();\n"+
                "            programs prog=new programs(parent_workflow.workbox.getCurrentWorkflows());\n"+
                "            prog.Run(properties);\n"+
                "        }\n"+
                "    }//GEN-LAST:event_run_jButton_ActionPerformed\n"+
                "\n"+
                "    private void stop_jButton_ActionPerformed(java.awt.event.ActionEvent evt){//GEN-FIRST:event_stop_jButton_ActionPerformed\n"+
                "        // TODO add your handling code here:\n"+
                "        properties.put(\"Status\", Config.status_nothing);\n"+
                "        properties.killThread();\n"+
                "    }//GEN-LAST:event_stop_jButton_ActionPerformed\n"+
                "\n"+
                "    private void reset_jButton_ActionPerformed(java.awt.event.ActionEvent evt){//GEN-FIRST:event_reset_jButton_ActionPerformed\n"+
                "        // TODO add your handling code here:\n"+
                "        properties.load();             //--reload current properties from file\n"+
                "        this.setProperties(properties);//--Update current field\n"+
                "        this.display(properties);\n"+
                "    }//GEN-LAST:event_reset_jButton_ActionPerformed\n"+
                "\n"+
                "    private void name_jTextField_ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_name_jTextField_ActionPerformed\n"+
                "        // TODO add your handling code here:\n"+
                "        properties.put(\"Name\", name_jTextField.getText());\n"+
                "    }//GEN-LAST:event_name_jTextField_ActionPerformed\n"+
                "\n"+
                "    private void name_jTextField_FocusLost(java.awt.event.FocusEvent evt) {//GEN-FIRST:event_name_jTextField_ActionPerformed\n"+
                "        // TODO add your handling code here:\n"+
                "        properties.put(\"Name\", name_jTextField.getText());\n"+
                "    }//GEN-LAST:event_name_jTextField_ActionPerformed\n"+
                "\n")
    if 'Docker' in yml and yml['Docker'] is not None:
        out.write("    private void docker_jButton_ActionPerformed(java.awt.event.ActionEvent evt){//GEN-FIRST:event_docker_jButton_ActionPerformed\n"+
                    "        // TODO add your handling code here:\n"+
                    "        dockerEditor dock = new dockerEditor(this.frame, false, properties);\n"+
                    "        dock.setVisible(true);\n"+
                    "    }//GEN-LAST:event_docker_jButton_ActionPerformed\n"+
                    "    \n")

    write_event_menu(out,yml)
    write_event_commands(out,yml)

def write_event_menu(out,yml):
    allMenu = []
    for Panel in yml['Menus']:
        if Panel['isMenu']:
            allMenu.append(u.name_without_space(Panel['name']))
    mLen = len(allMenu)
    for menu in allMenu:
        out.write(  "    private void "+menu+"_ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_"+menu+"_ActionPerformed\n"+
                    "        // TODO add your handling code here:\n")
        if mLen > 1:
            p = 0
            out.write(  "        if (")
            for menu2 in allMenu:
                if menu != menu2:
                    if p == 0:
                        out.write(  "properties.isSet("+menu2+".getName())")
                    else :
                        out.write(  " &&\n            properties.isSet("+menu2+".getName())")
                    p+=1

            out.write(  "){\n")

            for menu2 in allMenu:
                if menu != menu2:
                    out.write(  "            properties.remove("+menu2+".getName());\n")

            out.write(  "        }\n"+
                        "        Util.buttonEventSpinner(properties,"+menu+",null);\n"+
                        "        menuFields(properties);\n")
        out.write(  "    }//GEN-LAST:event_"+menu+"_ActionPerformed\n"+
                    "    \n")

def  write_event_commands(out,yml):
    for Panel in yml['Menus']:
        pName   =  Panel['name']
        if 'Panel' in Panel:
            for Tab in Panel['Panel']:
                tName   =  Tab['tab']
                if 'Arguments' in Tab:
                    for Arguments in Tab['Arguments']:
                        cName     = Arguments['name']
                        cType     = Arguments['cType']
                        childrens = Arguments['parentOf']
                        opposites = Arguments['oppositeTo']

                        c       = u.create_button_name(pName,tName,cName,cType)
                        v       = ""
                        vType   = ""
                        if 'values' in Arguments and \
                            Arguments['values'] is not None and \
                            Arguments['values']['vType'] is not None:
                            vCom    = Arguments['values']
                            vType   = vCom['vType']
                            v       = u.create_value_name(pName,tName,cName,vType)

                            write_event_command_value(out,c,cType,v,vType)

                        write_event_command(out,c,cType,v,vType,childrens,opposites)


def write_event_command(out,c,cType,v,vType,childrens,opposites):

    out.write(  "    private void "+c+"_ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_"+c+"_ActionPerformed\n"+
                "        // TODO add your handling code here:\n")
    if childrens != None :
        write_event_command_is_a_parent(out,c,childrens)
    if opposites != None :
        write_event_command_is_opposite_to(out,opposites)

    vType = u.get_value_java_type(vType)
    isCheckBox = u.is_a_box(cType)
    isButton   = u.is_a_button(cType)

    if v == "":
        v = 'null'
    if isCheckBox:
        if vType == "" or 'Spinner' in vType:
            out.write("        Util.boxEventSpinner(properties,"+c+","+v+");\n")
        if 'TextField' in vType:
            out.write("        Util.boxEventText(properties,"+c+","+v+");\n")
        if 'ComboBox' in vType:
            out.write("        Util.boxEventComboBox(properties,"+c+","+v+");\n")
        if 'Dir' in vType:
            write_event_command_dir(out,c,cType,v,vType)
    if isButton:
        if vType == "" or 'Spinner' in vType:
            out.write("        Util.buttonEventSpinner(properties,"+c+","+v+");\n")
        if 'TextField' in vType:
            out.write("        Util.buttonEventText(properties,"+c+","+v+");\n")

    out.write("    }//GEN-LAST:event_"+c+"_ActionPerformed\n")

def write_event_command_is_a_parent(out,c,childrens):
    out.write(  "        if (properties.isSet("+c+".getName())) {\n")
    for child in childrens:
        out.write("            "+child[0]+".setEnabled(true);\n")
        if child[1] != None and child[1] != '':
            out.write(  "            if (!properties.isSet("+child[0]+".getName())) {\n"+
                        "                "+child[1]+".setEnabled(false);\n"+
                        "              }\n")
    out.write(  "        } else {\n")
    for child in childrens:
        out.write("            "+child[0]+".setEnabled(false);\n")
        if child[1] != None and child[1] != '':
            out.write(  "                "+child[1]+".setEnabled(false);\n")
    out.write(  "        }\n"+
                "\n")

def write_event_command_is_opposite_to(out,opposites):
    x=0
    oLen = len(opposites)
    out.write(  "        if (\n")
    for o in opposites:
        out.write(  "            properties.isSet("+o[0]+".getName())")
        if x < (oLen-1) and oLen > 1:
            out.write(  " && \n")
        x+=1
    out.write(  "\n        ){\n")
    for o in opposites:
        out.write(  "            properties.remove("+o[0]+".getName());\n"+
                    "            "+o[0]+".setSelected(false);\n")
        if o[1] != "":
            out.write(  "            "+o[1]+".setEnabled(false);\n")
    out.write(  "        }\n"+
                "\n")

def write_event_command_dir(out,c,cType,v,vType):
    print 'is a directory. Need to be done'

def write_event_command_value(out,c,cType,v,vType):
    d = u.get_java_eventHandler_simple(vType)

    vType = u.get_value_java_type(vType)
    isCheckBox = u.is_a_box(cType)
    isButton   = u.is_a_button(cType)

    action = "ActionPerformed"
    if vType == "" or 'Spinner' in vType:
        action = "StateChanged"
    if 'TextField' in vType:
        action = "FocusLost"
    if 'ComboBox' in vType:
        action = "ActionPerformed"

    out.write(  "    private void "+v+"_"+d[3]+"("+d[4]+""+d[2]+" evt) {//GEN-FIRST:event_"+v+"_"+d[0]+"\n"+
                "        // TODO add your handling code here:\n")

    if isCheckBox:
        if vType == "" or 'Spinner' in vType:
            out.write("        Util.boxEventSpinner(properties,"+c+","+v+");\n")
        if 'TextField' in vType:
            out.write("        Util.boxEventText(properties,"+c+","+v+");\n")
        if 'ComboBox' in vType:
            out.write("        Util.boxEventComboBox(properties,"+c+","+v+");\n")
        if 'Dir' in vType:
            write_event_command_dir_value(out,c,cType,v,vType)
    if isButton:
        if vType == "" or 'Spinner' in vType:
            out.write("        Util.buttonEventSpinner(properties,"+c+","+v+");\n")
        if 'TextField' in vType:
            out.write("        Util.buttonEventText(properties,"+c+","+v+");\n")

    out.write(  "    }//GEN-LAST:event_"+v+"_"+d[0]+"\n"+
                "\n")

    if 'TextField' in vType:
        action = "ActionPerformed"
        out.write(  "    private void "+v+"_ActionPerformed("+d[4]+"ActionEvent evt) {//GEN-FIRST:event_"+v+"_"+d[0]+"\n"+
                    "        // TODO add your handling code here:\n")

        if isCheckBox:
            if 'TextField' in vType:
                out.write("        Util.boxEventText(properties,"+c+","+v+");\n")
        if isButton:
            if vType == "" or 'Spinner' in vType:
                out.write("        Util.buttonEventSpinner(properties,"+c+","+v+");\n")
            if 'TextField' in vType:
                out.write("        Util.buttonEventText(properties,"+c+","+v+");\n")

        out.write(  "    }//GEN-LAST:event_"+v+"_"+d[0]+"\n"+
                    "\n")

def write_event_command_dir_value(out,c,cType,v,vType):
    print 'is a directory. Need to be done'
    out.write(  "        JFileChooser d;\n"+
                "        if (this."+v+".getText().isEmpty()):\n"+
                "            d=new JFileChooser(config.getExplorerPath());\n"+
                "         else:\n"+
                "            d=new JFileChooser(this."+v+".getText());\n"+
                "        \n")
    if v.endswith('DirRep'):
        out.write("        d.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);\n")
    else:
        out.write("        d.setFileSelectionMode(JFileChooser.FILES_ONLY);\n")

    out.write("        d.setAcceptAllFileFilterUsed(false);\n")
    if v.endswith('DirFiles'):
        out.write("        d.setMultiSelectionEnabled(true);\n")
    else:
        out.write("        d.setMultiSelectionEnabled(false);\n")
    out.write(  "        int result = d.showOpenDialog(this);\n"+
                "        \n"+
                "        if (result==JFileChooser.APPROVE_OPTION){\n"+
                "            File dir = d.getSelectedFile();\n"+
                "            \n"+
                "            // Set the text\n"+
                "            String s = dir.getAbsolutePath();\n"+
                "            "+v+".setText(s);\n"+
                "            properties.remove("+v+".getName());\n"+
                "            Util."+ctype+"EventText(properties,"+c+","+v+");\n"+
                "        }\n")


# ===============================================
# write_functions
# ===============================================
def write_functions(out,yml):
    write_objects_list_dictionaries(out,yml)
    write_objects_dictionaries(out,yml)
    write_configuration_object_properties(out,yml)
    write_set_properties(out,yml)
    write_default_program_values(out,yml)
    write_menu_fields(out,yml)
    write_save_image(out,yml)

def write_objects_list_dictionaries(out,yml):
    out.write(  "    /*******************************************************************\n"+
                "     * Perpare List Dictionaries\n"+
                "     ******************************************************************/\n"+
                "\n"+
                "    /**\n"+
                "     * Perpare List of Dictionaries\n"+
                "     * @param properties\n"+
                "     */\n"+
                "\n"+
                "    public void perpareListDictionaries(workflow_properties properties){\n")
    p = 0
    for Panel in yml['Menus']:
        if 'Panel' in Panel:
            if Panel['isMenu']:
                out.write("        Util.dictsReset(listDictsMenu"+str(p)+",DictMenuCBS"+str(p)+",DictMenuCBT"+str(p)+",DictMenuCBC"+str(p)+",DictMenuRBS"+str(p)+",DictMenuRBT"+str(p)+");\n")
            else:
                out.write("        Util.dictsReset(listDicts"+str(p)+",DictCBS"+str(p)+",DictCBT"+str(p)+",DictCBC"+str(p)+",DictRBS"+str(p)+",DictRBT"+str(p)+");\n")
            p += 1
    out.write("    }\n"+
              "\n")

def write_objects_dictionaries(out,yml):
    out.write(  "    /*******************************************************************\n"+
                "     * Perpare Dictionaries\n"+
                "     ******************************************************************/\n"+
                "\n"+
                "    /**\n"+
                "     * Perpare Dictionaries by adding commands\n"+
                "     * @param properties\n"+
                "     */\n"+
                "\n"+
                "    public void perpareDictionaries(workflow_properties properties){\n")
    p = 0
    for Panel in yml['Menus']:
        pName   = Panel['name']
        if 'Panel' in Panel:
            for Tab in Panel['Panel']:
                tName   = Tab['tab']
                if 'Arguments' in Tab:
                    for Arguments in Tab['Arguments']:
                        cName   = Arguments['name']
                        cType   = Arguments['cType']
                        c       = u.create_button_name(pName,tName,cName,cType)
                        vType   = ""
                        v       = "null"
                        if 'values' in Arguments and \
                            Arguments['values'] is not None and \
                            Arguments['values']['vType'] is not None:
                            vType   = Arguments['values']['vType']
                            v       = u.create_value_name(pName,tName,cName,vType)

                        cType = u.get_box_type(cType)
                        if vType != "":
                            vType = u.get_value_java_type(vType)

                        if 'CheckBox' in cType:
                            if vType == "" or 'Spinner' in vType:
                                if Panel['isMenu']:
                                    out.write("        DictMenuCBS"+str(p)+".put("+c+","+v+");\n")
                                else:
                                    out.write("        DictCBS"+str(p)+".put("+c+","+v+");\n")
                            if 'TextField' in vType:
                                if Panel['isMenu']:
                                    out.write("        DictMenuCBT"+str(p)+".put("+c+","+v+");\n")
                                else:
                                    out.write("        DictCBT"+str(p)+".put("+c+","+v+");\n")
                            if 'ComboBox' in vType:
                                if Panel['isMenu']:
                                    out.write("        DictMenuCBC"+str(p)+".put("+c+","+v+");\n")
                                else:
                                    out.write("        DictCBC"+str(p)+".put("+c+","+v+");\n")

                        if 'Button' in cType:
                            if vType == "" or 'Spinner' in vType:
                                if Panel['isMenu']:
                                    out.write("        DictMenuRBS"+str(p)+".put("+c+","+v+");\n")
                                else:
                                    out.write("        DictRBS"+str(p)+".put("+c+","+v+");\n")
                            if 'TextField' in vType:
                                if Panel['isMenu']:
                                    out.write("        DictMenuRBT"+str(p)+".put("+c+","+v+");\n")
                                else:
                                    out.write("        DictRBT"+str(p)+".put("+c+","+v+");\n")
            p += 1
    out.write("    }\n"+
              "\n")


def write_configuration_object_properties(out,yml):
    out.write("\n    /*******************************************************************\n"+
                "     * Set the configuration properties for this object\n"+
                "     ******************************************************************/\n"+
                "\n"+
                "    @Override\n"+
                "    public void display(workflow_properties properties){\n"+
                "        this.properties=properties;\n"+
                "        initComponents();\n"+
                "        setIconImage(Config.image);\n"+
                "        // Set position\n"+
                "        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();\n"+
                "        Dimension d = getSize();\n"+
                "        setLocation((screenSize.width-d.width)/2,\n"+
                "                (screenSize.height-d.height)/2);\n"+
                "        \n"+
                "        // Set the program properties\n"+
                "        this.setProperties(properties);\n"+
                "        \n"+
                "        this.setAlwaysOnTop(true);\n"+
                "        this.setVisible(true);\n"+
                "    }\n"+
                "\n")
def write_set_properties(out,yml):
    out.write("    /*******************************************************************\n"+
              "     * Sets for Properties\n"+
              "     ******************************************************************/\n"+
              "\n"+
              "    /**\n"+
              "     * Set Properties\n"+
              "     * @param properties\n"+
              "     */\n"+
              "\n"+
              "    public void setProperties(workflow_properties properties){\n"+
              "        this.properties=properties;\n"+
              "        setTitle(properties.getName());\n"+
              "        //if (this.properties.isSet(\"Description\")) this.Notice.setText(properties.get(\"Description\"));\n"+
              "        \n"+
              "        // Prepare dictionaries\n"+
              "        this.perpareListDictionaries(properties);\n"+
              "        this.perpareDictionaries(properties);\n"+
              "        // Properties Default Options\n"+
              "        this.defaultPgrmValues(properties);\n"+
              "        // Update Saved Properties => usp\n")
    p = 0
    for Panel in yml['Menus']:
        if 'Panel' in Panel:
            if Panel['isMenu']:
                out.write("        Util.updateSavedProperties(properties,listDictsMenu"+str(p)+",name_jTextField);\n")
            else:
                out.write("        Util.updateSavedProperties(properties,listDicts"+str(p)+",name_jTextField);\n"+
                          "        properties.put(\""+u.name_without_space(Panel['name'])+"\",true);\n")
            p += 1
    out.write("        // Set the menu\n"+
              "        this.menuFields(properties);\n"+
              "    }\n"+
              "\n"+
              "    public void setProperties(String filename, String path){\n"+
              "        workflow_properties tmp=new workflow_properties();\n"+
              "        tmp.load(filename, path);\n"+
              "        this.properties=tmp;\n"+
              "        setTitle(properties.getName());\n"+
              "    }\n"+
              "\n")


def write_default_program_values(out,yml):
    allMenu = []
    for Panel in yml['Menus']:
        if Panel['isMenu']:
            allMenu.append(u.name_without_space(Panel['name']))
    mLen = len(allMenu)

    out.write("    /*******************************************************************\n"+
              "     * Set With default program values present in properties file\n"+
              "     ******************************************************************/\n"+
              "    private void defaultPgrmValues(workflow_properties properties){\n")
    if mLen > 0:
        p = 0
        out.write("        boolean b = true;\n"+
                  "        if (")
        for menu in allMenu:
            if p > 0:
                out.write("        && ")
            out.write("!(properties.isSet("+menu+".getName()))\n")
            p+=1

        out.write("        ){\n"+
                  "            b = false;\n"+
                  "        }\n"+
                  "        \n"+
                  "        Util.getDefaultPgrmValues(properties,b);\n")
    else:
        out.write("        //Util.getDefaultPgrmValues(properties,boolean to test the presence of a default value);\n")

    out.write("    }\n"+
              "    \n")

def write_menu_fields(out,yml):
    allMenu    = []
    allNotMenu = []
    p = 0
    for Panel in yml['Menus']:
        if 'Panel' in Panel:
            if Panel['isMenu']:
                allMenu.append([u.name_without_space(Panel['name']),str(p)])
            if not Panel['isMenu']:
                allNotMenu.append([u.name_without_space(Panel['name']),str(p)])
            p+=1
    mLen = len(allMenu)

    # Menu Fields Options setting
    p = 0
    for Panel in yml['Menus']:
        pNameS = u.name_without_space(Panel['name'])
        if 'Panel' not in Panel:
            out.write("    /*******************************************************************\n"+
                      "     * Set Menu fields\n"+
                      "     ******************************************************************/\n"+
                      "\n"+
                      "    private void menuFields(workflow_properties properties){\n"+
                      "        if (properties.isSet("+pNameS+".getName())){\n"+
                      "            "+pNameS+".setSelected(true);\n")
            for menu in allMenu:
                out.write("            Util.enabled_Advanced_Options(properties,false,listDictsMenu"+menu[1]+");\n")
            out.write("        }\n")

        if 'Panel' in Panel and Panel['isMenu']:
            out.write("        else if (properties.isSet("+pNameS+".getName())){\n"+
                      "            "+pNameS+".setSelected(true);\n")
            for menu in allMenu:
                out.write("            Util.enabled_Advanced_Options(properties,")
                if pNameS != menu[0]:
                    out.write("false")
                if pNameS == menu[0]:
                    out.write("true")
                out.write(",listDictsMenu"+menu[1]+");\n")
            out.write("        }\n")

    for notMenu in allNotMenu:
        out.write("        Util.enabled_Advanced_Options(properties,true,listDicts"+notMenu[1]+");\n")

    out.write("    }\n"+
              "\n")

def write_save_image(out,yml):
    out.write("\n    /*******************************************************************\n"+
                "     * Save Image\n"+
                "     ******************************************************************/\n"+
                "\n"+
                "    public void saveImage(String filename){\n"+
                "        BufferedImage bi;\n"+
                "        try{\n"+
                "            bi = new Robot().createScreenCapture(this.getBounds());\n"+
                "            ImageIO.write(bi, \"png\", new File(filename));\n"+
                "            this.setVisible(false);\n"+
                "         } catch (Exception ex) {\n"+
                "            Config.log(\"Unable to save \"+filename+\" dialog image\");\n"+
                "        }\n"+
                "    }\n"+
                "\n")

# ===============================================
# write_bottom_variables
# ===============================================
def write_bottom_variables(out,yml):
    out.write("    // Variables declaration - do not modify//GEN-BEGIN:variables\n"+
              "    private javax.swing.JButton how_jButton;\n"
              "    private javax.swing.JTabbedPane "+u.get_program_name(yml)+"_tab;\n"+
              "    private javax.swing.JPanel general_jPanel1;\n"+
              "    private javax.swing.JLabel name_jLabel;\n"+
              "    private javax.swing.JTextField name_jTextField;\n"+
              "    private javax.swing.JButton rename_jButton;\n"+
              "    private javax.swing.JButton reset_jButton;\n"+
              "    private javax.swing.JButton close_jButton;\n"+
              "    private javax.swing.JButton stop_jButton;\n"+
              "    private javax.swing.JButton run_jButton;\n"+
              "    private javax.swing.ButtonGroup Menu_Buttons;\n")
    if 'Docker' in yml and yml['Docker'] is not None:
        out.write("    private javax.swing.JButton docker_jButton;\n")
    write_java_variables(out,yml,"bottom")
    out.write("    // End of variables declaration//GEN-END:variables\n"+
                "    }\n"+
                "\n")

# ===============================================
# write_java_variables (header and bottom)
# ===============================================
def write_java_variables(out,yml,where):
    for Panel in yml['Menus']:
        if Panel['isMenu']:
            pNameS = u.name_without_space(Panel['name'])
            if (where == "header"):
                out.write("        "+pNameS+" = new javax.swing.JRadioButton();\n")
            if (where == "bottom"):
                out.write("    private javax.swing.JRadioButton "+pNameS+";\n")
    #
    # Always add main scroll and tab panel
    #

    if (where == "header"):
        out.write("        main_jScroll = new javax.swing.JScrollPane();\n")
        out.write("        options_tab_panel = new javax.swing.JTabbedPane();\n")
    if (where == "bottom"):
        out.write("    private javax.swing.JScrollPane main_jScroll;\n")
        out.write("    private javax.swing.JTabbedPane options_tab_panel;\n")

    #
    # Think about adding or not a default option
    # Now, a default option without data is needed then add extra data
    #

    for Panel in yml['Menus']:
        pName = Panel['name']
        pNameI = u.create_initials(pName)
        if 'Panel' in Panel:
            # Create a panel to insert Arguments
            if (where == "header"):
                out.write("        "+pNameI+"_JPanel = new javax.swing.JPanel();\n")
            if (where == "bottom"):
                out.write("    private javax.swing.JPanel "+pNameI+"_JPanel;\n")

            pLen = len(Panel['Panel'])
            if pLen>1 and Panel['isTab']: # Means need a tabs
                tmName = pNameI+"_"+pNameI
                if (where == "header"):
                    out.write("        "+tmName+"_JTabbedPane = new javax.swing.JTabbedPane();\n")
                if (where == "bottom"):
                    out.write("    private javax.swing.JTabbedPane "+tmName+"_JTabbedPane;\n")
            for Tab in Panel['Panel']:
                if 'Arguments' in Tab:
                    tName  = Tab['tab']
                    tNameI = u.create_initials(tName)
                    if pLen>1 and Panel['isTab']: # Means need a tabs
                        if (where == "header"):
                            out.write("        "+pNameI+"_"+tNameI+"_JPanel = new javax.swing.JPanel();\n")
                        if (where == "bottom"):
                            out.write("    private javax.swing.JPanel "+pNameI+"_"+tNameI+"_JPanel;\n")

                    if not Panel['isTab']: # Means need a Label instead of tabs
                        if (where == "header"):
                            out.write("        "+pNameI+"_"+tNameI+"_JLabel = new javax.swing.JLabel();\n")
                        if (where == "bottom"):
                            out.write("    private javax.swing.JLabel "+pNameI+"_"+tNameI+"_JLabel;\n")

                    for Arguments in Tab['Arguments']:
                        cName   = Arguments['name']
                        cType   = Arguments['cType']
                        c       = u.create_button_name(pName,tName,cName,cType)
                        if (where == "header"):
                            out.write("        "+c+" = new javax.swing."+u.get_box_type(cType)+"();\n")
                        if (where == "bottom"):
                            out.write("    private javax.swing."+u.get_box_type(cType)+" "+c+";\n")
                        if 'values' in Arguments and \
                            Arguments['values'] is not None and \
                            Arguments['values']['vType'] is not None:
                            v       = ""
                            vType   = Arguments['values']['vType']
                            v       = u.create_value_name(pName,tName,cName,vType)
                            if (where == "header"):
                                out.write("        "+v+" = new javax.swing."+u.get_value_java_type(vType)+"();\n")
                            if (where == "bottom"):
                                out.write("    private javax.swing."+u.get_value_java_type(vType)+" "+v+";\n")
