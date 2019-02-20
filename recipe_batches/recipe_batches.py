#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    """Calculates the largest number of batches of a recipe possible."""
    low_multiple = None
    # Determine which ingredient has the least on hand, in terms of amount
    # needed to make the recipe.
    for ingredient in recipe.keys():
        # If the ingredient isn't on hand, we can make 0 (Zero) batches.
        if(not (ingredient in ingredients)):
            low_multiple = 0
            break
        # Calculate batches possible for ingredient
        amount_needed = recipe[ingredient]
        amount_have = ingredients[ingredient]
        possible_batches = int(amount_have / amount_needed)
        # The amount we're able to make can't be more than this number.
        if(low_multiple is None or low_multiple > possible_batches):
            low_multiple = possible_batches
    return low_multiple


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    msg = "{batches} batches can be made from the available ingredients: {ingredients}."
    msg = msg.format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients)
    print(msg)
