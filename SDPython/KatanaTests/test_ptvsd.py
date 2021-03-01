import ptvsd 
# Allow other computers to attach to ptvsd at this IP address and port.
ptvsd.enable_attach()
# Pause the program until a remote debugger is attached

ptvsd.wait_for_attach()
