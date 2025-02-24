import requests
import json

url = 'http://127.0.0.1:8000'
headers = {"Content-Type": "application/json"}


def send_post_request(json_request):
    response = requests.post(url+'/conversion', json=json_request, headers=headers)

    # Check if the request was successful and print the response
    if response.status_code == 200:
        print("Response from microservice:")
        print(json.dumps(response.json(), indent=4))  # Print the converted ingredients data/ pretty print
    else:
        print(f"Error: {response.status_code}")


def get_user_ingredients(num_ingredients):

    print("\nPlease enter", num_ingredients, "ingredients (name, quantity, unit)")
    ingredients = []

    for num in range(num_ingredients):
        name = input("Ingredient name: ").strip()
        quantity = float(input("Quantity: ").strip())
        unit = input("Unit: ").strip()
        print()
        ingredients.append({"name": name, "quantity": quantity, "unit": unit})

    return ingredients


def get_user_choice():
    """Show menu options and return user's choice."""
    print("\nChoose an option:")
    print("1. Scale the recipe")
    print("2. Convert units to different system")
    print("3. Both scale and convert systems")
    print("4. Start over with new ingredients")
    print("5. Exit")

    return int(input("\nEnter your choice (1-5): ").strip())


def main():
    print("Welcome to the Interactive Recipe Microservice A CLIENT!")

    while True:
        json_request = {}
        print("Let's get your recipe.")
        num_ingredients = int(input("How many ingredients would you like to enter? ").strip())
        ingredients_array = get_user_ingredients(num_ingredients)
        json_request["ingredients"] = ingredients_array

        while True:
            user_choice = get_user_choice()

            if user_choice == 1 or user_choice == 3:
                scale_factor = float(input("\nHow many servings: ").strip())
                json_request["serving_size"] = scale_factor

            if user_choice == 2 or user_choice == 3:
                print("Please type 'm' for conversion to metric or 'c' for conversion to customary.")

                while True:
                    system_choice = input("System (m or c): ").strip().lower()
                    if system_choice == 'm':
                        json_request["conversion_system"] = "metric"
                        break
                    elif system_choice == 'c':
                        json_request["conversion_system"] = "customary"
                        break
                    else:
                        print("Invalid input. Try again!")

            if user_choice in [1,2,3]:
                print((send_post_request(json_request)))

            elif user_choice == 4:
                break

            else:
                print("Thanks for using Microservice A Client")
                return


main()
