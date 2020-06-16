class Recipe:
    #Recipe Class:
    def __init__(self, name, pTime, cTime, servings, ingr, inst):
        self.name = name
        self.prep_time = pTime
        self.cook_time = cTime
        self.servings = servings
        self.ingr = ingr
        self.inst = inst

        ingr_no_meas = []
        for ingredient in ingr:
            ingr_no_meas.append(remove_measurement(ingredient))
        self.ingr_no_meas = ingr_no_meas

    def num_ingredients(self):
        #Returns the number of ingredients in a recipe.
        return len(self.ingr)

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
        self.all_ingredients = []

    def add_recipe(self, new_recipe):
        #Adds the new recipe to a master list and adds the ingredients from the recipe to a master list.
        self.recipes.append(new_recipe)
        
        for x in new_recipe.ingr_no_meas:
            if x not in self.all_ingredients:
                self.all_ingredients.append(x)

    def print_all_ingredients(self):
        #Prints a list of all the ingredients from all of the recipes in the cookbook and the amount of times they occur.
        for x in self.all_ingredients:
            print(x)


    def print_num_recipes(self):
        print(len(self.recipes))
        

    def recommend_recipes(self, on_hand_ingredients, percentage):
        #Takes a list of on hand ingredients and a percentage and returns a list of recipes that is greater than or equal to the percentage of ingredients on hand.
        returned_recipes = []
        for recipe in self.recipes:
            counter = 0
            for ingredient in recipe.ingr_no_meas:
                if ingredient in on_hand_ingredients:
                    counter = counter + 1
            if (counter / recipe.num_ingredients()) >= (percentage / 100):
                returned_recipes.append(recipe)
        return returned_recipes


#Helper Functions:
    #possibly move this function inside the recipe class
def remove_measurement(ingredient):
    #Takes a string that represents an ingredient and returns a string without measurement units.
    measurment_types = ['teaspoons','tablespoons','pounds','ounces','pints','milliliters','liters','kilograms','grams','cups','teaspoon','tablespoon','pound','ounce','pint','milliliter','liter','kilogram','gram','cup']
    for mUnit in measurment_types:
        #Handles the base case of there being a measurement unit in the passed string.
        if mUnit in ingredient:
            return ingredient[(ingredient.rfind(mUnit)+len(mUnit)+1):]
        #Handles the case where the end up the measurement type list was reached and not added.
        if mUnit == measurment_types[len(measurment_types)-1]:
            #Handles the case of there being no numbers in ingredient description and no formating is needed.
            if ingredient.isalpha():
                return ingredient
            #Handles case of there being a number in the string.
            return ingredient[(ingredient.find(" ")+1):]


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

for x in cookbook.recommend_recipes(["all-puropse flour", "sugar", "baking powder"], 1):
    print(x.name)


