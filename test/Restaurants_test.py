import os
import unittest
from Restaurants import Restaurants, RestaurantsArgumentError


class RestaurantTests(unittest.TestCase):

    def test_pick(self):
        x = Restaurants("test.txt")
        assert x.pick() == "Restaurants list is empty use command add"
        os.remove("test.txt")

    def test_add(self):
        x = Restaurants("test.txt")
        x.add("test")
        assert "test" in x.restaurants
        try:
            x.add("test")
            self.fail("Exception should be thrown")
        except RestaurantsArgumentError as e:
            assert str(e) == "'test' was already added to see all restaurants use command show"
        os.remove("test.txt")

    def test_remove(self):
        x = Restaurants("test.txt")
        x.add("test")
        x.remove("test")
        assert "test" not in x.restaurants
        try:
            x.remove("test")
            self.fail("Exception should be thrown")
        except RestaurantsArgumentError as e:
            assert str(e) == "There is no 'test' on a list, to see all restaurants use command show"
        os.remove("test.txt")


if __name__ == '__main__':
    unittest.main()
