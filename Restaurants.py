import random
import os


class RestaurantsArgumentError(Exception):
    pass


class Restaurants:
    def __init__(self, path):
        """ Creates file with restaurants if file already exist copy all lines to list """
        self.path = path
        if os.path.exists(path):
            mode = "r"
        else:
            mode = "w+"
        with open(path, mode) as file:
            self.restaurants = [line.rstrip('\n') for line in file]

    def pick(self):
        """ Picks random restaurant from list """
        if len(self.restaurants) == 0:
            return "Restaurants list is empty use command add"
        else:
            return random.choice(self.restaurants)

    def add(self, restaurants):
        """ Adds restaurant to list """
        for restaurant in restaurants.split(","):
            if restaurant not in self.restaurants:
                self.restaurants.append(restaurant)
            else:
                raise RestaurantsArgumentError(f"'{restaurant}' was already added "
                                               f"to see all restaurants use command show")
        self.update_file()

    def remove(self, restaurant):
        """ Removes restaurant from list """
        try:
            self.restaurants.remove(restaurant)
            self.update_file()
        except ValueError:
            raise RestaurantsArgumentError(f"There is no '{restaurant}' on a list, "
                                           f"to see all restaurants use command show")

    def show(self):
        """ Shows all restaurants on list """
        return self.restaurants

    def update_file(self):
        """ Updates external file """
        with open(self.path, "w") as file:
            for res in self.restaurants:
                file.writelines(res + "\n")
