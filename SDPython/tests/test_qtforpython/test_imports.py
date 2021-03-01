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

import importlib
import platform
import unittest

def isDesignerSDK():
    import sd
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    return app.getUIMgr() == None

class TestQtForPython(unittest.TestCase):

    @unittest.skipIf(isDesignerSDK(), "Test requires Designer")
    def test_import(self):
        """
        Test that PySide modules load correctly
        """
        components = [
            'Charts',
            'Concurrent',
            'Core',
            'Gui',
            'Multimedia',
            'MultimediaWidgets',
            'Network',
            'OpenGL',
            'PrintSupport',
            'Qml',
            'Quick',
            'QuickWidgets',
            'Sql',
            'Svg',
            'UiTools',
            'WebSockets',
            'Widgets',
            'Xml',
            'XmlPatterns',
        ]
        if platform.system() == 'Linux':
            components += ['X11Extras']
        elif platform.system() == 'Darwin':
            components += ['MacExtras']
        elif platform.system() == 'Windows':
            components += ['WinExtras']

        for component_name in components:
            with self.subTest(component_name=component_name):
                module_name = f"PySide2.Qt{component_name}"
                try:
                    module = importlib.import_module(module_name)
                except Exception as e:
                    self.fail(f'Import of {module_name} failed with exception "{e}".')

if __name__ == '__main__':
    unittest.main()
