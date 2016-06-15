import list
import unittest

class test_stuff_with_lists(unittest.TestCase):
    def test_is_this_thing_on(self):
        self.assertEqual(True, list.check())