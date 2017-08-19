#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Title:   Useful function
Author:  JG
Date:    dec 2016
"""
import re
import sys,os
import yaml
import string
from os import listdir
from os.path import isfile, join

# Util functions
testDirectory = "./outputs/"

def print_help_exit():
    print_help()
    sys.exit(2)

def print_help():
    print   (__file__+' [options]\n'+
            '[-h,--help]\tHelp\n'+
            '[-y <input yanl file>]\tdirectory to yaml file\n'+
            '[-d <Armadillo directory>]\tdirectory to Armadillo root\n')

# Test on the connector range
def connector_range(name,val):
    if 2 <= val <= 4:
        return True
    else:
        print "Connector value nammed : '"+name+"' is not in the range [2,4]."
        raise SystemExit

# Test on empty string
def empty_var(name,v):
    s = "{}".format(v)
    if s:
        return True
    else:
        print "A '"+name+"' can not be empty."
        raise SystemExit

def print_tab_values(values):
    sf = ""
    for s in values:
        sf = sf + "{}".format(s)
    return sf

#
# Get Paths
#
def define_edit_path(a):
    if a == '':
        return testDirectory
    return a+"/src/editors/"

def define_prop_path(a):
    if a == '':
        return testDirectory
    return a+"/data/properties/"

def define_biol_path(a):
    if a != '':
        return a+"/src/biologic/"
    return a

def define_prog_path(a):
    if a == '':
        return testDirectory
    return a+"/src/programs/"

def get_armadillo_biologic_files_name():
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    s = "{}".format(onlyfiles)
    return s;

def cleanOutuptPath(yml):
    s = yml['Program']['outputPath']
    s = s.replace(os.path.sep,"\"+File.separator+\"")
    s = '"'+s+'"'
    return s

#
# Get Names and fix it
#
def set_docker_name(yml):
    o = get_program_name(yml)+"_"+yml['kword']+"_0"
    return o

def get_program_name(yml):
    o = replace_space_by_underscore(yml['Program']['name'])
    return o

def get_program_version(yml):
    o = replace_space_by_underscore(yml['Program']['version'])
    return o

def create_button_name(panel,title,name,btype):
    p = create_initials(panel)
    t = create_initials(title)
    n = get_command_name(name)
    b = "_"+btype.lower()
    o = p+"_"+t+n+b
    return o

def create_value_name(panel,title,name,vtype):
    p = create_initials(panel)
    t = create_initials(title)
    n = get_command_name(name)
    b = "_"+get_value_java_type(vtype.upper())+"Value"
    o = p+"_"+t+n+b
    return o

def get_command_name(s):
    b = hyphen_start_of_argument(s)
    o = change_symboles_by_names(s)
    return b+o

def get_argument_text(s):
    p = re.compile('-+\s*(.*)')
    m = p.match(s)
    if m:
        return (m.group(1))
    else:
        return "WRONG"

def create_initials(s):
    o = s.title()
    o = o.translate(None,string.ascii_lowercase)
    o = o.replace("_","")
    o = o.replace(" ","")
    return o

def name_without_space(s):
    return replace_space_by_underscore(s)

def replace_space_by_underscore(s):
    o = s.replace(" ","_")
    return o

def change_symboles_by_names(s):
    o = get_argument_text(s)
    o = o.replace("=","EQUALSYMBOL")
    o = o.replace("_","UNDERSCORESYMBOL")
    o = o.replace("-","HYPHENSYMBOL")
    o = o.replace("+","PLUS")
    o = o.replace(".","DOT")
    return o

def remove_hyphen(s):
    o = s.replace("-","")
    return o

def hyphen_start_of_argument(s):
    if s.startswith("--"):
        return "__"
    return "_"

def get_value_text_type(s):
    o = s.upper()
    d = {
        "BYT"       : "Byte",
        "INT"       : "Integer",
        "LON"       : "Long",
        "SHO"       : "Short",
        "FLO"       : "Float",
        "DOU"       : "Double",
        "BOO"       : "Integer",
        "COMBO"     : "ComboBox",
        "TEXT"      : "Text",
        "TXT"       : "Text",
        "DIRFILE"   : "Text",
        "DIRFILES"  : "Text",
        "DIRREP"    : "Text",
        "LABEL"     : "Label",
        "DIR"       : "Text"
        }
    if o in d:
        return d[o]
    else:
        return "NotAGoodValue1"

def is_a_spinner(s):
    o = s.upper()
    d = {
        "BYT"       : True,
        "INT"       : True,
        "LON"       : True,
        "SHO"       : True,
        "FLO"       : True,
        "DOU"       : True,
        "BOO"       : True
        }
    if o in d:
        return d[o]
    else:
        return False

def is_a_text(s):
    o = s.upper()
    d = {
        "TEXT"      : True,
        "TXT"       : True,
        "DIRFILE"   : True,
        "DIRFILES"  : True,
        "DIRREP"    : True,
        "DIR"       : False
        }
    if o in d:
        return d[o]
    else:
        return False

def is_a_combo(s):
    o = s.upper()
    d = {
        "COMBO"      : True
        }
    if o in d:
        return d[o]
    else:
        return False

def is_a_label(s):
    o = s.upper()
    d = {
        "LAB"       : True,
        "LABEL"     : True,
        "JLABEL"    : True
        }
    if o in d:
        return d[o]
    else:
        return False

def get_value_java_type(s):
    o = s.upper()
    d = {
        "BOO"       : "JSpinner",
        "BYT"       : "JSpinner",
        "INT"       : "JSpinner",
        "INTEGER"   : "JSpinner",
        "FLO"       : "JSpinner",
        "LON"       : "JSpinner",
        "SHO"       : "JSpinner",
        "DOU"       : "JSpinner",
        "TEXT"      : "JTextField",
        "COMBO"     : "JComboBox",
        "TXT"       : "JTextField",
        "DIRFILE"   : "JTextField",
        "DIRFILES"  : "JTextField",
        "DIRREP"    : "JTextField",
        "LABEL"     : "JLabel",
        "DIR"       : "JTextField"
        }
    if o in d:
        return d[o]
    else:
        return "NotAGoodValue2"

def return_range_value(vType,vDefault,vMin,vMax,vJump,isText):
    vType = vType.upper()
    if vType == 'BYT':
        return vType_is_byt(vType,vDefault,vMin,vMax,vJump,isText)
    elif vType == 'INT':
        return vType_is_int(vType,vDefault,vMin,vMax,vJump,isText)
    elif vType == 'LON':
        return vType_is_lon(vType,vDefault,vMin,vMax,vJump,isText)
    elif vType == 'SHO':
        return vType_is_sho(vType,vDefault,vMin,vMax,vJump,isText)
    elif vType == 'FLO':
        return vType_is_flo(vType,vDefault,vMin,vMax,vJump,isText)
    elif vType == 'DOU':
        return vType_is_dou(vType,vDefault,vMin,vMax,vJump,isText)
    elif vType == 'BOO':
        return vType_is_boo(vType,vDefault,vMin,vMax,vJump,isText)
    else:
        return (vDefault,vMin,vMax,vJump)

def string_range_values_text(vType,vDefault,vMin,vMax,vJump):
    s = "initial=\""+str(vDefault)+"\""
    if vMax != None:
        s = s+" maximum=\""+str(vMax)+"\""
    if vMin != None:
        s = s+" minimum=\""+str(vMin)+"\""
    s = s+" numberType=\"java.lang."+get_value_text_type(vType)+"\""
    s = s+" stepSize=\""+str(vJump)+"\""
    return s

def vType_is_byt(vType,vDefault,vMin,vMax,vJump,isText):
    if vDefault ==  '' or vDefault == None:
        vDefault = '0'
    if vMin ==  '' or vMin == None:
        vMin = 'null'
    if vMax ==  '' or vMax == None:
        vMax = 'null'
    if vJump ==  '' or vJump == None:
        vJump = '1'
    if isText:
        return string_range_values(vType,vDefault,vMin,vMax,vJump)
    else:
        vDefault= return_java_byte(vDefault)
        vMin    = return_java_byte(vMin)
        vMax    = return_java_byte(vMax)
        vJump   = return_java_byte(vJump)
        return vDefault+','+vMin+','+vMax+','+vJump

def return_java_byte(v):
    if v != 'null':
        return '(byte)'+str(v)
    else:
        return v

def vType_is_int(vType,vDefault,vMin,vMax,vJump,isText):
    # Have remove 2 extrems values
    if vDefault ==  '' or vDefault == None:
        vDefault = '0'
    if vMin ==  '' or vMin == None:
        vMin = 'null'
    if vMax ==  '' or vMax == None:
        vMax = 'null'
    if vJump ==  '' or vJump == None:
        vJump = '1'
    if isText:
        return string_range_values(vType,vDefault,vMin,vMax,vJump)
    else:
        return str(vDefault)+','+str(vMin)+','+str(vMax)+','+str(vJump)

def vType_is_lon(vType,vDefault,vMin,vMax,vJump,isText):
    # Have remove 2 extrems values
    if vDefault ==  '' or vDefault == None:
        vDefault = '0'
    if vMin ==  '' or vMin == None:
        vMin = 'null'
    if vMax ==  '' or vMax == None:
        vMax = 'null'
    if vJump ==  '' or vJump == None:
        vJump = '1'
    if isText:
        return string_range_values(vType,vDefault,vMin,vMax,vJump)
    else:
        vDefault= return_java_long(vDefault)
        vMin    = return_java_long(vMin)
        vMax    = return_java_long(vMax)
        vJump   = return_java_long(vJump)
        return vDefault+','+vMin+','+vMax+','+vJump

def return_java_long(v):
    if v != 'null':
        return str(v)+'L'
    else:
        return v

def vType_is_flo(vType,vDefault,vMin,vMax,vJump,isText):
    # Choose an arbitrary range
    if vDefault ==  '' or vDefault == None:
        vDefault = '0.0'
    if vMin ==  '' or vMin == None:
        vMin = 'null'
    if vMax ==  '' or vMax == None:
        vMax = 'null'
    if vJump ==  '' or vJump == None:
        vJump = '1.0'
    vDefault= return_val_with_dot(vDefault)
    vMax    = return_val_with_dot(vMax)
    vMin    = return_val_with_dot(vMin)
    vJump   = return_val_with_dot(vJump)
    if isText:
        return string_range_values(vType,vDefault,vMin,vMax,vJump)
    else:
        vDefault= return_java_float(vDefault)
        vMin    = return_java_float(vMin)
        vMax    = return_java_float(vMax)
        vJump   = return_java_float(vJump)
        return vDefault+','+vMin+','+vMax+','+vJump

def return_java_float(v):
    if v != 'null':
        return v+'f'
    else:
        return v

def vType_is_dou(vType,vDefault,vMin,vMax,vJump,isText):
    # Have remove 2 extrems values
    if vDefault ==  '' or vDefault == None:
        vDefault = '1.0'
    if vMin ==  '' or vMin == None:
        vMin = 'null'
    if vMax ==  '' or vMax == None:
        vMax = 'null'
    if vJump ==  '' or vJump == None:
        vJump = '1.0'
    vDefault= return_val_with_dot(vDefault)
    vMax    = return_val_with_dot(vMax)
    vMin    = return_val_with_dot(vMin)
    vJump   = return_val_with_dot(vJump)
    if isText:
        return string_range_values(vType,vDefault,vMin,vMax,vJump)
    else:
        vDefault= return_java_double(vDefault)
        vMin    = return_java_double(vMin)
        vMax    = return_java_double(vMax)
        vJump   = return_java_double(vJump)
        return vDefault+','+vMin+','+vMax+','+vJump

def return_java_double(v):
    if v != 'null':
        v = return_val_with_dot(v)
        return v+'d'
    else:
        return v

def vType_is_sho(vType,vDefault,vMin,vMax,vJump,isText):
    # Have remove 2 extrems values
    if vDefault ==  '' or vDefault == None:
        vDefault = '0'
    if vMin ==  '' or vMin == None:
        vMin = 'null'
    if vMax ==  '' or vMax == None:
        vMax = 'null'
    if vJump ==  '' or vJump == None:
        vJump = '1'
    if isText:
        return string_range_values(vType,vDefault,vMin,vMax,vJump)
    else:
        # add (short) in front if not null
        vDefault= return_java_short(vDefault)
        vMin    = return_java_short(vMin)
        vMax    = return_java_short(vMax)
        vJump   = return_java_short(vJump)
        return vDefault+','+vMin+','+vMax+','+vJump

def return_java_short(v):
    if v != 'null':
        return '(short)'+str(v)
    else:
        return v

def vType_is_boo(vType,vDefault,vMin,vMax,vJump,isText):
    # Have remove 2 extrems values
    if vDefault ==  '' or vDefault == None:
        vDefault = '0'
    if vMin ==  '' or vMin == None:
        vMin = '0'
    if vMax ==  '' or vMax == None:
        vMax = '1'
    if vJump ==  '' or vJump == None:
        vJump = '1'
    if isText:
        return string_range_values(vType,vDefault,vMin,vMax,vJump)
    else:
        return str(vDefault)+','+str(vMin)+','+str(vMax)+','+str(vJump)

def return_val_with_dot(v):
    v = str(v)
    if v != 'null':
        v = v.replace(',','.')
        x = v.rfind('.')
        if x == -1:
            v = v+'.0'
        return v
    else:
        return v

def get_box_size(bType):
    s = get_value_java_type(bType)
    if s == "JSpinner" or s == "JComboBox":
        return 115
    if s == "JTextField":
        return 220
    else :
        return None

def refactor_components_notTab2(pName,Panel):
    pNameI  = create_initials(pName)
    dictBV   = {}
    tabBV    = []
    for Tab in Panel:
        tName = Tab['tab']
        tNameI = create_initials(tName)
        tNameL = pNameI+"_"+tNameI+"_JLabel"
        dictBV[tNameL] = ""
        tabBV.append(tNameL)
        if 'Arguments' in Tab:
            for Arguments in Tab['Arguments']:
                cName   = Arguments['name']
                cType   = Arguments['cType']
                c       = create_button_name(pName,tName,cName,cType)
                v       = ""
                if 'values' in Arguments and Arguments['values'] is not None:
                    cName   = Arguments['name']
                    vCom    = Arguments['values']
                    vType   = vCom['vType']
                    v       = create_value_name(pName,tName,cName,vType)
                dictBV[c] = v
                tabBV.append(c)
    return (tabBV,dictBV)

def refactor_components_notTab(pName,Panel):
    pNameI  = create_initials(pName)
    dictBV  = {}
    tabBV   = []
    infB    = {}
    infV    = {}
    for Tab in Panel:
        tName = Tab['tab']
        tNameI = create_initials(tName)
        tNameL = pNameI+"_"+tNameI+"_JLabel"
        dictBV[tNameL] = ""
        tabBV.append(tNameL)
        infB[tNameL] = tName
        if 'Arguments' in Tab:
            for Arguments in Tab['Arguments']:
                cName   = Arguments['name']
                cType   = Arguments['cType']
                cHelp = ""
                if 'cHelp' in Arguments and (Arguments['cHelp'] != None or Arguments['cHelp'] ==""):
                    cHelp = Arguments['cHelp']
                c       = create_button_name(pName,tName,cName,cType)
                v       = ""
                if 'values' in Arguments and \
                    Arguments['values'] is not None and \
                    Arguments['values']['vType'] is not None:
                    cName   = Arguments['name']
                    vCom    = Arguments['values']
                    vType   = vCom['vType']
                    v       = create_value_name(pName,tName,cName,vType)
                    infV[v] = [vType,Arguments['values']]
                dictBV[c] = v
                tabBV.append(c)
                infB[c] = [cName,cType,cHelp]
    return (tabBV,dictBV,infB,infV)

def refactor_components_Tab(pName,tName,Tab):
    dictBV   = {}
    tabBV    = []
    for Arguments in Tab:
        cName   = Arguments['name']
        cType   = Arguments['cType']
        c       = create_button_name(pName,tName,cName,cType)
        v       = ""
        if 'values' in Arguments and Arguments['values'] is not None:
            cName   = Arguments['name']
            vCom    = Arguments['values']
            vType   = vCom['vType']
            v       = create_value_name(pName,tName,cName,vType)
        dictBV[c] = v
        tabBV.append(c)
    return (tabBV,dictBV)


#
# Clean Help Text
#
def clean_help_text(s):
    o = ""
    d = {
        "á" : "&aacute;","Á" : "&Aacute;","â" : "&acirc;","Â" : "&Acirc;","à" : "&agrave;","À" : "&Agrave;","å" : "&aring;","Å" : "&Aring;","ã" : "&atilde;","Ã" : "&Atilde;","ä" : "&auml;","Ä" : "&Auml;",
        "æ" : "&aelig;","Æ" : "&AElig;","ç" : "&ccedil;","Ç" : "&Ccedil;","é" : "&eacute;","É" : "&Eacute;","ê" : "&ecirc;","Ê" : "&Ecirc;","è" : "&egrave;","È" : "&Egrave;","ë" : "&euml;","Ë" : "&Euml;",
        "í" : "&iacute;","Í" : "&Iacute;","î" : "&icirc;","Î" : "&Icirc;","ì" : "&igrave;","Ì" : "&Igrave;","ï" : "&iuml;","Ï" : "&Iuml;","ñ" : "&ntilde;","Ñ" : "&Ntilde;","ó" : "&oacute;","Ó" : "&Oacute;",
        "ô" : "&ocirc;","Ô" : "&Ocirc;","ò" : "&ograve;","Ò" : "&Ograve;","ø" : "&oslash;","Ø" : "&Oslash;","õ" : "&otilde;","Õ" : "&Otilde;","ö" : "&ouml;","Ö" : "&Ouml;","œ" : "&oelig;","Œ" : "&OElig;",
        "š" : "&scaron;","Š" : "&Scaron;","ß" : "&szlig;","ð" : "&eth;","Ð" : "&ETH;","þ" : "&thorn;","Þ" : "&THORN;","ú" : "&uacute;","Ú" : "&Uacute;","û" : "&ucirc;","Û" : "&Ucirc;","ù" : "&ugrave;",
        "Ù" : "&Ugrave;","ü" : "&uuml;","Ü" : "&Uuml;","ý" : "&yacute;","Ý" : "&Yacute;","ÿ" : "&yuml;","ÿ" : "&Yuml;","-" : "&shy;","«" : "&laquo;","»" : "&raquo;","‹" : "&lsaquo;","›" : "&rsaquo;",
        "“" : "&ldquo;","”" : "&rdquo;","„" : "&bdquo;","’" : "&rsquo;","‚" : "&sbquo;","…" : "&hellip;","!" : "!","¡" : "&iexcl;","?" : "?","¿" : "&iquest;","(" : "(",")" : ")","[" : "[","]" : "]","{" : "{",
        "" : "","¨" : "&uml;","´" : "&acute;","`" : "`","^" : "^","ˆ" : "&circ;","~" : "~","˜" : "&tilde;","¸" : "&cedil;","#" : "#","*" : "*","," : ",","." : ".",":" : ":",";" : ";","·" : "&middot;",
        "•" : "&bull;","¯" : "&macr;","‾" : "&oline;","-" : "-","–" : "&ndash;","—" : "&mdash;","_" : "_","|" : "|","¦" : "&brvbar;","†" : "&dagger;","†" : "&Dagger;",
        "§" : "&sect;","¶" : "&para;","©" : "&copy;","®" : "&reg;","™" : "&trade;","&" : "&amp;","@" : "@","/" : "/","\\" : "\\","◊" : "&loz;","♠" : "&spades;","♣" : "&clubs;","♥" : "&hearts;","♦" : "&diams;","←" : "&larr;",
        "↑" : "&uarr;","→" : "&rarr;","↓" : "&darr;","↔" : "&harr;","¤" : "&curren;","€" : "&euro;","\$" : "\$","¢" : "&cent;","£" : "&pound;","¥" : "&yen;","ƒ" : "&fnof;","°" : "&deg;",
        "µ" : "&micro;","<" : "&lt;",">" : "&gt;","≤" : "&le;","≥" : "&ge;","Err :520" : "Err :520","≈" : "&asymp;","≠" : "&ne;","≡" : "&equiv;","±" : "&plusmn;","−" : "&minus;","+" : "+","×" : "&times;","÷" : "&divide;",
        "⁄" : "&frasl;","%" : "%","‰" : "&permil;","¼" : "&frac14;","½" : "&frac12;","¾" : "&frac34;","¹" : "&sup1;","²" : "&sup2;","³" : "&sup3;","º" : "&ordm;","ª" : "&ordf;","ƒ" : "&fnof;","′" : "&prime;","′" : "&Prime;",
        "∂" : "&part;","∏" : "&prod;","∑" : "&sum;","√" : "&radic;","∞" : "&infin;","¬" : "&not;","∩" : "&cap;","∫" : "&int;","→" : "&rArr;","↔" : "&hArr;","∀" : "&forall;","∃" : "&exist;","∇" : "&nabla;","∈" : "&isin;",
        "∋" : "&ni;","∝" : "&prop;","∠" : "&ang;","⊥" : "&and;","⊦" : "&or;","∪" : "&cup;","∴" : "&there4;","∼" : "&sim;","⊂" : "&sub;","⊃" : "&sup;","⊆" : "&sube;","⊇" : "&supe;",
        "⊥" : "&perp;","α" : "&alpha;","Α" : "&Alpha;","β" : "&beta;","Β" : "&Beta;","γ" : "&gamma;","Γ" : "&Gamma;","δ" : "&delta;","Δ" : "&Delta;","ε" : "&epsilon;","Ε" : "&Epsilon;","ζ" : "&zeta;",
        "Ζ" : "&Zeta;","η" : "&eta;","Η" : "&Eta;","θ" : "&theta;","Θ" : "&Theta;","ι" : "&iota;","Ι" : "&Iota;","κ" : "&kappa;","Κ" : "&Kappa;","λ" : "&lambda;","Λ" : "&Lambda;","μ" : "&mu;","Μ" : "&Mu;","ν" : "&nu;",
        "Ν" : "&Nu;","ξ" : "&xi;","Ξ" : "&Xi;","ο" : "&omicron;","Ο" : "&Omicron;","π" : "&pi;","Π" : "&Pi;","ρ" : "&rho;","Ρ" : "&Rho;","σ" : "&sigma;","ς" : "&sigmaf;","Σ" : "&Sigma;","τ" : "&tau;","Τ" : "&Tau;",
        "υ" : "&upsilon;","Υ" : "&Upsilon;","φ" : "&phi;","Φ" : "&Phi;","χ" : "&chi;","Χ" : "&Chi;","ψ" : "&psi;","Ψ" : "&Psi;","ω" : "&omega;","Ω" : "&Omega;","\"":"&quot","‘":"&lsquo"
        }
    for c in s:
        if c in d:
            o += d[c]
        else:
            o += c
    return o





#
# Get color
#
def get_color(yml):
    t_colors = ("BLUE","GREEN","ORANGE","CYAN","RED","PURPLE")
    d_colors = {
        "Alignments":"BLUE",
        "Tree":"GREEN",
        "NGS":"ORANGE",
        "System":"RED"
    }
    if not yml['Program']['menu']:
        return "PURPLE"
    else:
        for ctype in d_colors:
            if ctype in yml['Program']['menu']:
                return d_colors[ctype]
    return "CYAN"

def get_box_type(s):
    o = s.upper()
    # Link type options. Default JButton
    d = {
        "RBUTTON"   : "JRadioButton",
        "RBUT"      : "JRadioButton",
        "BUTTON"    : "JButton",
        "BUT"       : "JButton",
        "JBUTTON"   : "JButton",
        "BOX"       : "JCheckBox",
        "JLABEL"    : "JLabel"
    }
    if o in d:
        return d[o]
    else:
        return "NotAGoodValue3"

def is_a_button(s):
    o = s.upper()
    d = {
        "RBUTTON"   : True,
        "RBUT"      : True,
        "BUTTON"    : True,
        "BUT"       : True,
        "JBUTTON"   : True
        }
    if o in d:
        return d[o]
    else:
        return False

def is_a_box(s):
    o = s.upper()
    d = {
        "BOX"       : True
        }
    if o in d:
        return d[o]
    else:
        return False

def get_tab_per_panel(out, yml):
    tabPerPanel = []
    for Panel in yml['Menus']:
        if 'Panel' in Panel:
            for Tab in Panel['Panel']:
                if 'Arguments' in Tab:
                    tName   = Tab['tab']
                    tNameS  = replace_space_by_underscore(tName)
                    tabPerPanel.append(tNameS)
    return tabPerPanel

def get_java_eventHandler(s):
    o = s.upper()
    # Link type options. Default JButton
    d = {
        "RBUTTON"   : ["action"],
        "RBUT"      : ["action"],
        "BUTTON"    : ["action"],
        "BUT"       : ["action"],
        "JBUTTON"   : ["action"],
        "JRADIOBUTTON"   : ["action"],
        "BOX"       : ["action"],
        "JLABEL"    : [""],
        "BOO"       : ["state"],
        "BYT"       : ["state"],
        "INT"       : ["state"],
        "INTEGER"   : ["state"],
        "FLO"       : ["state"],
        "LON"       : ["state"],
        "SHO"       : ["state"],
        "DOU"       : ["state"],
        "TEXT"      : ["action","focus"],
        "COMBO"     : ["action"],
        "TXT"       : ["action","focus"],
        "DIRFILE"   : ["action","focus"],
        "DIRFILES"  : ["action","focus"],
        "DIRREP"    : ["action","focus"],
        "LABEL"     : [""],
        "DIR"       : ["action","focus"]
    }
    if o in d:
        tab = []
        for t in d[o]:
            if t != '':
                tab.append(get_java_eventHandler_correspondances(t))
        return tab
    else:
        print s + "We have a problem"
        return "We have a problem"


def get_java_eventHandler_simple(s):
    o = s.upper()
    # Link type options. Default JButton
    d = {
        "RBUTTON"   : "action",
        "RBUT"      : "action",
        "BUTTON"    : "action",
        "BUT"       : "action",
        "JBUTTON"   : "action",
        "JRADIOBUTTON"   : "action",
        "BOX"       : "action",
        "JLABEL"    : "",
        "BOO"       : "state",
        "BYT"       : "state",
        "INT"       : "state",
        "INTEGER"   : "state",
        "FLO"       : "state",
        "LON"       : "state",
        "SHO"       : "state",
        "DOU"       : "state",
        "TEXT"      : "focus",
        "COMBO"     : "action",
        "TXT"       : "focus",
        "DIRFILE"   : "focus",
        "DIRFILES"  : "focus",
        "DIRREP"    : "focus",
        "LABEL"     : "",
        "DIR"       : "focus"
    }
    if o in d:

        return get_java_eventHandler_correspondances(d[o])
    else:
        print s + "We have a problem"
        return "We have a problem"


def get_java_eventHandler_correspondances(s):
    o = s.lower()
    d = {
        "component" :["componentShown","ComponentListener","ComponentEvent","ComponentShown","java.awt.event."],
        "action"    :["actionPerformed","ActionListener","ActionEvent","ActionPerformed","java.awt.event."],
        "focus"     :["focusLost","FocusListener","FocusEvent","FocusLost","java.awt.event."],
        "state"     :["stateChanged","ChangeListener","ChangeEvent","StateChanged","javax.swing.event."]
        }
    if o in d:
        return d[o]
    else:
        return ""

#
# Update Yml file with java name
#
def create_commands_name(yml):
    commands_name = {}
    for Panel in yml['Menus']:
        pName   =  Panel['name']
        if 'Panel' in Panel:
            for Tab in Panel['Panel']:
                tName   =  Tab['tab']
                if 'Arguments' in Tab:
                    for Arguments in Tab['Arguments']:
                        cName = Arguments['name']
                        cType = Arguments['cType']
                        c     = create_button_name(pName,tName,cName,cType)

                        v       = ""
                        if 'values' in Arguments and \
                            Arguments['values'] is not None and \
                            Arguments['values']['vType'] is not None:
                            vType   = Arguments['values']['vType']
                            v       = create_value_name(pName,tName,cName,vType)

                        commands_name[remove_hyphen(cName)] = [c,v]
    return commands_name

def update_command_opposites_names(yml):
    c_names   = create_commands_name(yml)
    opposites = []
    for Panel in yml['Menus']:
        if 'Panel' in Panel:
            for Tab in Panel['Panel']:
                if 'Arguments' in Tab:
                    for Arguments in Tab['Arguments']:
                        if 'oppositeTo' in Arguments:
                            opposites = Arguments['oppositeTo']
                            if opposites != None :
                                oppoTemp = []
                                for o in opposites:
                                    if o in c_names:
                                        oppoTemp.append(c_names[o])
                                if len(oppoTemp) > 0:
                                    Arguments['oppositeTo'] = oppoTemp

                        if 'parentOf' in Arguments:
                            childrens = Arguments['parentOf']
                            if childrens != None :
                                cTemp = []
                                for o in childrens:
                                    if o in c_names:
                                        cTemp.append(c_names[o])
                                if len(cTemp) > 0:
                                    Arguments['parentOf'] = cTemp

def isBiologicType(v):
    v = v.lower()
    tabBiologic = [
        'Alignment',
        'Ancestor',
        'ArffFile',
        'BamFile',
        'BananaFile',
        'BedFile',
        'Biologic',
        'Blast',
        'BlastDB',
        'BlastHit',
        'CatFile',
        'ChipsFile',
        'CramFile',
        'CsvFile',
        'DatFile',
        'DataSet',
        'DiffseqFile',
        'EinvertedFile',
        'EmblFile',
        'Est2genomeFile',
        'FaidxFile',
        'FastaFile',
        'FastqFile',
        'FileFile',
        'GcgFile',
        'Genome',
        'GenomeFile',
        'HTML',
        'ImageFile',
        'InfoAlignment',
        'InfoMultipleSequences',
        'InfoSequence',
        'Input',
        'ListSequence',
        'Matrix',
        'MiRNA_MatchesFile',
        'MiRcheckFoldedmirsFile',
        'Model',
        'MultipleAlignments',
        'MultipleSequences',
        'MultipleTrees',
        'NbrfFile',
        'Outgroup',
        'Output',
        'OutputText',
        'PdbFile',
        'Phylip',
        'Phylip_Distance',
        'Phylip_Seqboot',
        'PirFile',
        'PositionToSequence',
        'ProteinAlignment',
        'RNAFoldFile',
        'Results',
        'RootedTree',
        'RunWorkflow',
        'SOLIDFile',
        'SamFile',
        'Sample',
        'Sequence',
        'SwissprotFile',
        'Text',
        'TextFile',
        'Tree',
        'Unknown',
        'UnrootedTree',
        'VCFFile',
        'WekaModelFile',
        'Workflows',
        'alertFile',
        'alignFile',
        'maskedFile',
        'tblFile'
    ]

    for b in tabBiologic:
        if b.lower() == v:
            return True
    else:
        return False


def wait():
    raw_input("Press Enter to continue...")
