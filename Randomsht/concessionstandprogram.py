menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print('-------MENU-------')
for key, value in menu.items():
    print(f'{key:10}: ${value:.2f}')

while True:
        food = input("Select your item (q or quit): ").lower()
        if food == 'q':
            print("Thank you for your order !")
            break
        elif menu.get(food) is not None:
            cart.append(food)
            total += menu[food]
        else:
            print(f'{food} is not in the menu')
            continue
print("----- YOUR ORDER -----")
for food in cart:
    print(f'{food:5}: ${menu.get(food):.2f}')

print(f"Total number of Items: {len(cart)}")
print(f'Total cost: ${total:.2f}')
