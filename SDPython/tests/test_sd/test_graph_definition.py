import unittest
from samples.plugins.custom_graph.custom_graph import *


class TestGraphDefinition(unittest.TestCase):

    def runTest(self):
        CustomGraph.init('custom_graph_test')


if __name__ == '__main__':
    TestGraphDefinition().runTest()

