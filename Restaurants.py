import random
import os


class Restaurants:
    def __init__(self):
        """ Creates file with restaurants if file already exist copy all lines to list """
        if os.path.exists("restaurants.txt"):
            mode = "r"
        else:
            mode = "w+"
        with open("restaurants.txt", mode) as file:
            self.restaurants = [line.rstrip('\n') for line in file]

    def pick(self):
        """ Picks random restaurant from list """
        if len(self.restaurants) == 0:
            return "Restaurants list is empty use command add"
        else:
            return self.restaurants[random.randint(0, len(self.restaurants) - 1)]

    def add(self, restaurants):
        """ Adds restaurant to list """
        for restaurant in restaurants.split(","):
            if restaurant not in self.restaurants:
                self.restaurants.append(restaurant)
            else:
                print(f"{restaurant} was already added to see all restaurants use command show")
        self.update_file()

    def remove(self, restaurant):
        """ Removes restaurant from list """
        try:
            self.restaurants.remove(restaurant)
            self.update_file()
        except ValueError:
            print(f"There is no {restaurant} on a list, to see all restaurants use command show")

    def show(self):
        """ Shows all restaurants on list """
        return self.restaurants

    def update_file(self):
        """ Updates external file """
        with open("restaurants.txt", "w") as file:
            for res in self.restaurants:
                file.writelines(res + "\n")
