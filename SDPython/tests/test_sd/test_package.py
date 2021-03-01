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

import unittest
import sd
from tests import tools


class TestPackage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        context = sd.getContext()

        # Load the reference package
        cls.sdPackage = tools.loadSDPackage(context, 'test_sdpackage.sbs')

        # Load some other packages
        cls.sdPackageTestNewContent = tools.loadSDPackage(context, 'test_write_content.sbs')

    def testPackagesLoaded(self):
        self.assertTrue(self.sdPackage, 'Fail to load package')
        self.assertTrue(self.sdPackageTestNewContent, 'Fail to load package')

    def test_SDPackage_getChildrenResources(self):
        # Check Non Recursive mode
        sbsResourceArray = self.sdPackage.getChildrenResources(False)
        self.assertEqual(len(sbsResourceArray), 3)

        # Check Recursive Mode
        sbsResourceArray = self.sdPackage.getChildrenResources(True)
        self.assertEqual(len(sbsResourceArray), 5)

    def test_SDPackage_findResourceFromUrl(self):
        # Check that a resource of the reference package can be retrieved
        sbMDLSubGraph = self.sdPackage.findResourceFromUrl('folder0/mdl_sub_graph')
        self.assertTrue(sbMDLSubGraph)

        # Check that a resource in another can't be found in the reference package
        sbPBRGraph = self.sdPackage.findResourceFromUrl('pbr_graph')
        self.assertFalse(sbPBRGraph)

    def test_SDPackage_getDependencies(self):
        pkgDeps = self.sdPackage.getDependencies()
        self.assertEqual(len(pkgDeps), 1)
        firstPkgDep = pkgDeps[0]
        self.assertTrue(len(firstPkgDep.getFilePath())>0)
        self.assertTrue(firstPkgDep.getPackage())

if __name__ == '__main__':
    unittest.main()

