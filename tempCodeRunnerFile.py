# Welcome
print("Good Evening Sir.\n Welcome to our Restaurant. \nHere is our menu. \nWhat would you like to eat here?")

# Menu
menu = {
    "Pizza"     : 300,
    "Burger"    : 120,
    "Noodles"   : 150,
    "Dimsums"   : 90,
    "Cold Drink": 100,
    "Veg Kebabs": 220
}

print("Pizza      : 300\nBurger     : 120\nNoodles    : 150\nDimsums    : 90\nCold Drink : 100\nVeg Kebabs : 220")

item_1 = input("What would you like Sir? :")

sub_total = 0

if item_1 in menu:
    sub_total += menu[item_1]
    print(f"{item_1} is added to your order.")

else:
    print(f"{item_1} is not available with us.")

another_item = input("Would you like anything else sir? (Yes/No): ")

if another_item == "Yes":
    item_2 = input("What else would you like Sir?")
    if item_2 in menu:
        sub_total += menu[item_2]
        print(f"{item_2} has been added in you order.")

    else:
        print(f"{item_2} is not available with us.")


print(f"Thank You for ordering from us.\nYour food will arrive in few minutes.\nYour sub_total is {sub_total}")
