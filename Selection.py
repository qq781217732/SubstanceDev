import sd
context = sd.getContext()
sd_app = context.getSDApplication()
ui_manager = sd_app.getQtForPythonUIMgr()
print('Katana')
node_list = ui_manager.getCurrentGraphSelection()

for node in node_list:
    print(node)
    print('OK')