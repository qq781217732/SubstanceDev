# ADOBE CONFIDENTIAL
#
# Copyright 2019 Adobe
# All Rights Reserved.
#
# NOTICE:  Adobe permits you to use, modify, and distribute this file in
# accordance with the terms of the Adobe license agreement accompanying it.
# If you have received this file from a source other than Adobe,
# then your use, modification, or distribution of it requires the prior
# written permission of Adobe.
#

import os
import importlib
import inspect
from sd.tools import io


def getAssetsDir(aPyFile=None):
    if aPyFile:
        pyFile = aPyFile
    else:
        aPyFile = __file__

    return io.getAssetsDir(aPyFile)

def loadTestAssetFile(aSBSFileName, aPyFile=None):
    """
    :rtype: string
    """
    return os.path.join(getAssetsDir(aPyFile), aSBSFileName)


def getTestOutputDir(aPyFile):
    """
    :rtype: string
    """
    return io.getUserDocumentOutputDir(aPyFile)


def loadSDPackage(aContext, aTestAssetSBSFile, aPyFile=None, updatePackages=True):
    """

    :param aContext:
    :type aContext: sd.context.Context
    :param aTestAssetSBSFile:
    :type aTestAssetSBSFile: string
    :param aPyFile:
    :type aTestAssetSBSFile: string
    :rtype: sd.api.sdpackage.SDPackage
    """
    pkgFileName = loadTestAssetFile(aTestAssetSBSFile, aPyFile)
    return aContext.getSDApplication().getPackageMgr().loadUserPackage(pkgFileName, updatePackages)


def getPyFiles(aDirAbsPath, aFilePrefix=''):
    files = []
    for child in os.listdir(aDirAbsPath):
        childAbsPath = os.path.join(aDirAbsPath, child)
        if os.path.isdir(childAbsPath):
            files += getPyFiles(childAbsPath)
        else:
            if not child.endswith('.py'):
                continue
            if child == '__init__.py':
                continue
            if aFilePrefix:
                if not child.startswith(aFilePrefix):
                    continue
            if childAbsPath == os.path.abspath(__file__):
                continue
            files.append(childAbsPath)
    return files


def getClassesFromPyModule(aPyModule):
    items = []
    for classDesc in inspect.getmembers(aPyModule, inspect.isclass):
        items.append(classDesc[1])
    return items

def getFunctionsFromPyModule(aPyModule):
    """
    Get the list of the functions located in the specified python module

    :param aPyModule: The Python Module to introspect
    :type aPyModule: Module
    :rtype: [Function]
    """
    items = []
    for functionDesc in inspect.getmembers(aPyModule, inspect.isfunction):
        items.append(functionDesc[1])
    return items

def importPyModuleFromPyFile(aPyFile):
    """
    Import the python module defined by the specified aPyFile file

    :param aPyFile: The file path of the python module
    :type aPyFile: string
    :rtype: Python Module
    """
    # Create module name
    currentDir = io.getAPIRootDir()
    moduleName = aPyFile[len(currentDir + os.path.sep):]
    if moduleName.endswith('.py'):
        moduleName = moduleName[0:len(moduleName) - len('.py')]
    moduleName = moduleName.replace(os.path.sep, '_')

    # Import module
    spec = importlib.util.spec_from_file_location(moduleName, aPyFile)
    pyModule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pyModule)
    return pyModule


def createFileLines(aStringList):
    newLines = []
    for l in aStringList:
        for splitLine in l.split('\n'):
            newLines.append(splitLine + '\n')
    return newLines

def writeLinesToFile(aFilePath, aStringList):
    with open(aFilePath, 'wt', encoding='utf-8') as f:
        f.writelines(aStringList)
        f.close()

def readLinesFromFile(aFilePath):
    lines = []
    with open(aFilePath, 'rt', encoding='utf-8') as rf:
        lines = rf.readlines()
        rf.close()
    return lines

def compareLines(aUnitTestInstance, aReferenceLines, aLines):
    referenceLinesCount = len(aReferenceLines)
    linesCount = len(aLines)

    for i in range(referenceLinesCount):
        srcLine = aReferenceLines[i]
        if i >= linesCount:
            aUnitTestInstance.assertTrue(False, 'Line count differs')
        newLine = aLines[i]
        aUnitTestInstance.assertEqual(newLine, srcLine)

    if linesCount > referenceLinesCount:
        aUnitTestInstance.assertTrue(False, 'Line count differs')

def toPlatformIndenpendantPath(aPath):
    return aPath.replace('\\', '/')

def toPlatformIndenpendantAPIRelativePath(aPath):
    piPath = toPlatformIndenpendantPath(aPath)
    gitRootDir = toPlatformIndenpendantPath(io.getAPIRootDir() + os.path.sep)
    i = piPath.find(gitRootDir)
    if i >= 0:
        str0 = piPath[0:i]
        str1 = piPath[i+len(gitRootDir):]
        return str0 + str1
    return piPath
