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
import sd
from PySide2 import QtWidgets

# Get the application and the UI Manager.
app = sd.getContext().getSDApplication()
uiMgr = app.getQtForPythonUIMgr()

# Create a new dialog. For shortcuts to work correctly
# it is important to parent the new dialog to Designer's main window.
mainWindow = uiMgr.getMainWindow()
dialog = QtWidgets.QDialog(parent=mainWindow)

# Create a layout and some widgets.
layout = QtWidgets.QVBoxLayout()
layout.addWidget(QtWidgets.QPushButton("Press Me"))
dialog.setLayout(layout)

# Show the dialog (non-modal).
dialog.show()
print('AAA')
