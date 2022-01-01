import os
import unittest

from pyrmanent import Pyrmanent


class Example(Pyrmanent):
    def init(self):
        self.menu = "pizza"


class TestPersistency(unittest.TestCase):
    def test_init_values(self):
        example = Example()
        self.assertTrue(hasattr(example, "menu"))
        self.assertEqual(example.menu, "pizza")
        os.remove("Example.pickle")

    def test_not_saved_values(self):
        example = Example()
        example.menu = "rice"
        example = Example()
        self.assertTrue(hasattr(example, "menu"))
        self.assertEqual(example.menu, "pizza")
        os.remove("Example.pickle")

    def test_saved_values(self):
        example = Example()
        example.menu = "rice"
        example.save()
        example = Example()
        self.assertTrue(hasattr(example, "menu"))
        self.assertEqual(example.menu, "rice")
        os.remove("Example.pickle")

    def test_values_for_different_names(self):
        first = Example(name="first")
        second = Example(name="second")
        first.menu = "rice"
        second.menu = "soup"
        first.save()
        second.save()
        first = Example(name="first")
        second = Example(name="second")
        self.assertTrue(hasattr(first, "menu"))
        self.assertTrue(hasattr(second, "menu"))
        self.assertEqual(first.menu, "rice")
        self.assertEqual(second.menu, "soup")
        os.remove("Example_first.pickle")
        os.remove("Example_second.pickle")