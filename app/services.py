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
        scale_factor = request.serving_size
    else:
        scale_factor = False

    # Was a new measurement system included?
    if request.system is True:

#    for ingredient in request.ingredients:
#        new_quantity = ingredient.quantity


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
        converted_unit = 'pounds'

# LENGTH
    # centimeter to inch
    elif metric_unit == 'centimeters' or metric_unit == 'centimeter':
        converted_quantity = round((quantity * 0.3937007874), 2)
        converted_unit = 'inch'


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
