# ADOBE CONFIDENTIAL
#
# Copyright 2020 Adobe
# All Rights Reserved.
#
# NOTICE:  Adobe permits you to use, modify, and distribute this file in
# accordance with the terms of the Adobe license agreement accompanying it.
# If you have received this file from a source other than Adobe,
# then your use, modification, or distribution of it requires the prior
# written permission of Adobe.
#
# Autogenerated by ipa. Don't edit directly, edit the definitions and regenerate it when changing
#

import ctypes
import base64
from enum import Enum
from .sdpackagemgr import SDPackageMgr
from .sdmodulemgr import SDModuleMgr
from .sdgraphdefinitionmgr import SDGraphDefinitionMgr
from .sduimgr import SDUIMgr
from .sdpluginmgr import SDPluginMgr
from .sdcolormanagementengine import SDColorManagementEngine
from .sdapiobject import SDAPIObject
from .sdapiobject import SDApiError
from .apiexception import APIException

class SDApplicationPath(Enum):
    """
    Enum representing predefined paths
    """
    """The directory where the application is installed"""
    InstallationDir = 0
    """The directory where the default library is installed"""
    DefaultResourcesDir = 1

class SDApplication(SDAPIObject):
    """
    Root object of all objects managed by the API
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDApplication
        """
        SDAPIObject.__init__(self, APIContext, handle, *args, **kwargs)
        # Manually written code patched in by IPA begins
        self.mContext = APIContext
        # Create new SD application
        handle = ctypes.c_void_p()
        res = self.mContext.getCTypesFct('CApi_getSDApplication')(ctypes.byref(handle))
        if res != 0:
            raise Exception('Fail to initialize SD Application')
        self.mHandle = handle

        # App callbacks
        dllHandle = self.mContext.mDllHandle
        self.__registerBeforeFileLoadedCallback = dllHandle.registerBeforeFileLoadedAppCallback
        self.__registerAfterFileLoadedCallback = dllHandle.registerAfterFileLoadedAppCallback
        self.__registerBeforeFileSavedCallback = dllHandle.registerBeforeFileSavedAppCallback
        self.__registerAfterFileSavedCallback = dllHandle.registerAfterFileSavedAppCallback
        self.__unregisterCallback = dllHandle.unregisterAppCallback

        from .sdcallbackmap import SDCallbackMap
        self.__callbackMap = SDCallbackMap
        # Manually written code patched in by IPA ends

    def registerPythonClass(self, pyFileName, pyModuleName, pyClassName):
        """
        Register the specified Python Class to the runtime

        :param pyFileName: The file name of the Python module
        :type pyFileName: string
        :param pyModuleName: The name of the Python module that contains the Python Class to register
        :type pyModuleName: string
        :param pyClassName: The name of the Python Class to register
        :type pyClassName: string
        :rtype: None
        """
        _res = self.mAPIContext.SDApplication_registerPythonClass(self.mHandle, ctypes.create_string_buffer(pyFileName.encode('utf-8')), ctypes.create_string_buffer(pyModuleName.encode('utf-8')), ctypes.create_string_buffer(pyClassName.encode('utf-8')))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return None

    def unregisterAllPythonClasses(self, pyFileName, pyModuleName):
        """
        Unregister all the Python Classes defined in the specified module

        :param pyFileName: The file name of the Python module
        :type pyFileName: string
        :param pyModuleName: The name of the Python module that contains all the Python Classes to unregister
        :type pyModuleName: string
        :rtype: None
        """
        _res = self.mAPIContext.SDApplication_unregisterAllPythonClasses(self.mHandle, ctypes.create_string_buffer(pyFileName.encode('utf-8')), ctypes.create_string_buffer(pyModuleName.encode('utf-8')))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return None

    def getPackageMgr(self):
        """
        Get the Package Manager

        :rtype: SDPackageMgr
        """
        outPackageManager = ctypes.c_void_p()
        _res = self.mAPIContext.SDApplication_getPackageMgr(self.mHandle, ctypes.byref(outPackageManager))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outPackageManager, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outPackageManager.value, ownHandle=True)

    def getModuleMgr(self):
        """
        Get the Module Manager

        :rtype: SDModuleMgr
        """
        outSDModuleMgr = ctypes.c_void_p()
        _res = self.mAPIContext.SDApplication_getModuleMgr(self.mHandle, ctypes.byref(outSDModuleMgr))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outSDModuleMgr, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outSDModuleMgr.value, ownHandle=True)

    def getSDGraphDefinitionMgr(self):
        """
        Get the Graph Definition Mgr

        :rtype: SDGraphDefinitionMgr
        """
        outSDGraphDefinitionMgr = ctypes.c_void_p()
        _res = self.mAPIContext.SDApplication_getSDGraphDefinitionMgr(self.mHandle, ctypes.byref(outSDGraphDefinitionMgr))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outSDGraphDefinitionMgr, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outSDGraphDefinitionMgr.value, ownHandle=True)

    def getPath(self, sdApplicationPath):
        """
        Get the path specified by the SDApplicationPath enum

        :param sdApplicationPath: The enum representing the path to get
        :type sdApplicationPath: SDApplicationPath
        :rtype: string
        """
        outPath = ctypes.c_char_p()
        _res = self.mAPIContext.SDApplication_getPath(self.mHandle, sdApplicationPath.value, ctypes.byref(outPath))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outPath.value.decode('utf-8')

    def getUIMgr(self):
        """
        Get the UI Manager

        :rtype: SDUIMgr
        """
        outUIManager = ctypes.c_void_p()
        _res = self.mAPIContext.SDApplication_getUIMgr(self.mHandle, ctypes.byref(outUIManager))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outUIManager, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outUIManager.value, ownHandle=True)

    def getPluginMgr(self):
        """
        Get the Plugin Manager

        :rtype: SDPluginMgr
        """
        outPluginManager = ctypes.c_void_p()
        _res = self.mAPIContext.SDApplication_getPluginMgr(self.mHandle, ctypes.byref(outPluginManager))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outPluginManager, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outPluginManager.value, ownHandle=True)

    def getColorManagementEngine(self):
        """
        Get the Color Management Engine

        :rtype: SDColorManagementEngine
        """
        outColorManagementEngine = ctypes.c_void_p()
        _res = self.mAPIContext.SDApplication_getColorManagementEngine(self.mHandle, ctypes.byref(outColorManagementEngine))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outColorManagementEngine, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outColorManagementEngine.value, ownHandle=True)
    # Manually written code patched in by IPA begins
    def getQtForPythonUIMgr(self):
       """ return ..."""
       uiMgr = self.getUIMgr()

       if uiMgr:
           from .qtforpythonuimgrwrapper import QtForPythonUIMgrWrapper
           return QtForPythonUIMgrWrapper(uiMgr)

       return None

    def _unregisterAllClasses(self, aModule):
        # print('Unregistering all classes: ' + str(aModule.__name__))
        # print('   from: \'' + str(aModule.__file__) + '\'')

        try:
            self.unregisterAllPythonClasses(aModule.__file__, aModule.__name__)
            return True
        except APIException:
            print('Fail to unregister all classes in module: \'' + str(aModule.__name__) + '\'')
            print('   from: \'' + str(aModule.__file__) + '\'')
            import traceback
            traceback.print_exc()
        return False

    def _registerClass(self, aModule, aClass):
        # print('Registering class: ' + str(aModule.__name__) + '.' + str(aClass.__name__))
        # print('   from: \'' + str(aModule.__file__) + '\'')
        try:
            self.registerPythonClass(aModule.__file__, aModule.__name__, aClass.__name__)
            return True
        except APIException:
            print('Fail to register class: \'' + str(aModule.__name__) + '.' + str(aClass.__name__) + '\'')
            print('   from: \'' + str(aModule.__file__) + '\'')
            import traceback
            traceback.print_exc()
        return False

    def registerModule(self, aModuleName):
        import sys
        import inspect
        def __getModuleClassList(aModule):
            """ return a list of a tuple of (className; class)"""
            # print('getModuleClassList: ' + str(aModule))
            classList = []
            for classDesc in inspect.getmembers(aModule, inspect.isclass):
                classList.append(classDesc[1])
            return classList

        # ----------------------------------------------------
        # print('Register module: ' + str(aModuleName))
        mod = sys.modules[aModuleName]

        self._unregisterAllClasses(mod)
        classRegistered = False
        for cls in __getModuleClassList(mod):
            if self._registerClass(mod, cls):
                classRegistered = True
        # print("Done.\n")
        # if not classRegistered:
        #     raise Exception("register_module(%r): defines no classes" % aModuleName)

    # App callbacks
    def registerBeforeFileLoadedCallback(self, callable):
        """
        Register a callback to be called before a file is loaded
        Returns a callback ID that can be used later to unregister the callback

        :param callable: Function to call before a file is loaded
        :type callable: Python function
        :rtype: int
        """
        functionType = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
        f = functionType(callable)
        return self.__callbackMap._registerCallback(f, self.__registerBeforeFileLoadedCallback)

    def registerAfterFileLoadedCallback(self, callable):
        """
        Register a callback to be called after a file is loaded
        Returns a callback ID that can be used later to unregister the callback

        :param callable: Function to call after a file is loaded
        :type callable: Python function
        :rtype: int
        """
        functionType = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_bool, ctypes.c_bool)
        f = functionType(callable)
        return self.__callbackMap._registerCallback(f, self.__registerAfterFileLoadedCallback)

    def registerBeforeFileSavedCallback(self, callable):
        """
        Register a callback to be called before a file is saved
        Returns a callback ID that can be used later to unregister the callback

        :param callable: Function to call before a file is saved
        :type callable: Python function
        :rtype: int
        """
        functionType = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_char_p)
        f = functionType(callable)
        return self.__callbackMap._registerCallback(f, self.__registerBeforeFileSavedCallback)

    def registerAfterFileSavedCallback(self, callable):
        """
        Register a callback to be called after a file is saved
        Returns a callback ID that can be used later to unregister the callback

        :param callable: Function to call after a file is saved
        :type callable: Python function
        :rtype: int
        """
        functionType = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_bool)
        f = functionType(callable)
        return self.__callbackMap._registerCallback(f, self.__registerAfterFileSavedCallback)

    def unregisterCallback(self, callbackID):
        """
        Unregister a callback

        :param callbackID: The callback ID of the callback to unregister
        :type callbackID: int
        :rtype: None
        """
        self.__callbackMap._unregisterCallback(callbackID, self.__unregisterCallback)

    # Manually written code patched in by IPA ends
