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

import shiboken2
from PySide2 import QtWidgets

class QtForPythonUIMgrWrapper(object):
    def __init__(self, uiMgr):
        self.__mUiMgr = uiMgr

    def getMainWindow(self):
        """
        Get the main window

        :rtype: PySide2.QtWidgets.QMainWindow
        """
        return shiboken2.wrapInstance(self.__mUiMgr.getMainWindowPtr(), QtWidgets.QMainWindow)

    def newMenu(self, menuTitle, objectName):
        """
        Create a new menu in the application menu bar

        :param menuTitle: The menu title
        :type menuTitle: string
        :param objectName: The internal object name of the menu
        :type objectName: string
        :rtype: PySide2.QtWidgets.QMenu
        """
        return shiboken2.wrapInstance(self.__mUiMgr.newMenu(menuTitle, objectName), QtWidgets.QMenu)

    def findMenuFromObjectName(self, objectName):
        """
        Return an existing menu in the application menu bar

        :param objectName: The internal object name of the menu
        :type menuName: string
        :rtype: PySide2.QtWidgets.QMenu
        """
        menuPtr = self.__mUiMgr.findMenuFromObjectName(objectName)
        if menuPtr:
            return shiboken2.wrapInstance(menuPtr, QtWidgets.QMenu)

    def deleteMenu(self, objectName):
        """
        Remove a menu from the application menu bar

        :param objectName: The internal object name of the menu
        :type objectName: string
        """
        self.__mUiMgr.deleteMenu(objectName)

    def newDockWidget(self, identifier, title):
        """
        Create a new dock widget

        :param identifier: Dock internal identifier (must be unique)
        :type identifier: string
        :param title: Dock title
        :type title: string
        :rtype: PySide2.QtWidgets.QWidget
        """
        return shiboken2.wrapInstance(self.__mUiMgr.newDockWidget(identifier, title), QtWidgets.QWidget)

    def addToolbarToGraphView(self, graphViewID, toolbar, icon=None, tooltip=None):
        """
        Add a toolbar to a graph view

        :param graphViewID: Graph view identifier
        :type graphViewID: int
        :param toolbar: Toolbar to add to the widget
        :type identifier: QToolBar
        :param toolbar: The toolbar icon
        :type identifier: QIcon
        :param tooltip: The toolbar tooltip
        :type identifier: string
        :rtype: None
        """

        action = toolbar.toggleViewAction()

        if icon:
            action.setIcon(icon)

        if tooltip:
            action.setToolTip(tooltip)

        return self.__mUiMgr.addToolbarToGraphView(
            graphViewID,
            shiboken2.getCppPointer(toolbar)[0],
            shiboken2.getCppPointer(action)[0])

    def getCurrentGraph(self):
        """
        Get the current graph (can be null)

        :rtype: SDGraph
        """
        return self.__mUiMgr.getCurrentGraph()

    def getCurrentGraphSelection(self):
        """
        Get the selected nodes in the current graph

        :rtype: SDArray[SDNode]
        """
        return self.__mUiMgr.getCurrentGraphSelection()

    def getGraphFromGraphViewID(self, graphViewID):
        """
        Get the graph from a Graph View ID (can be null)

        :param graphViewID: The Graph View ID
        :type graphViewID: int
        :rtype: SDGraph
        """
        return self.__mUiMgr.getGraphFromGraphViewID(graphViewID)

    def getCurrentGraphSelectionFromGraphViewID(self, graphViewID):
        """
        Get the selected nodes in a graph from a Graph View ID (can be null)

        :param graphViewID: The Graph View ID
        :type graphViewID: int
        :rtype: SDArray[SDNode]
        """
        return self.__mUiMgr.getCurrentGraphSelectionFromGraphViewID(graphViewID)

    def addActionToExplorerToolbar(self, explorerID, action):
        """
        Add an action to an explorer toolbar

        :param explorerID: Explorer identifier
        :type explorerID: int
        :param action: action
        :type action: QAction
        :rtype: None
        """
        return self.__mUiMgr.addActionToExplorerToolbar(
            explorerID,
            shiboken2.getCppPointer(action)[0])

    def getExplorerSelection(self, explorerID):
        """
        Return the currently selected items in the explorer panel

        :param explorerID: Explorer identifier
        :type explorerID: int
        :rtype: SDArray[SDAPIObject]
        """
        return self.__mUiMgr.getExplorerSelection(explorerID)

    def registerGraphViewCreatedCallback(self, callable):
        """
        Register a callback to be called when a new graph view is created
        Returns a callback ID that can be used later to unregister the callback

        :param callable: Function to call when a new graph view is created
        :type callable: Python function
        :rtype: int
        """
        return self.__mUiMgr.registerGraphViewCreatedCallback(callable)

    def registerExplorerCreatedCallback(self, callable):
        """
        Register a callback to be called when a new explorer is created
        Returns a callback ID that can be used later to unregister the callback

        :param callable: Function to call when a new explorer is created
        :type callable: Python function
        :rtype: int
        """
        return self.__mUiMgr.registerExplorerCreatedCallback(callable)

    def registerExplorerSelectionChangedCallback(self, callable):
        """
        Register a callback to be called when the explorer selection changed
        Returns a callback ID that can be used later to unregister the callback

        :param callable: Function to call when the explorer selection changed
        :type callable: Python function
        :rtype: int
        """
        return self.__mUiMgr.registerExplorerSelectionChangedCallback(callable)

    def unregisterCallback(self, callbackID):
        """
        Unregister a callback

        :param callbackID: The callback ID of the callback to unregister
        :type callbackID: int
        :rtype: None
        """
        self.__mUiMgr.unregisterCallback(callbackID)
