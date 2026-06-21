# Promo Code Validator
# Tests promo code behavior based on decision table logic

from datetime import date

# Test data — each case is one row from your decision table
test_cases = [
    {
        "id": "TC001",
        "description": "Valid promo code applied to non-empty cart",
        "promo_code": "SAVE5",
        "cart_total": 44.98,
        "cart_empty": False,
        "code_expired": False,
        "expected_discount": 5
    },
    {
        "id": "TC002",
        "description": "Expired promo code rejected",
        "promo_code": "OLD10",
        "cart_total": 44.98,
        "cart_empty": False,
        "code_expired": True,
        "expected_discount": 0
    },
    {
        "id": "TC003",
        "description": "Promo code rejected on empty cart",
        "promo_code": "SAVE5",
        "cart_total": 0,
        "cart_empty": True,
        "code_expired": False,
        "expected_discount": 0
    },
    {
        "id": "TC004",
        "description": "Case insensitive — lowercase code accepted",
        "promo_code": "save5",
        "cart_total": 44.98,
        "cart_empty": False,
        "code_expired": False,
        "expected_discount": 5
    },

{
        "id": "TC005",
        "description": "valid promo code rejected because expired",
        "promo_code": "SAVE5",
        "cart_total": 44.98,
        "cart_empty": False,
        "code_expired": True,
        "expected_discount": 0
    }
]

# Valid promo codes in the system
valid_codes = ["SAVE5", "PROMO10", "DEAL15"]

def validate_promo_code(promo_code, cart_total, cart_empty, code_expired):
    if cart_empty:
        return 0
    if code_expired:
        return 0
    if promo_code.upper() not in valid_codes:
        return 0
    return 5

# Run test cases
passed = 0
failed = 0

print("=" * 50)
print("PROMO CODE VALIDATION TEST RESULTS")
print("=" * 50)

for tc in test_cases:
    actual_discount = validate_promo_code(
        tc["promo_code"],
        tc["cart_total"],
        tc["cart_empty"],
        tc["code_expired"]
    )

    if actual_discount == tc["expected_discount"]:
        print(f"PASS — {tc['id']}: {tc['description']}")
        passed += 1
    else:
        print(f"FAIL — {tc['id']}: {tc['description']}")
        print(f"       Expected discount: {tc['expected_discount']}%")
        print(f"       Actual discount:   {actual_discount}%")
        failed += 1

print("=" * 50)
print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
print("=" * 50)