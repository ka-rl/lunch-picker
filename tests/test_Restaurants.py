import os
import unittest
from Restaurants import Restaurants, RestaurantsArgumentError


class RestaurantTests(unittest.TestCase):
    def setUp(self):
        self.class_manager = Restaurants("tests.txt")

    def tearDown(self):
        os.remove("tests.txt")

    def test_pick(self):
        self.assertEqual(self.class_manager.pick(), "Restaurants list is empty use command add")

    def test_add(self):
        self.class_manager.add("tests")
        self.assertIn("tests", self.class_manager.restaurants)
        self.assertRaises(RestaurantsArgumentError, self.class_manager.add, "tests")

    def test_remove(self):
        self.class_manager.add("tests")
        self.class_manager.remove("tests")
        self.assertNotIn("tests", self.class_manager.restaurants)
        self.assertRaises(RestaurantsArgumentError, self.class_manager.remove, "tests")


if __name__ == '__main__':
    unittest.main()
