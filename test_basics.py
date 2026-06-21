item_name = "Coffee Mug"
item_price = 24.99
quantity = 2
is_in_stock = True
barcode = "00123"

# Print them
print(item_name)
print(item_price * quantity)
print(is_in_stock)

# List — ordered collection
cart_items = ["Coffee Mug", "Water Bottle", "Notebook"]
print(cart_items[0])        # first item
print(len(cart_items))      # number of items

# Dictionary — key value pairs, like a JSON object
product = {
    "name": "Coffee Mug",
    "price": 24.99,
    "barcode": "00123",
    "in_stock": True
}
print(product["name"])
print(product["price"])

cart_total = 44.98
is_member = True
promo_code = "SAVE5"

if is_member and cart_total > 100:
    discount = 0.25
elif is_member and cart_total <= 100:
    discount = 0.10
elif not is_member and cart_total > 100:
    discount = 0.05
else:
    discount = 0

final_total = cart_total - (cart_total * discount)
print(f"Discount: {discount * 100}%")
print(f"Final total: ${final_total:.2f}")

cart_items = [
    {"name": "Coffee Mug", "price": 24.99},
    {"name": "Water Bottle", "price": 19.99},
    {"name": "Notebook", "price": 12.99}
]

total = 0
for item in cart_items:
    print(f"{item['name']}: ${item['price']}")
    total += item['price']

print(f"Cart total: ${total:.2f}")


def calculate_discount(is_member, cart_total):
    if is_member and cart_total > 100:
        return 0.25
    elif is_member and cart_total <= 100:
        return 0.10
    elif not is_member and cart_total > 100:
        return 0.05
    else:
        return 0

def apply_discount(cart_total, discount):
    return cart_total - (cart_total * discount)

# Now use them
total = 44.98
member = True
discount = calculate_discount(member, total)
final = apply_discount(total, discount)
print(f"Final total: ${final:.2f}")