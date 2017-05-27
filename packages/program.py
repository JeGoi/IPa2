#!/usr/bin/env python
"""
Title:   Program object
Author:  JG
Date:    dec 2016
"""

from util import connector_range, empty_var

class clProgram(object):
    name        = ""
    exitValue   = ""
    pathLinux   = ""
    pathMac     = ""
    pathWin     = ""
    menu        = ""
    numImput    = ""
    outputPath  = ""
    pubRef      = ""
    pgrmHelp    = ""
    Desc        = ""
    Website     = ""
    WebServices = ""
    outputFiles = ""

    def __init__(self, name, exitValue, pathLinux, pathMac, pathWin, menu, numImput, outputPath, pubRef, pgrmHelp, Desc, Website, WebServices, outputFiles):
        if empty_var('Program Name',name):
            self.name       = name
        if empty_var('Program Exit value',exitValue):
            self.exitValue  = exitValue
        if empty_var('Program Path Linux',PathLinux):
            self.PathLinux  = PathLinux
        if empty_var('Program Path Mac',PathMac):
            self.PathMac    = PathMac
        if empty_var('Program Path Win',PathWin):
            self.PathWin    = PathWin
        if empty_var('Program Menu',menu):
            self.menu       = menu
        if empty_var('Program Number of Input(s)',numImput):
            self.numImput   = numImput
        if empty_var('Program Output Path',outputPath):
            self.outputPath = outputPath
        self.pubRef         = pubRef
        self.pgrmHelp       = pgrmHelp
        self.Desc           = Desc
        self.Website        = Website
        self.WebServices    = WebServices
        self.outputFiles    = outputFiles        
     
    def __str__(self):
        s = (
            "Program:\n"+
            "name:\t{}\n".format(self.name)+
            "exitValue:\t{}\n".format(self.exitValue)+
            "PathLinux:\t{}\n".format(self.PathLinux)+
            "PathMac:\t{}\n".format(self.PathMac)+
            "PathWin:\t{}\n".format(self.PathWin)+
            "menu:\t{}\n".format(self.menu)+
            "numImput:\t{}\n".format(self.numImput)+
            "outputPath:\t{}\n".format(self.outputPath)+
            "pubRef:\t{}\n".format(self.pubRef)+
            "pgrmHelp:\t{}\n".format(self.pgrmHelp)+
            "Desc:\t{}\n".format(self.Desc)+
            "Website:\t{}\n".format(self.Website)+
            "WebServices:\t{}\n".format(self.WebServices)+
            "outputFiles:\t{}\n".format(self.outputFiles)
            )
        return s

def make_program(name, exitValue, pathLinux, pathMac, pathWin, menu, numImput, outputPath, pubRef, pgrmHelp, Desc, Website, WebServices, outputFiles):
    oProgram = clProgram(name, exitValue, pathLinux, pathMac, pathWin, menu, numImput, outputPath, pubRef, pgrmHelp, Desc, Website, WebServices, outputFiles)
    return oProgram
