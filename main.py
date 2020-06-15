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
    
    def __init__(self):
        self.recipes = []

    def add_recipe(self, new_recipe):
        self.recipes.append(new_recipe)

    def print_num_recipes(self):
        print(len(self.recipes))




r1 = Recipe("Easy Basic Pancakes",
            ["1 cup all-puropse flour", "2 tablespoons sugar", "2 teaspoons baking powder", "1/2 teaspoon salt", "1 cup milk", "2 tablespoons unsalted butter, melted, or vegetable oil", "1/2 large egg", "1 tablespoon vegetable oil"],
            ["Preheat oven to 200 degrees; have a baking sheet or heatproof platter ready to keep cooked pancakes warm in the oven. In a small bowl, whisk together flour, sugar, baking powder, and salt; set aside."])
r1.list_ingredients()
print("\n")
r1.list_ingredients_no_measure()

cookbook = CookBook()


cookbook.add_recipe("new recipe")
cookbook.add_recipe("new recipe")

