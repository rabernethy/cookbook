class Recipe:
    """Recipe Class intented for storing information about a particular recipe such as name, ingredientsm"""
    def __init__(self, name, ingr, inst):
        
        self.name = name
        self.ingr = ingr
        self.inst = inst
        
        """create a list of ingredients without the measurments so that it can be searched later"""
        measurment_types = ['teaspoons','tablespoons','pounds','ounces','pints','milliliters','liters','kilograms','grams','cups','teaspoon','tablespoon','pound','ounce','pint','milliliter','liter','kilogram','gram','cup']
        ingr_no_meas = []
        for x in ingr:
           for y in measurment_types:
               if y in x:
                  ingr_no_meas.append(x[(x.rfind(y)+len(y)+1):])
                  break
               if y == measurment_types[len(measurment_types)-1]:
                   if x.isalpha():
                      ingr_no_meas.append(x)
                      break
                   ingr_no_meas.append(x[(x.find(" ")+1):])
        self.ingr_no_meas = ingr_no_meas

    def list_ingredients(self):
        for items in self.ingr:
            print(items)
            
    def list_instructions(self):
        for items in self.inst:
            print(items)

    def list_ingredients_no_measure(self):
        for items in self.ingr_no_meas:
            print(items)
            
class CookBook:
    """Cookbook object that keeps track of all of the recipes added. """
    def __init__(self):
        self.recipes = []
        self.all_ingredients = None

    def add_recipe(self, new_recipe):
        """ Adds the recipe to a master list and add's the ingredients from the recipe to a master list """
        self.recipes.append(new_recipe)
        for x in new_recipe.ingr_no_meas:
            if self.all_ingredients is None:
                self.all_ingredients = Node(x)
            else:
                binary_insert(self.all_ingredients, Node(x))

    def print_all_ingredients(self):
        in_order_print(self.all_ingredients)


    def print_num_recipes(self):
        print(len(self.recipes))

class Node:
    """BST for storing the ingredients and how often they are used in recipes"""
    def __init__(self, val):
        self.Left = None
        self.Right = None
        self.data = val
        self.counter = 1
        
    def inc_counter(self):
        self.counter = self.counter + 1

    def print_node(self):
        print(self.data + self.counter)
        
def binary_insert(root, Node):
    """Inserts elements into the binary search tree. This binary insert keeps track of duplicates by incrementing a counter """
    if root is None:
        root = Node
    else:
        if Node.data == root.data:
            root.inc_counter()
        else:
            if root.data > Node.data:
                if root.Left is None:
                    root.Left = Node
                else:
                    binary_insert(root.Right, Node)
            else:
                if root.Right is None:
                    root.Right = Node
                else:
                    binary_insert(root.Right, Node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.Left)
    print(root.data +' (' + str(root.counter) + ')')
    in_order_print(root.Right)





r1 = Recipe("Easy Basic Pancakes",
            ["1 cup all-puropse flour", "2 tablespoons sugar", "2 teaspoons baking powder", "1/2 teaspoon salt", "1 cup milk", "2 tablespoons unsalted butter, melted, or vegetable oil", "1/2 large egg", "1 tablespoon vegetable oil"],
            ["Preheat oven to 200 degrees; have a baking sheet or heatproof platter ready to keep cooked pancakes warm in the oven. In a small bowl, whisk together flour, sugar, baking powder, and salt; set aside."])
r2 = Recipe("Test",
            ["1 cup all-puropse flour", "2 tablespoons sugar"],
            ["Just shove it in the oven"])
cookbook = CookBook()


cookbook.add_recipe(r1)
cookbook.add_recipe(r2)
cookbook.print_all_ingredients()


