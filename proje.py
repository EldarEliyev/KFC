#Menyunu temsile etmek ucun luget yaradin.Her bir acar elementin adidir ve deyer onun qiymetidir.:
menu = {
    "Chicken": 10,
    "Burger": 5,
    "Fries": 3,
    "Soda": 2,
    "Ice Cream": 4,
    "Coffee": 2,
    "Tea": 2,
    "Water": 7,
    "Salad": 6,
    "Pasta": 8,
    "Pizza": 10,
    "Sandwich": 5,
    "Soup": 4,
    "Steak": 12,
    "Fish": 9

}
#Her bir menu elementini cap edin:
for item, price in menu.items():
    print(item, price)

#Indiki qiymetler uzerinde endirim hesablayan bir funksiya yaradin:
def calculate_discounted_price(menu, discount_rate):
    discounted_menu = {}
    for item, price in menu.items():
        discounted_menu[item] = price - (price * discount_rate / 100)
    return discounted_menu

#Indiki qiymetler uzerinde 10% endirim hesablayin:
discount = 10
discounted_menu = calculate_discounted_price(menu, discount)
print(discounted_menu)

#Menyu ve kombinlerden istifade ederek sifarisin minimum qiymetini hesablayin.
#Sifarisin minimum qiymetini hesablayan bir funksiya yaradin:
def calculate_minimum_order(menu, *items):
    total_price = 0
    for item in items:
        total_price += menu[item]
    return total_price


order = ["Chicken", "Burger", "Fries", "Soda"]
minimum_order = calculate_minimum_order(menu, *order)
print(minimum_order)

discounted_order = calculate_minimum_order(discounted_menu, *order)
print(discounted_order)



def get_remaining_items(menu, *items):
    remaining_items = []
    for item in items:
        if item not in menu:
            remaining_items.append(item)
    return remaining_items

print(get_remaining_items(menu, *order))


print("Total order price: ", discounted_order)