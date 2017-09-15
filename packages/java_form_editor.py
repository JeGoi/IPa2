#!/usr/bin/env python
"""
Title   : Java form editor file
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
#     FUNCTION create Java File Editor Form
# ===============================================
def create_java_editor_form(yml,armaDir):
    progDir     = u.define_edit_path(armaDir)
    filename    = progDir+""+u.get_program_name(yml)+"Editors.form"
    out = open(filename, 'w')

    yml['FrameDefaultVariables'] = {
        "name"  : "jTextField",
        "rename": "jButton",
        "reset" : "jButton",
        "close" : "jButton",
        "stop"  : "jButton",
        "run"   : "jButton"
    }

    write_begin(out,yml)
    write_layout(out,yml)
    write_container(out,yml)
    write_close_form(out,yml)

# ===============================================
#  SUB FUNCTIONS TO CREATE Java File Editor
# ===============================================
#
# Header and variables
#
def write_begin(out,yml):
    write_begin_file(out,yml)
#
# Header and variables
#
def write_begin_file(out,yml):
    out.write(  "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"+
                "\n"+
                "<Form version=\"1.5\" maxVersion=\"1.9\" type=\"org.netbeans.modules.form.forminfo.JDialogFormInfo\">\n")
    if len(yml['Menus'])>0:
        out.write(  "    <NonVisualComponents>\n"+
                    "        <Component class=\"javax.swing.ButtonGroup\" name=\"Menu_Buttons\">\n"+
                    "        </Component>\n"+
                    "    </NonVisualComponents>\n")

    out.write(  "    <Properties>\n"+
                "        <Property name=\"defaultCloseOperation\" type=\"int\" value=\"2\"/>\n"+
                "    </Properties>\n"+
                "    <SyntheticProperties>\n"+
                "        <SyntheticProperty name=\"formSizePolicy\" type=\"int\" value=\"1\"/>\n"+
                "        <SyntheticProperty name=\"generateCenter\" type=\"boolean\" value=\"false\"/>\n"+
                "    </SyntheticProperties>\n"+
                "    <AuxValues>\n"+
                "        <AuxValue name=\"FormSettings_autoResourcing\" type=\"java.lang.Integer\" value=\"0\"/>\n"+
                "        <AuxValue name=\"FormSettings_autoSetComponentName\" type=\"java.lang.Boolean\" value=\"false\"/>\n"+
                "        <AuxValue name=\"FormSettings_generateFQN\" type=\"java.lang.Boolean\" value=\"true\"/>\n"+
                "        <AuxValue name=\"FormSettings_generateMnemonicsCode\" type=\"java.lang.Boolean\" value=\"false\"/>\n"+
                "        <AuxValue name=\"FormSettings_i18nAutoMode\" type=\"java.lang.Boolean\" value=\"false\"/>\n"+
                "        <AuxValue name=\"FormSettings_layoutCodeTarget\" type=\"java.lang.Integer\" value=\"1\"/>\n"+
                "        <AuxValue name=\"FormSettings_listenerGenerationStyle\" type=\"java.lang.Integer\" value=\"0\"/>\n"+
                "        <AuxValue name=\"FormSettings_variablesLocal\" type=\"java.lang.Boolean\" value=\"false\"/>\n"+
                "        <AuxValue name=\"FormSettings_variablesModifier\" type=\"java.lang.Integer\" value=\"2\"/>\n"+
                "    </AuxValues>\n"+
                "\n")

def write_layout(out,yml):
    write_layout_start(out,yml)
    write_command_component(out,8,"close_jButton","Close","jButton",91,[0,0,"ff"],"Close this box",None,False)
    write_command_component(out,8,"ClusterProgram_jButton","Cluster Options","jButton",91,[0,0,"ff"],"Access to cluster properties",None,False)
    write_command_component(out,8,"how_jButton","?","jButton",51,["ff",0,"ff"],"About this box",None,False)
    if 'Docker' in yml and yml['Docker'] is not None:
        write_command_component(out,8,"docker_jButton","Docker Editor",'JButton',91,None,'Access to the docker editor',None,False)

def write_layout_start(out,yml):
    out.write(  "    <Layout>\n"+
                "        <DimensionLayout dim=\"0\">\n"+
                "            <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n"+
                "                <Group type=\"102\" attributes=\"0\">\n"+
                "                    <Component id=\"close_jButton\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                    <EmptySpace type=\"separate\" max=\"-2\" attributes=\"0\"/>\n"+
                "                    <Component id=\"ClusterProgram_jButton\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                    <EmptySpace max=\"32767\" attributes=\"0\"/>\n")
    if 'Docker' in yml and yml['Docker'] is not None:
        out.write(  "                    <Component id=\"docker_jButton\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                    "                    <EmptySpace type=\"separate\" max=\"-2\" attributes=\"0\"/>\n")

    out.write(  "                    <Component id=\"how_jButton\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                </Group>\n"+
                "                <Component id=\""+u.get_program_name(yml)+"_tab\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "            </Group>\n"+
                "        </DimensionLayout>\n"+
                "        <DimensionLayout dim=\"1\">\n"+
                "            <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n"+
                "                <Group type=\"102\" attributes=\"0\">\n"+
                "                    <Group type=\"103\" groupAlignment=\"3\" attributes=\"0\">\n"+
                "                        <Component id=\"close_jButton\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                        <Component id=\"ClusterProgram_jButton\" alignment=\"3\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                        <Component id=\"how_jButton\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")

    if 'Docker' in yml and yml['Docker'] is not None:
        out.write(  "                    <Component id=\"docker_jButton\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")

    out.write(  "                    </Group>\n"+
                "                    <EmptySpace max=\"-2\" attributes=\"0\"/>\n"+
                "                    <Component id=\""+u.get_program_name(yml)+"_tab\" min=\"-2\" max=\"32767\" attributes=\"0\"/>\n"+
                "                </Group>\n"+
                "            </Group>\n"+
                "        </DimensionLayout>\n"+
                "    </Layout>\n"+
                "\n"+
                "    <SubComponents>\n")

def write_container(out,yml):
    out.write(  "    <Container class=\"javax.swing.JTabbedPane\" name=\""+u.get_program_name(yml)+"_tab\">\n"+
                "      <AccessibilityProperties>\n"+
                "        <Property name=\"AccessibleContext.accessibleName\" type=\"java.lang.String\" value=\""+u.get_program_name(yml)+"\"/>\n"+
                "      </AccessibilityProperties>\n"+
                "      <Events>\n"+
                "        <EventHandler event=\"componentShown\" listener=\"java.awt.event.ComponentListener\" parameters=\"java.awt.event.ComponentEvent\" handler=\""+u.get_program_name(yml)+"_tab_ComponentShown\"/>\n"+
                "      </Events>\n"+
                "      <AuxValues>\n"+
                "        <AuxValue name=\"JavaCodeGenerator_SerializeTo\" type=\"java.lang.String\" value=\""+u.get_program_name(yml)+"\"/>\n"+
                "      </AuxValues>\n"+
                "\n"+
                "      <Layout class=\"org.netbeans.modules.form.compat2.layouts.support.JTabbedPaneSupportLayout\"/>\n"+
                "      <SubComponents>\n"+
                "        <Container class=\"javax.swing.JPanel\" name=\"general_jPanel1\">\n"+
                "          <Properties>\n"+
                "            <Property name=\"name\" type=\"java.lang.String\" value=\"general_jPanel1\" noResource=\"true\"/>\n"+
                "            <Property name=\"preferredSize\" type=\"java.awt.Dimension\" editor=\"org.netbeans.beaninfo.editors.DimensionEditor\">\n"+
                "              <Dimension value=\"[459, 400]\"/>\n"+
                "            </Property>\n"+
                "          </Properties>\n"+
                "          <Constraints>\n"+
                "            <Constraint layoutClass=\"org.netbeans.modules.form.compat2.layouts.support.JTabbedPaneSupportLayout\" value=\"org.netbeans.modules.form.compat2.layouts.support.JTabbedPaneSupportLayout$JTabbedPaneConstraintsDescription\">\n"+
                "              <JTabbedPaneConstraints tabName=\""+u.get_program_name(yml)+"\">\n"+
                "                <Property name=\"tabTitle\" type=\"java.lang.String\" value=\""+u.get_program_name(yml)+"\"/>\n"+
                "              </JTabbedPaneConstraints>\n"+
                "            </Constraint>\n"+
                "          </Constraints>\n"+
                "\n"+
                "          <Layout>\n"+
                "            <DimensionLayout dim=\"0\">\n"+
                "              <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n"+
                "                  <Group type=\"102\" alignment=\"0\" attributes=\"0\">\n"+
                "                      <Component id=\"reset_jButton\" alignment=\"0\" min=\"-2\" pref=\"95\" max=\"-2\" attributes=\"0\"/>\n"+
                "                      <EmptySpace min=\"-2\" pref=\"10\" max=\"-2\" attributes=\"0\"/>\n"+
                "                      <Component id=\"stop_jButton\" alignment=\"0\" min=\"-2\" pref=\"95\" max=\"-2\" attributes=\"0\"/>\n"+
                "                      <EmptySpace type=\"separate\" max=\"-2\" attributes=\"0\"/>\n"+
                "                      <Component id=\"run_jButton\" alignment=\"0\" min=\"-2\" pref=\"95\" max=\"-2\" attributes=\"0\"/>\n"+
                "                  </Group>\n"+
                "                  <Group type=\"102\" alignment=\"0\" attributes=\"0\">\n"+
                "                      <Component id=\"name_jLabel\" alignment=\"0\" min=\"-2\" pref=\"95\" max=\"-2\" attributes=\"0\"/>\n"+
                "                      <EmptySpace type=\"separate\" max=\"-2\" attributes=\"0\"/>\n"+
                "                      <Component id=\"name_jTextField\" alignment=\"0\" min=\"-2\" pref=\"204\" max=\"-2\" attributes=\"0\"/>\n"+
                "                  </Group>\n")


    allMenu = []
    for Panel in yml['Menus']:
        if Panel['isMenu']:
            allMenu.append(u.name_without_space(Panel['name']))

    mLen = len(allMenu)
    if mLen>1:
        out.write(  "                  <Group type=\"102\" attributes=\"0\">\n"+
                    "                      <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n")
    x = 0
    boo  = False
    for menu in allMenu:
        if mLen%2 != 0:
            if mLen>1 and (mLen-x-1)%2==0 and mLen-x>1:
                out.write(  "                          <Group type=\"102\" alignment=\"0\" attributes=\"0\">\n    ")
                boo = True
            if x%2 != 0 and mLen>1 :
                out.write(  "                              <EmptySpace type=\"separate\" max=\"-2\" attributes=\"0\"/>\n    ")
                boo = True
            out.write(  "                          <Component id=\""+menu+"\"")
            if boo:
                out.write(" alignment=\"0\"")
            out.write(  " min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")
            if mLen>1 and (mLen-x-1)%2==1 and mLen-x>1:
                out.write(  "                          </Group>\n")
        if mLen%2 == 0:
            if x%2 == 0:
                out.write(  "                          <Group type=\"102\" alignment=\"0\" attributes=\"0\">\n    ")
                boo = True
            if x%2 != 0 and mLen>1 :
                out.write(  "                              <EmptySpace type=\"separate\" max=\"-2\" attributes=\"0\"/>\n    ")
                boo = True
            out.write(  "                          <Component id=\""+menu+"\"")
            if boo:
                out.write(" alignment=\"0\"")
            out.write(  " min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")
            if x%2 != 0:
                out.write(  "                          </Group>\n")
        x+=1
        boo = False

    if mLen>1:
        out.write(  "                      </Group>\n"+
                    "                  </Group>\n")
    out.write(  "                  <Group type=\"102\" attributes=\"0\">\n"+
                "                      <Component id=\"main_jScroll\" pref=\"0\" max=\"32767\" attributes=\"0\"/>\n"+
                "                      <EmptySpace max=\"-2\" attributes=\"0\"/>\n"+
                "                  </Group>\n"+
                "              </Group>\n"+
                "            </DimensionLayout>\n"+
                "            <DimensionLayout dim=\"1\">\n"+
                "              <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n"+
                "                  <Group type=\"102\" alignment=\"0\" attributes=\"0\">\n"+
                "                      <EmptySpace max=\"-2\" attributes=\"0\"/>\n"+
                "                      <Group type=\"103\" groupAlignment=\"3\" attributes=\"0\">\n"+
                "                          <Component id=\"stop_jButton\" alignment=\"3\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                          <Component id=\"reset_jButton\" alignment=\"3\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                          <Component id=\"run_jButton\" alignment=\"3\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                      </Group>\n"+
                "                      <EmptySpace max=\"-2\" attributes=\"0\"/>\n"+
                "                      <Group type=\"103\" groupAlignment=\"3\" attributes=\"0\">\n"+
                "                          <Component id=\"name_jLabel\" alignment=\"3\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                          <Component id=\"name_jTextField\" alignment=\"3\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"+
                "                      </Group>\n"+
                "                      <EmptySpace max=\"-2\" attributes=\"0\"/>\n")

    x    = 0
    boo  = False
    for menu in allMenu:
        if mLen%2 != 0:
            if mLen>1 and (mLen-x-1)%2==0 and mLen-x>1:
                out.write(  "                      <Group type=\"103\" groupAlignment=\"3\" attributes=\"0\">\n    ")
                boo = True
            if x%2 != 0 and mLen>1 :
                out.write(  "    ")
                boo = True
            out.write(  "                      <Component id=\""+menu+"\"")
            if boo:
                out.write(" alignment=\"3\"")
            out.write(  " min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")
            if mLen>1 and (mLen-x-1)%2==1 and mLen-x>1:
                out.write(  "                      </Group>\n"+
                            "                      <EmptySpace max=\"-2\" attributes=\"0\"/>\n")
        if mLen%2 == 0:
            if x%2 == 0:
                out.write(  "                      <Group type=\"103\" groupAlignment=\"3\" attributes=\"0\">\n    ")
                boo = True
            if x%2 != 0 and mLen>1 :
                out.write(  "    ")
                boo = True
            out.write(  "                      <Component id=\""+menu+"\"")
            if boo:
                out.write(" alignment=\"3\"")
            out.write(  " min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")
            if x%2 != 0:
                out.write(  "                      </Group>\n"+
                            "                      <EmptySpace max=\"-2\" attributes=\"0\"/>\n")
        x+=1
        boo = False
    out.write(  "                  <EmptySpace max=\"-2\" attributes=\"0\"/>\n"+
                "                  <Component id=\"main_jScroll\" min=\"-2\" pref=\"266\" max=\"-2\" attributes=\"0\"/>\n"+
                "                  <EmptySpace max=\"-2\" attributes=\"0\"/>\n"+
                "                </Group>\n"+
                "              </Group>\n"+
                "            </DimensionLayout>\n"+
                "          </Layout>\n"+
                "          <SubComponents>\n")
    write_command_component(out,12,"stop_jButton","Stop","button",91,[0,0,"ff"],"Stop this box",None,False)
    write_command_component(out,12,"reset_jButton","Reset","button",91,['ff',74,0],"Reset to default values",None,False)
    write_command_component(out,12,"run_jButton","RUN","button",91,['ff',74,0],"Run this box",None,False)
    write_command_component(out,12,"name_jLabel","(re)Name","label",None,None,"Name Box",None,False)
    write_command_component(out,12,"name_jTextField","Name","txt",None,None,"Rename the box here",None,False)

    for Panel in yml['Menus']:
        if Panel['isMenu']:
            h = Panel['name']
            if 'help' in Panel:
                h = Panel['help']
            write_command_component(out,12,u.name_without_space(Panel['name']),Panel['name'],"RBUTTON",None,None,h,None,True)

    out.write(  "            <Container class=\"javax.swing.JScrollPane\" name=\"main_jScroll\">\n"+
                "\n"+
                "              <Layout class=\"org.netbeans.modules.form.compat2.layouts.support.JScrollPaneSupportLayout\"/>\n"+
                "              <SubComponents>\n"+
                "                <Container class=\"javax.swing.JTabbedPane\" name=\"options_tab_panel\">\n"+
                "\n"+
                "                  <Layout class=\"org.netbeans.modules.form.compat2.layouts.support.JTabbedPaneSupportLayout\"/>\n"+
                "                  <SubComponents>\n")
    for Panel in yml['Menus']:
        sIndent = 20
        if 'Panel' in Panel:
            pLen  = len(Panel['Panel'])
            pName = Panel['name']
            pNameI = u.create_initials(pName)

            write_panel(out,sIndent,pName)

            dictBV   = {}
            tabBV    = []
            if not Panel['isTab']:
                (tabBV,dictBV,infB,infV) = u.refactor_components_notTab(pName,Panel['Panel'])
                write_layout_panel2(out,sIndent,tabBV,dictBV)
                write_subComponents2(out,sIndent,tabBV,dictBV,infB,infV)
            if Panel['isTab']:
                if pLen>1: # Means need a tabs
                    tmName = pNameI+"_"+pNameI
                    write_tab_panel(out,sIndent,pName,Panel['Panel'])
                    sIndent += 6
                for Tab in Panel['Panel']:
                    if 'Arguments' in Tab:
                        tName  = Tab['tab']
                        if pLen>1:
                            write_panel(out,sIndent,tName)
                        dictBV   = {}
                        tabBV    = []
                        (tabBV,dictBV) = u.refactor_components_Tab(pName,tName,Tab['Arguments'])
                        write_layout_panel(out,sIndent,pName,tName,Tab['Arguments'])
                        write_subComponents(out,sIndent,pName,tName,Tab['Arguments'])
                        if pLen>1 and Panel['isTab']:
                            y = st_indented(sIndent,"        </Container>\n")
                            out.write(y)

                if pLen>1 and Panel['isTab']: # Means need a tabs and needs to close it
                    s = ""
                    sIndent -= 6
                    s += st_indented(sIndent,"      </SubComponents>\n")
                    s += st_indented(sIndent,"    </Container>\n")
                    s += st_indented(sIndent,"  </SubComponents>\n")
                    out.write(s)
            v = st_indented(sIndent,"</Container>\n")
            out.write(v)

    out.write(  "                  </SubComponents>\n"+
                "                </Container>\n"+
                "              </SubComponents>\n"+
                "            </Container>\n"+
                "          </SubComponents>\n"+
                "        </Container>\n"+
                "      </SubComponents>\n"+
                "    </Container>\n")

def write_panel(out,sIndent,pName):
    pNameI  = u.create_initials(pName)
    s = ""
    s += st_indented(sIndent,"<Container class=\"javax.swing.JPanel\" name=\""+pNameI+"_jPanel\">\n")
    s += st_indented(sIndent,"  <Constraints>\n")
    s += st_indented(sIndent,"    <Constraint layoutClass=\"org.netbeans.modules.form.compat2.layouts.support.JTabbedPaneSupportLayout\" value=\"org.netbeans.modules.form.compat2.layouts.support.JTabbedPaneSupportLayout$JTabbedPaneConstraintsDescription\">\n")
    s += st_indented(sIndent,"      <JTabbedPaneConstraints tabName=\""+pName+"\">\n")
    s += st_indented(sIndent,"        <Property name=\"tabTitle\" type=\"java.lang.String\" value=\""+pName+"\"/>\n")
    s += st_indented(sIndent,"      </JTabbedPaneConstraints>\n")
    s += st_indented(sIndent,"    </Constraint>\n")
    s += st_indented(sIndent,"  </Constraints>\n")
    out.write(s)


def write_tab_panel(out,sIndent,pName,panel):
    pNameI  = u.create_initials(pName)
    tmNameI = pNameI+"_"+pNameI

    s = ""
    s += st_indented(sIndent,"  <Layout>\n")
    s += st_indented(sIndent,"    <DimensionLayout dim=\"0\">\n")
    s += st_indented(sIndent,"      <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"        <Group type=\"102\" alignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"          <Component id=\""+tmNameI+"_JTabbedPane\" min=\"-2\" pref=\"261\" max=\"-2\" attributes=\"0\"/>\n")
    s += st_indented(sIndent,"          <EmptySpace min=\"0\" pref=\"215\" max=\"32767\" attributes=\"0\"/>\n")
    s += st_indented(sIndent,"        </Group>\n")
    s += st_indented(sIndent,"      </Group>\n")
    s += st_indented(sIndent,"    </DimensionLayout>\n")
    s += st_indented(sIndent,"    <DimensionLayout dim=\"1\">\n")
    s += st_indented(sIndent,"      <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"        <Group type=\"102\" alignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"          <Component id=\""+tmNameI+"_JTabbedPane\" pref=\"70\" max=\"32767\" attributes=\"0\"/>\n")
    s += st_indented(sIndent,"          <EmptySpace min=\"0\" pref=\"70\" max=\"32767\" attributes=\"0\"/>\n")
    s += st_indented(sIndent,"        </Group>\n")
    s += st_indented(sIndent,"      </Group>\n")
    s += st_indented(sIndent,"    </DimensionLayout>\n")
    s += st_indented(sIndent,"  </Layout>\n")
    s += st_indented(sIndent,"  <SubComponents>\n")
    s += st_indented(sIndent,"    <Container class=\"javax.swing.JTabbedPane\" name=\""+tmNameI+"_JTabbedPane\">\n")
    s += st_indented(sIndent,"      <Layout class=\"org.netbeans.modules.form.compat2.layouts.support.JTabbedPaneSupportLayout\"/>\n")
    s += st_indented(sIndent,"      <SubComponents>\n")

    out.write(s)

def write_layout_panel2(out,sIndent,tabBV,dictBV):
    s = ""
    s += st_indented(sIndent,"  <Layout>\n")
    s += st_indented(sIndent,"    <DimensionLayout dim=\"0\">\n")
    s += st_indented(sIndent,"      <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"        <Group type=\"102\" attributes=\"0\">\n")

    boo = False
    s += st_indented(sIndent,"          <Group type=\"103\" alignment=\"1\" attributes=\"0\">\n")
    for bv in tabBV:
        s += st_indented(sIndent,"            <Component id=\""+bv+"\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")
        if dictBV[bv] != "":
            boo = True
    s += st_indented(sIndent,"          </Group>\n")
    if boo:
        s += st_indented(sIndent,"          <EmptySpace type=\"separate\" max=\"-2\" attributes=\"0\"/>\n")
        s += st_indented(sIndent,"          <Group type=\"103\" alignment=\"1\" attributes=\"0\">\n")
        for bv in tabBV:
            if dictBV[bv] != "":
                s += st_indented(sIndent,"            <Component id=\""+dictBV[bv]+"\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")
        s += st_indented(sIndent,"            <EmptySpace max=\"32767\" attributes=\"0\"/>\n")
        s += st_indented(sIndent,"          </Group>\n")
    s += st_indented(sIndent,"        </Group>\n")
    s += st_indented(sIndent,"      </Group>\n")
    s += st_indented(sIndent,"    </DimensionLayout>\n")
    s += st_indented(sIndent,"    <DimensionLayout dim=\"1\">\n")
    s += st_indented(sIndent,"      <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"        <Group type=\"102\" alignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"          <EmptySpace max=\"-2\" attributes=\"0\"/>\n")
    for bv in tabBV:
        if dictBV[bv] != "":
            s += st_indented(sIndent,"            <Group type=\"103\" groupAlignment=\"3\" attributes=\"0\">\n  ")
        s += st_indented(sIndent,"            <Component id=\""+bv+"\"")
        if dictBV[bv] != "":
            s += " alignment=\"3\""
        s += " min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"
        if dictBV[bv] != "":
            s += st_indented(sIndent,"              <Component id=\""+dictBV[bv]+"\" alignment=\"3\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n  ")
            s += st_indented(sIndent,"            </Group>\n")
        s += st_indented(sIndent,"        <EmptySpace max=\"-2\" attributes=\"0\"/>\n")
    s += st_indented(sIndent,"          <EmptySpace max=\"32767\" attributes=\"0\"/>\n")
    s += st_indented(sIndent,"        </Group>\n")
    s += st_indented(sIndent,"      </Group>\n")
    s += st_indented(sIndent,"    </DimensionLayout>\n")
    s += st_indented(sIndent,"  </Layout>\n")
    out.write(s)

def write_subComponents2(out,sIndent,tabBV,dictBV,infB,infV):
    s = st_indented(sIndent,"  <SubComponents>\n")
    out.write(s)

    for bv in tabBV:
        if bv.endswith("JLabel"):
            write_command_component(out,sIndent+2,bv,infB[bv],"label",None,None,"Sub Items",None,False)
        else:
            write_command_component(out,sIndent+2,bv,infB[bv][0],infB[bv][1],None,None,infB[bv][2],None,False)
            if dictBV[bv] != "":
                v = dictBV[bv]
                write_command_component(out,sIndent+2,v,infB[bv][0],infV[v][0],None,None,infB[bv][2],infV[v][1],False)
    s = st_indented(sIndent,"  </SubComponents>\n")
    out.write(s)

def write_layout_panel(out,sIndent,pName,tName,commands):
    pNameI = u.create_initials(pName)
    tNameI = u.create_initials(tName)
    s = ""
    s += st_indented(sIndent,"  <Layout>\n")
    s += st_indented(sIndent,"    <DimensionLayout dim=\"0\">\n")
    s += st_indented(sIndent,"      <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"        <Group type=\"102\" attributes=\"0\">\n")

    boo = False
    if len(commands)>0:
        s += st_indented(sIndent,"          <Group type=\"103\" alignment=\"1\" attributes=\"0\">\n")
        for co in commands:
            cName   = co['name']
            cType   = co['cType']
            c       = u.create_button_name(pName,tName,cName,cType)
            s += st_indented(sIndent,"            <Component id=\""+c+"\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")

            if 'values' in co:
                boo = True
        s += st_indented(sIndent,"          </Group>\n")
    if boo:
        s += st_indented(sIndent,"          <EmptySpace type=\"separate\" max=\"-2\" attributes=\"0\"/>\n")
        s += st_indented(sIndent,"          <Group type=\"103\" alignment=\"1\" attributes=\"0\">\n")
        for co in commands:
            if 'values' in co:
                cName   = co['name']
                cType   = co['cType']
                v       = ""
                vType   = co['values']['vType']
                v       = u.create_value_name(pName,tName,cName,vType)
                s += st_indented(sIndent,"            <Component id=\""+v+"\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n")

        s += st_indented(sIndent,"            <EmptySpace max=\"32767\" attributes=\"0\"/>\n")
        s += st_indented(sIndent,"          </Group>\n")

    s += st_indented(sIndent,"        </Group>\n")
    s += st_indented(sIndent,"      </Group>\n")
    s += st_indented(sIndent,"    </DimensionLayout>\n")
    s += st_indented(sIndent,"    <DimensionLayout dim=\"1\">\n")
    s += st_indented(sIndent,"      <Group type=\"103\" groupAlignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"        <Group type=\"102\" alignment=\"0\" attributes=\"0\">\n")
    s += st_indented(sIndent,"          <EmptySpace max=\"-2\" attributes=\"0\"/>\n")

    for co in commands:
        if 'values' in co:
            s += st_indented(sIndent,"            <Group type=\"103\" groupAlignment=\"3\" attributes=\"0\">\n  ")
        cName   = co['name']
        cType   = co['cType']
        c       = u.create_button_name(pName,tName,cName,cType)
        s += st_indented(sIndent,"            <Component id=\""+c+"\"")
        if 'values' in co:
            s += " alignment=\"3\""
        s += " min=\"-2\" max=\"-2\" attributes=\"0\"/>\n"

        if 'values' in co:
            v       = ""
            vType   = co['values']['vType']
            v       = u.create_value_name(pName,tName,cName,vType)
            #s += st_indented(sIndent,"                <EmptySpace type=\"separate\" max=\"-2\" attributes=\"0\"/>\n")
            s += st_indented(sIndent,"              <Component id=\""+v+"\" alignment=\"3\" min=\"-2\" max=\"-2\" attributes=\"0\"/>\n  ")

        if 'values' in co:
            s += st_indented(sIndent,"            </Group>\n")
        s += st_indented(sIndent,"        <EmptySpace max=\"-2\" attributes=\"0\"/>\n")

    s += st_indented(sIndent,"          <EmptySpace max=\"32767\" attributes=\"0\"/>\n")
    s += st_indented(sIndent,"        </Group>\n")
    s += st_indented(sIndent,"      </Group>\n")
    s += st_indented(sIndent,"    </DimensionLayout>\n")
    s += st_indented(sIndent,"  </Layout>\n")
    out.write(s)

def write_subComponents(out,sIndent,pName,tName,commands):
    s = st_indented(sIndent,"  <SubComponents>\n")
    out.write(s)
    for co in commands:
        cName   = co['name']
        cType   = co['cType']
        c       = u.create_button_name(pName,tName,cName,cType)
        cHelp = ""
        if 'cHelp' in co and (co['cHelp'] != None or co['cHelp'] ==""):
            cHelp = co['cHelp']

        write_command_component(out,sIndent+2,c,cName,cType,None,None,cHelp,None,False)

        if 'values' in co:
            v       = ""
            vType   = co['values']['vType']
            v       = u.create_value_name(pName,tName,cName,vType)
            write_command_component(out,sIndent+2,v,cName,vType,None,None,cHelp,co['values'],False)
    s = st_indented(sIndent,"  </SubComponents>\n")
    out.write(s)

def write_command_component(out,sIndent,name,text,bType,hSize,rgbColors,bHelp,vCom,isMenu):
    isSpin  = u.is_a_spinner(bType)
    isText  = u.is_a_text(bType)
    isLabel = u.is_a_label(bType)
    isCombo = u.is_a_combo(bType)
    val     = ""

    s = ""
    if isLabel or isText or vCom != None:
        s += st_indented(sIndent,"<Component class=\"javax.swing."+u.get_value_java_type(bType)+"\" name=\""+name+"\">\n")
    else:
        s += st_indented(sIndent,"<Component class=\"javax.swing."+u.get_box_type(bType)+"\" name=\""+name+"\">\n")
    s += st_indented(sIndent,"  <Properties>\n")
    s += st_indented(sIndent,"    <Property name=\"name\" type=\"java.lang.String\" value=\""+name+"\" noResource=\"true\"/>\n")

    if isMenu:
        s += st_indented(sIndent,"    <Property name=\"buttonGroup\" type=\"javax.swing.ButtonGroup\" editor=\"org.netbeans.modules.form.RADComponent$ButtonGroupPropertyEditor\">\n")
        s += st_indented(sIndent,"      <ComponentRef name=\"Menu_Buttons\"/>\n")
        s += st_indented(sIndent,"    </Property>\n")

    if isLabel or isText:
        s += st_indented(sIndent,"    <Property name=\"font\" type=\"java.awt.Font\" editor=\"org.netbeans.beaninfo.editors.FontEditor\">\n")
        s += st_indented(sIndent,"      <Font name=\"Ubuntu\" size=\"15\" style=\"3\"/>\n")
        s += st_indented(sIndent,"    </Property>\n")

    if text != '' and (isSpin == False and isCombo == False):
        s += st_indented(sIndent,"    <Property name=\"text\" type=\"java.lang.String\" value=\""+text+"\"/>\n")

    if (isLabel or isText) and vCom != None:
        if 'vValues' in vCom:
            val = str(vCom['vValues'])
            s += st_indented(sIndent,"    <Property name=\"text\" type=\"java.lang.String\" value=\""+val+"\"/>\n")

    if hSize != None :
        s += st_indented(sIndent,"    <Property name=\"maximumSize\" type=\"java.awt.Dimension\" editor=\"org.netbeans.beaninfo.editors.DimensionEditor\">\n")
        s += st_indented(sIndent,"      <Dimension value=\"["+str(hSize)+", 29]\"/>\n")
        s += st_indented(sIndent,"    </Property>\n")
        s += st_indented(sIndent,"    <Property name=\"minimumSize\" type=\"java.awt.Dimension\" editor=\"org.netbeans.beaninfo.editors.DimensionEditor\">\n")
        s += st_indented(sIndent,"      <Dimension value=\"["+str(hSize)+", 29]\"/>\n")
        s += st_indented(sIndent,"    </Property>\n")
        s += st_indented(sIndent,"    <Property name=\"preferredSize\" type=\"java.awt.Dimension\" editor=\"org.netbeans.beaninfo.editors.DimensionEditor\">\n")
        s += st_indented(sIndent,"      <Dimension value=\"["+str(hSize)+", 29]\"/>\n")
        s += st_indented(sIndent,"    </Property>\n")

    if rgbColors != None :
        if len(rgbColors) == 3:
            s += st_indented(sIndent,"    <Property name=\"foreground\" type=\"java.awt.Color\" editor=\"org.netbeans.beaninfo.editors.ColorEditor\">\n")
            s += st_indented(sIndent,"      <Color blue=\""+str(rgbColors[2])+"\" green=\""+str(rgbColors[1])+"\" red=\""+str(rgbColors[0])+"\" type=\"rgb\"/>\n")
            s += st_indented(sIndent,"    </Property>\n")

    if isSpin:
        vDefault    = vCom['vDefault']
        vMin        = vCom['vMin']
        vMax        = vCom['vMax']
        vJump       = vCom['vJump']
        val         = u.string_range_values_text(bType,vDefault,vMin,vMax,vJump)
        s += st_indented(sIndent,"    <Property name=\"model\" type=\"javax.swing.SpinnerModel\" editor=\"org.netbeans.modules.form.editors2.SpinnerModelEditor\">\n")
        s += st_indented(sIndent,"      <SpinnerModel "+val+" type=\"number\"/>\n")
        s += st_indented(sIndent,"    </Property>\n")

        s += st_indented(sIndent,"    <Property name=\"preferredSize\" type=\"java.awt.Dimension\" editor=\"org.netbeans.beaninfo.editors.DimensionEditor\">\n")
        s += st_indented(sIndent,"        <Dimension value=\"[115, 28]\"/>\n")
        s += st_indented(sIndent,"    </Property>\n")


    if isCombo:
        val = ', '.join(vCom['vValues'])
        s += st_indented(sIndent,"    <Property name=\"model\" type=\"javax.swing.ComboBoxModel\" editor=\"org.netbeans.modules.form.editors2.ComboBoxModelEditor\">\n")
        s += st_indented(sIndent,"      <StringArray count=\""+str(len(vCom['vValues']))+"\">\n")
        i = 0
        for l in vCom['vValues']:
            s += st_indented(sIndent,"        <StringItem index=\""+str(i)+"\" value=\""+l+"\"/>\n")
            i += 1
        s += st_indented(sIndent,"      </StringArray>\n")
        s += st_indented(sIndent,"    </Property>\n")


    s += st_indented(sIndent,"  </Properties>\n")

    if bHelp != '':
        bHelp = u.clean_help_text(bHelp)
        s += st_indented(sIndent,"  <AccessibilityProperties>\n")
        s += st_indented(sIndent,"    <Property name=\"AccessibleContext.accessibleDescription\" type=\"java.lang.String\" value=\""+bHelp+"\"/>\n")
        s += st_indented(sIndent,"  </AccessibilityProperties>\n")

    tab = u.get_java_eventHandler(bType)

    if len(tab)>0:
        s += st_indented(sIndent,"  <Events>\n")
        for t in tab:
            s += st_indented(sIndent,"    <EventHandler event=\""+t[0]+"\" listener=\"java.awt.event."+t[1]+"\" parameters=\"java.awt.event."+t[2]+"\" handler=\""+name+"_"+t[3]+"\"/>\n")
        s += st_indented(sIndent,"  </Events>\n")

    s += st_indented(sIndent,"</Component>\n")
    out.write(s)

def write_close_form(out,yml):
    out.write(  "  </SubComponents>\n"+
                "</Form>")

def st_indented(sIndent,st):
    return st.rjust(sIndent+len(st))

