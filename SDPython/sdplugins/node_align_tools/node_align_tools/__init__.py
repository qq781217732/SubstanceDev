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

from functools import partial
import os
import weakref

import sd
from sd.tools import graphlayout

from PySide2 import QtCore, QtGui, QtWidgets, QtSvg

DEFAULT_ICON_SIZE = 24

def loadSvgIcon(iconName, size):
    currentDir = os.path.dirname(__file__)
    iconFile = os.path.abspath(os.path.join(currentDir, iconName + '.svg'))

    svgRenderer = QtSvg.QSvgRenderer(iconFile)
    if svgRenderer.isValid():
        pixmap = QtGui.QPixmap(QtCore.QSize(size, size))

        if not pixmap.isNull():
            pixmap.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(pixmap)
            svgRenderer.render(painter)
            painter.end()

        return QtGui.QIcon(pixmap)

    return None

class NodeAlignmentToolBar(QtWidgets.QToolBar):
    __toolbarList = {}

    def __init__(self, graphViewID, uiMgr):
        super(NodeAlignmentToolBar, self).__init__(parent=uiMgr.getMainWindow())

        self.setObjectName("allegorithmic.com.node_alignment_toolbar")

        self.__graphViewID = graphViewID
        self.__uiMgr = uiMgr

        act = self.addAction(loadSvgIcon("align_horizontal", DEFAULT_ICON_SIZE), "HAlign")
        act.setShortcut(QtGui.QKeySequence('H'))
        act.setToolTip(self.tr("Align the selected nodes horizontally"))
        act.triggered.connect(self.__onHorizAlignNodes)

        act = self.addAction(loadSvgIcon("align_vertical", DEFAULT_ICON_SIZE), "VAlign")
        act.setShortcut(QtGui.QKeySequence('V'))
        act.setToolTip(self.tr("Align the selected nodes vertically"))
        act.triggered.connect(self.__onVertAlignNodes)

        act = self.addAction(loadSvgIcon("align_snap", DEFAULT_ICON_SIZE), "Snap")
        act.setShortcut(QtGui.QKeySequence('S'))
        act.setToolTip(self.tr("Snap the selected nodes on grid"))
        act.triggered.connect(self.__onSnapNodes)

        self.__toolbarList[graphViewID] = weakref.ref(self)
        self.destroyed.connect(partial(NodeAlignmentToolBar.__onToolbarDeleted, graphViewID=graphViewID))

    def tooltip(self):
        return self.tr("Align Tools")

    def __onHorizAlignNodes(self):
        graphlayout.alignSDNodes(
            self.__getSelectedNodes(),
            graphlayout.AlignmentDirection.Horizontal)

    def __onVertAlignNodes(self):
        graphlayout.alignSDNodes(
            self.__getSelectedNodes(),
            graphlayout.AlignmentDirection.Vertical)

    def __onSnapNodes(self):
        graphlayout.snapSDNodes(self.__getSelectedNodes())

    def __getSelectedNodes(self):
        return self.__uiMgr.getCurrentGraphSelectionFromGraphViewID(self.__graphViewID)

    @classmethod
    def __onToolbarDeleted(cls, graphViewID):
        del cls.__toolbarList[graphViewID]

    @classmethod
    def removeAllToolbars(cls):
        for toolbar in cls.__toolbarList.values():
            if toolbar():
                toolbar().deleteLater()

def onNewGraphViewCreated(graphViewID, uiMgr):
    toolbar = NodeAlignmentToolBar(graphViewID, uiMgr)
    uiMgr.addToolbarToGraphView(
        graphViewID,
        toolbar,
        icon = loadSvgIcon("align_tools", DEFAULT_ICON_SIZE),
        tooltip = toolbar.tooltip())

graphViewCreatedCallbackID = 0

def initializeSDPlugin():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    if uiMgr:
        global graphViewCreatedCallbackID
        graphViewCreatedCallbackID = uiMgr.registerGraphViewCreatedCallback(
            partial(onNewGraphViewCreated, uiMgr=uiMgr))

def uninitializeSDPlugin():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    if uiMgr:
        global graphViewCreatedCallbackID
        uiMgr.unregisterCallback(graphViewCreatedCallbackID)
        NodeAlignmentToolBar.removeAllToolbars()
