# https://www.testdome.com/questions/python/ice-cream-machine/94857

class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        combination=[]
        for ing in range(len(self.ingredients)):
            for top in range(len(self.toppings)):
                combination.append([self.ingredients[ing], self.toppings[top]])
        return combination



if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())  # should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
# ingredients=["vanilla", "chocolate"]
# toppings=["chocolate sauce"]
# combination=[]
# for ing in range(len(ingredients)):
#     for top in range(len(toppings)):
#         combination.append([ingredients[ing], toppings[top]])
# print(combination)