import sd
# Import the required classes.
from sd.api import sduimgr
from sd.api.sdproperty import *


uiMgr = app.getQtForPythonUIMgr()

# Access a node in the current graph, and its properties.
graph = uiMgr.getCurrentGraph()
print("The current graph is %s" % g)


node = graph.getNodeFromId('<Replace this text with the node ID>')
nodeProps = node.getProperties(SDPropertyCategory.Input)

# List node identifiers and types in console.
for i in range(len(nodeProps)):
	print(nodeProps[i].getId())
	print(nodeProps[i].getType())
