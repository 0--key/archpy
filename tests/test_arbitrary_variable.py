import unittest
import sys

from bunch.a_sample_variable import a


class ArbitraryContentPrimitiveTest(unittest.TestCase):
    """Does import works as expected?"""

    def test_variable_vaue(self):
        self.assertEqual(a, "An arbitrary string")
        print(sys.path)
