# Core logic for recipes conversions

# User Story 1: As a user, I want to scale my ingredient quantities up or down based on a new serving size so
#   that I can adjust the recipe as needed.

# User Story 2: As a user, I want to convert my recipe between the standard and metric measurement systems
#   so that I can use the appropriate units based on my preference or available tools.

# User Story 3: As a user, I want the microservice to automatically validate the ingredients in a recipe so that
#   invalid or incomplete ingredient data can be detected before processing and does not give me incorrect or
#   unexpected results.

from models import ConversionRequest


# Function to handle scaling and unit conversion
def process_conversion(request: ConversionRequest):
    updated_ingredients = []

    # Was a new serving size included?
    if request.serving_size is True:
        for ingredient in request.ingredients:
            new_quantity = ingredient.quantity * request.serving_size
            updated_ingredients.append({
                "name": ingredient.name,
                "quantity": new_quantity,
                "unit": ingredient.unit
            })
    else:
        for ingredient in request.ingredients:
            updated_ingredients.append({
                "name": ingredient.name,
                "quantity": ingredient.quantity,
                "unit": ingredient.unit
            })

    # Was a new measurement system included?
    if request.system is True:
        if request.system == 'customary':
            for ingredient in updated_ingredients:
                ingredient["quantity"], ingredient["unit"] = conversion_to_customary(
                    ingredient["unit"], ingredient["quantity"]
                )
        elif request.system == 'metric':
            for ingredient in updated_ingredients:
                ingredient["quantity"], ingredient["unit"] = conversion_to_metric(
                    ingredient["unit"], ingredient["quantity"]
                )

    return updated_ingredients


def conversion_to_customary(metric_unit, quantity):
# WEIGHT
    # gram to ounces
    if metric_unit == 'grams' or metric_unit == 'gram':
        converted_quantity = round((quantity * 0.0352739619), 2)
        converted_unit = 'ounces'

    # kilogram to pounds
    elif metric_unit == 'kilograms' or metric_unit == 'kilogram':
        converted_quantity = round((quantity * 2.2046226218), 1)
        converted_unit = 'lbs'

# LENGTH
    # centimeter to inch
    elif metric_unit == 'centimeters' or metric_unit == 'centimeter':
        converted_quantity = round((quantity * 0.3937007874), 2)
        converted_unit = 'in'


# TEMPERATURE
    # celsius to fahrenheit
    elif metric_unit == 'celsius' or metric_unit == '°C':
        converted_quantity = round((quantity * (9/5) + 32), 1)
        converted_unit = '°F'

# VOLUME
    # milliliter to
    elif metric_unit == 'milliliters' or metric_unit == 'milliliter':
        if quantity < 15:
            converted_quantity = round((quantity * 0.2028841362), 2)
            converted_unit = 'tsp'
        elif quantity < 50:
            converted_quantity = round((quantity * 0.0676280454), 2)
            converted_unit = 'Tbsp'
        elif quantity < 71:
            converted_quantity = round((quantity * 0.0338140227), 2)
            converted_unit = 'fl oz'
        elif quantity < 1704:
            converted_quantity = round((quantity * 0.003519508), 2)
            converted_unit = 'cup'
        else:
            converted_quantity = round((quantity * 0.0021133764), 2)
            converted_unit = 'pint'

    # liter to
    elif metric_unit == 'liters' or metric_unit == 'liter':
        if quantity < .8:
            converted_quantity = round((quantity * 4.2267528377), 2)
            converted_unit = 'cup'
        elif quantity < 4:
            converted_quantity = round((quantity * 2.1133764189), 2)
            converted_unit = 'pint'
        else:
            converted_quantity = round((quantity * 0.2641720524), 2)
            converted_unit = 'gallon'

    # Error
    else:
        converted_quantity = 0
        converted_unit = 0

    return converted_quantity, converted_unit


def conversion_to_metric(customary_unit, quantity):
# WEIGHT
    # ounces to grams
    if (customary_unit == 'ounces' or customary_unit == 'ounce' or
            customary_unit == 'oz'):
        converted_quantity = round((quantity * 28.349523125), 2)
        converted_unit = 'g'

    # pounds to kilograms
    elif customary_unit == 'pounds' or customary_unit == 'pound'\
            or customary_unit == 'lbs':
        converted_quantity = round((quantity * 0.45359237), 1)
        converted_unit = 'kg'

# LENGTH
    # inch to centimeter
    elif customary_unit == 'inches' or customary_unit == 'inch':
        converted_quantity = round((quantity * 2.54), 2)
        converted_unit = 'cm'


# TEMPERATURE
    # fahrenheit to celsius
    elif customary_unit == 'fahrenheit' or customary_unit == '°F':
        converted_quantity = round(((quantity - 32) * (5/9)), 1)
        converted_unit = '°C'

# VOLUME
    # tsp to milliliter
    elif customary_unit in ('tsp', 'teaspoon', 'teaspoons'):
        converted_quantity = round(quantity * 4.9289215937, 2)
        converted_unit = 'mL'

    # Tbsp to milliliter
    elif customary_unit in ('Tbsp', 'tablespoon', 'tablespoons'):
        converted_quantity = round(quantity * 14.786764781, 2)
        converted_unit = 'mL'

    # Fluid ounce to milliliter
    elif customary_unit in ('fl oz', 'fluid ounce', 'fluid ounces'):
        converted_quantity = round(quantity * 29.573529562, 2)
        converted_unit = 'mL'

    # Cup to milliliter
    elif customary_unit in ('cup', 'cups'):
        converted_quantity = round(quantity * 236.5882365, 2)
        converted_unit = 'mL'

    # Pint to liter
    elif customary_unit in ('pint', 'pints', 'p'):
        if quantity < 2.1133764189:
            converted_quantity = round(quantity * 473.176473, 2)
            converted_unit = 'mL'
        else:
            converted_quantity = round(quantity * 0.473176473, 2)
            converted_unit = 'L'

    # Quart to liter
    elif customary_unit in ('quart', 'quarts', 'qt'):
        converted_quantity = round(quantity * 0.946352946, 2)
        converted_unit = 'L'

    # Gallon to liter
    elif customary_unit in ('gallon', 'gallons'):
        converted_quantity = round(quantity * 3.785411784, 2)
        converted_unit = 'L'

    # Error
    else:
        converted_quantity = 0
        converted_unit = 0

    return converted_quantity, converted_unit
