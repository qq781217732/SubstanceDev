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
