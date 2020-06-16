"""
Author: Russell Abernethy
Written with Python v3.8.3
Date: 6/16/20
Desc: A searchable cookbook that can recommend recipes based on the ingredients you already have.
"""

from operator import attrgetter

class Recipe:
    
    """
    Recipe Object: Used to store information about a cooking recipe.
    
    - name: The name of the recipe.
    - prep_time: The prep time required for the recipe (minutes).
    - cook_time: The cook time required for the recipe (minutes).
    - total_time: The total time required to make a recipe (minutes).
    - servings: The number of servings the recipe produces.
    - ingr: A list of ingredients required to make the recipe.
    - ingr_no_meas: A list of ingredients required to make to recipe without meaurments.
    - inst: A list of instructions for making the recipe.
    """
    
    def __init__(self, name, pTime, cTime, servings, ingr, inst):
        self.name = name
        self.prep_time = pTime
        self.cook_time = cTime
        self.servings = servings
        self.ingr = ingr
        self.inst = inst
        self.total_time = pTime +cTime
        ingr_no_meas = []
        for ingredient in ingr:
            ingr_no_meas.append(remove_measurement(ingredient))
        self.ingr_no_meas = ingr_no_meas

    def __str__(self):
        #String representation (mostly here for testing, use print full recipe for full print-out).
        return self.name

    def num_ingredients(self):
        #Returns the number of ingredients in a recipe.
        return len(self.ingr)

    def list_ingredients(self):
        #Prints a list of ingredients in the recipe.
        for items in self.ingr:
            print(items)

    def list_ingredients_no_measure(self):
        #Prints a list of ingredients with no measurements in the recipe.
        for items in self.ingr_no_meas:
            print(items)
            
    def list_instructions(self):
        #Prints a list of instructions in the recipe.
        for items in self.inst:
            print(items)
    def print_full_recipe(self):
        #Prints out a full version of the recipe for the user.
        print('\n')
        print('Recipe name: ' + str(self.name))
        print('Prep time: ' + str(self.prep_time))
        print('Cook time: ' + str(self.cook_time))
        print('Total time: ' + str(self.total_time))
        print('Servings: ' + str(self.servings))
        print('\n')
        print('Ingredients: ')
        for x in self.ingr:
            print('- ' + x)
        print('\n')
        print('Instructions: ')
        for x, instructions in enumerate(self.inst, 1):
            print(x, '. ' + instructions + '\n', sep='',end='')

          
class CookBook:
    """
    Cookbook Object: used to store and manipulate recipe objects.
    
    - recipes: A list of recipes that have been added to the cookbook.
    - all_ingredients: A list of all the ingredients, without measurements, that are used in recipes that have been added to the cookbook.
    """
    def __init__(self):
        self.recipes = []
        self.all_ingredients = []

    def add_recipe(self, new_recipe):
        #Adds the new recipe to a master list and adds the ingredients from the recipe to a master list.
        self.recipes.append(new_recipe)
        for x in new_recipe.ingr_no_meas:
            if x not in self.all_ingredients:
                self.all_ingredients.append(x)
                
    def num_occurance(self, search):
        #Returns the number of recipes a passed ingredient occurs in.
        counter = 0
        for recipe in self.recipes:
            for ingredient in recipe.ingr_no_meas:
                if search in ingredient:
                    counter += 1
                    break
        return counter

    def num_recipes(self):
        #Returns the number of recipes in the cookbook.
        return len(self.recipes)

    def recommend_recipes(self, on_hand_ingredients, percentage):
        #Takes a list of on hand ingredients and a percentage and returns a list of recipes that is greater than or equal to the percentage of ingredients on hand.
        returned_recipes = []
        for recipe in self.recipes:
            counter = 0
            #Sum up the number of ingredients that are in both lists.
            for ingredient in recipe.ingr_no_meas:
                if ingredient in on_hand_ingredients:
                    counter += 1
            #If the percentage the lists have in common is greater than or equal to the passed percentage, add the recipe to the returned list.
            if (counter / recipe.num_ingredients()) >= (percentage / 100):
                returned_recipes.append(recipe)
        return returned_recipes

    def print_recipe(self, search):
        #Prints out an recipe page for a recipe that matches the name passed. If multiple recipes match the name, program with prompt user to pick one.
        found_recipes = []
        #Loop through all of the recipes and add any that contain the passed string to a list.
        for recipe in self.recipes:
            if search.casefold() in recipe.name.casefold():
                found_recipes.append(recipe)
        #Handles case of there being no results.
        if len(found_recipes) == 0:
            print('Sorry, no recipes were found with that name')
        #Handles case of there being multiple results.
        if len(found_recipes) > 1:
            print('There were multiple recipes with that name, please enter the number of the recipe you would like to print:')
            for i, recipe_name in enumerate(found_recipes, 1):
                print(i, '. ' + recipe_name.name + '\n', sep='',end='')
            #Sentinel Loop to verify choice.
            while(True):
                choice = int(input('Your choice: '))
                if choice < 1 or choice > len(found_recipes):
                    print('Sorry, you did not enter a valid recipe number, please try again.')
                else:
                    found_recipes[choice-1].print_full_recipe()
                    break
        #Handles case of there being one result
        if len(found_recipes) == 1:
            found_recipes[0].print_full_recipe()
            
    #Sorting Methods:
    def alpha_order_list(self):
        #Returns a list of recipe names in alphabetical order.
        return sorted(self.recipes, key=attrgetter('name'))

    def rev_alpha_order_list(self):
        #Returns a list of recipe names in reverse alphabetical order.
        return sorted(self.recipes, key=attrgetter('name'), reverse=True)

    def serv_asc_order_list(self):
        #Returns a list of recipe based on servings in ascending order.
        return sorted(self.recipes, key=attrgetter('servings'))

    def serv_dec_order_list(self):
        #Returns a list of recipe based on servings in decending order.
        return sorted(self.recipes, key=attrgetter('servings'), reverse=True)
    
    def pTime_asc_order_list(self):
        #Returns a list of recipe based on prep time in ascending order.
        return sorted(self.recipes, key=attrgetter('prep_time'))
    
    def pTime_dec_order_list(self):
        #Returns a list of recipe based on prep time in decending order.
        return sorted(self.recipes, key=attrgetter('prep_time'), reverse=True)

    def cTime_asc_order_list(self):
        #Returns a list of recipe based on cook time in ascending order.
        return sorted(self.recipes, key=attrgetter('cook_time'))

    def cTime_dec_order_list(self):
        #Returns a list of recipe based on cook time in decending order.
        return sorted(self.recipes, key=attrgetter('cook_time'), reverse=True)

    def tTime_asc_order_list(self):
        #Returns a list of recipe based on total time in ascending order.
        return sorted(self.recipes, key=attrgetter('total_time'))

    def tTime_dec_order_list(self):
        #Returns a list of recipe based on total time in decending order.
        return sorted(self.recipes, key=attrgetter('total_time'), reverse=True)
   
        
#Helper Functions:
def remove_measurement(ingredient):
    #Takes a string that represents an ingredient and returns a string without measurement units.
    measurment_types = ['teaspoons','tablespoons','pounds','ounces','pints','milliliters','liters','kilograms','grams','cups','teaspoon','tablespoon','pound','ounce','pint','milliliter','liter','kilogram','gram','cup', 'package','packages', 'quart', 'quarts']
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
    #name, pTime, cTime, servings, ingr, inst
r1 = Recipe('Easy Basic Pancakes',5,5,5,
            ['1 cup all-puropse flour', '2 tablespoons sugar', '2 teaspoons baking powder', '1/2 teaspoon salt', '1 cup milk', '2 tablespoons unsalted butter, melted, or vegetable oil', '1/2 large egg', '1 tablespoon vegetable oil'],
            ['Preheat oven to 200 degrees; have a baking sheet or heatproof platter ready to keep cooked pancakes warm in the oven. In a small bowl, whisk together flour, sugar, baking powder, and salt; set aside.', 'In a medium bowl, whisk together milk, butter (or oil), and egg. Add dry ingredients to milk mixture; whisk until just moistened (do not overmix; a few small lumps are fine).', 'Heat a large skillet (nonstick or cast-iron) or griddle over medium. Fold a sheet of paper towel in half, and moisten with oil; carefully rub skillet with oiled paper towel.', 'For each pancake, spoon 2 to 3 tablespoons of batter onto skillet, using the back of the spoon to spread batter into a round (you should be able to fit 2 to 3 in a large skillet).', 'Cook until surface of pancakes have some bubbles and a few have burst, 1 to 2 minutes. Flip carefully with a thin spatula, and cook until browned on the underside, 1 to 2 minutes more. Transfer to a baking sheet or platter; cover loosely with aluminum foil, and keep warm in oven. Continue with more oil and remaining batter. (You\'ll have 12 to 15 pancakes.) Serve warm, with desired toppings.'])

r2 = Recipe('French Onion-Breaded Baked Chicken', 10, 25, 4,
            ['1 cup bread crumbs', '1 ounce dry French onion soup mix', '1/3 cup mayonnaise', '1 tablespoon garlic paste', '4 boneless chicken breasts'],
            ['Preheat the oven to 425 degrees F (220 degrees C).', 'Mix bread crumbs and dry soup mix together in a bowl.', 'Mix mayonnaise and garlic paste together in a separate bowl. Microwave on high to thin out consistency, 20 to 30 seconds.',
             'Brush chicken breasts with the mayonnaise mixture. Cover with the crumb mixture. Place on a baking sheet.',
             'Bake on the middle rack of the preheated oven until chicken is no longer pink in the center and juices run clear, about 20 minutes. An instant-read thermometer inserted into the center should read at least 165 degrees F (74 degrees C).'])

r3 = Recipe('Fish Tacos', 40,20, 8,
            ['1 cup all-purpose flour', '2 tablespoons cornstarch', '1 teaspoon baking powder', '1/2 teaspoon salt', '1 egg', '1 cup beer', '1/2 cup plain yogurt', '1/2 cup mayonnaise', '1 lime, juiced', '1 jalapeno pepper, minced', '1 teaspoon minced capers', '1/2 teaspoon dried oregano', '1/2 teaspoon ground cumin', '1/2 teaspoon dried dill weed', '1 teaspoon ground cayenne pepper', '1 quart oil for frying', '1 pound cod fillet (cut into 2-3 oz pieces)', '1 package corn tortillas', '1/2 medium head cabbage, finely shredded'],
            ['To make beer batter: In a large bowl, combine flour, cornstarch, baking powder, and salt. Blend egg and beer, then quickly stir into the flour mixture (don\'t worry about a few lumps).', 'To make white sauce: In a medium bowl, mix together yogurt and mayonnaise. Gradually stir in fresh lime juice until consistency is slightly runny. Season with jalapeno, capers, oregano, cumin, dill, and cayenne.', 'Heat oil in deep-fryer to 375 degrees F (190 degrees C).', 'Dust fish pieces lightly with flour. Dip into beer batter, and fry until crisp and golden brown. Drain on paper towels. Lightly fry tortillas; not too crisp. To serve, place fried fish in a tortilla, and top with shredded cabbage, and white sauce.'])

c = CookBook()

c.add_recipe(r1)
c.add_recipe(r2)
c.add_recipe(r3)

c.print_recipe("e")
