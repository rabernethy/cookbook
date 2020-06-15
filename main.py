class Recipe:
    #Recipe Class:
    def __init__(self, name, pTime, cTime, servings, ingr, inst):
        self.name = name
        self.prep_time = pTime
        self.cook_time = cTime
        self.servings = servings
        self.ingr = ingr
        self.inst = inst
        #Create a list of ingredients without the measurments so that it can be searched later.
        measurment_types = ['teaspoons','tablespoons','pounds','ounces','pints','milliliters','liters','kilograms','grams','cups','teaspoon','tablespoon','pound','ounce','pint','milliliter','liter','kilogram','gram','cup']
        ingr_no_meas = []
        for x in ingr:
           for y in measurment_types:
               #If there measurement unit in the string, remove it and everything that comes before it.
               if y in x:
                  ingr_no_meas.append(x[(x.rfind(y)+len(y)+1):])
                  break
               if y == measurment_types[len(measurment_types)-1]:
                   #Handles the case of there being no numbers in ingredient description and no formating is needed.
                   if x.isalpha():
                      ingr_no_meas.append(x)
                      break
                    #Handles case of there being a number in the string.
                   ingr_no_meas.append(x[(x.find(" ")+1):])
        self.ingr_no_meas = ingr_no_meas

    def list_ingredients(self):
        #Prints a list of ingredients in the recipe.
        for items in self.ingr:
            print(items)

    def list_ingredients_no_measure(self):
        #Prints a list of ingredients with no measurements in the recipe
        for items in self.ingr_no_meas:
            print(items)
            
    def list_instructions(self):
        #Prints a list of instructions in the recipe.
        for items in self.inst:
            print(items)

          
class CookBook:
    #Cookbook Object:
    def __init__(self):
        self.recipes = []
        self.all_ingredients = None

    def add_recipe(self, new_recipe):
        #Adds the new recipe to a master list and adds the ingredients from the recipe to a master list.
        self.recipes.append(new_recipe)
        for x in new_recipe.ingr_no_meas:
            if self.all_ingredients is None:
                self.all_ingredients = Node(x)
            else:
                binary_insert(self.all_ingredients, Node(x))

    def print_all_ingredients(self):
        #Prints a list of all the ingredients from all of the recipes in the cookbook and the amount of times they occur.
        in_order_print(self.all_ingredients)


    def print_num_recipes(self):
        print(len(self.recipes))
        

class Node:
    #Node For BST. Used to keep track of master ingredient list.
    def __init__(self, val):
        self.Left = None
        self.Right = None
        self.data = val
        self.counter = 1
        
    def inc_counter(self):
        #Increases the node's counter. Method is called when there is a duplicate node in the tree.
        self.counter = self.counter + 1

    def dec_counter(self):
        #Decreases the node's counter. Method is called when removing a node.
        self.counter = counter - 1
    
    def print_node(self):
        #Prints an individual Node. (Meant for bug testing, BST is printed by in_order_print().)
        print(self.data + self.counter)
        
def binary_insert(root, Node):
    #Inserts elements into BST. Calls inc_counter() when duplicate entry is found.
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
    #Prints BST using In Order Traversal.
    if not root:
        return
    in_order_print(root.Left)
    print(root.data +' (' + str(root.counter) + ')')
    in_order_print(root.Right)




#Driver Code:
    
r1 = Recipe("Easy Basic Pancakes",5,5,5,
            ["1 cup all-puropse flour", "2 tablespoons sugar", "2 teaspoons baking powder", "1/2 teaspoon salt", "1 cup milk", "2 tablespoons unsalted butter, melted, or vegetable oil", "1/2 large egg", "1 tablespoon vegetable oil"],
            ["Preheat oven to 200 degrees; have a baking sheet or heatproof platter ready to keep cooked pancakes warm in the oven. In a small bowl, whisk together flour, sugar, baking powder, and salt; set aside."])
r2 = Recipe("Test",5,5,5,
            ["1 cup all-puropse flour", "2 tablespoons sugar"],
            ["Just shove it in the oven"])

cookbook = CookBook()

cookbook.add_recipe(r1)
cookbook.add_recipe(r2)

cookbook.print_all_ingredients()
