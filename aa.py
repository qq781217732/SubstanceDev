import sd

# Get the application and UI manager object.
ctx = sd.getContext()
app = ctx.getSDApplication()
uiMgr = app.getQtForPythonUIMgr()

# Get the current graph.
g = uiMgr.getCurrentGraph()
print("The current graph is %s" % g)

# Get the currently selected nodes.
selection = uiMgr.getCurrentGraphSelection()
for node in selection:
	print("Node %s" % node)