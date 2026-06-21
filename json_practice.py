import json

# Mock API response from your POS app — a product lookup
api_response = '''
{
    "status": "success",
    "product": {
        "id": "P001",
        "name": "Coffee Mug",
        "price": 24.99,
        "barcode": "00123",
        "in_stock": true,
        "category": "Kitchenware"
    }
}
'''

# Parse the JSON string into a Python dictionary
data = json.loads(api_response)

# Extract values
print(data["status"])
print(data["product"]["name"])
print(data["product"]["price"])
print(data["product"]["in_stock"])

# Mock cart response with multiple items
cart_response = '''
{
    "cart_id": "C-8821",
    "customer": "Sarah Johnson",
    "items": [
        {"name": "Coffee Mug", "price": 24.99, "quantity": 1},
        {"name": "Water Bottle", "price": 19.99, "quantity": 2},
        {"name": "Notebook", "price": 12.99, "quantity": 1}
    ],
    "discount": 5.00,
    "total": 72.96
}
'''

data = json.loads(cart_response)

print(f"Customer: {data['customer']}")
print(f"Cart ID: {data['cart_id']}")
print(f"Number of items: {len(data['items'])}")

for item in data["items"]:
    line_total = item["price"] * item["quantity"]
    print(f"{item['name']} x{item['quantity']} = ${line_total:.2f}")

print(f"Total: ${data['total']}")


import json

api_response = '''
{
    "status": "success",
    "discount_applied": 5.00,
    "final_total": 33.23
}
'''

data = json.loads(api_response)

expected_total = 33.23
actual_total = data["final_total"]

if actual_total == expected_total:
    print(f"PASS — total is correct: ${actual_total}")
else:
    print(f"FAIL — expected ${expected_total} but got ${actual_total}")