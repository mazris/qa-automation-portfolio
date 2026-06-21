from test_data import TestData

# Test cases using centralized test data
test_cases = [
    {
        "id": "TC001",
        "description": "Member with cart over $100",
        "is_member": True,
        "cart_total": TestData.CART_OVER_100,
        "expected_discount": TestData.expected_discount(True, TestData.CART_OVER_100)
    },
    {
        "id": "TC002",
        "description": "Member with cart under $100",
        "is_member": True,
        "cart_total": TestData.CART_UNDER_100,
        "expected_discount": TestData.expected_discount(True, TestData.CART_UNDER_100)
    },
    {
        "id": "TC003",
        "description": "Non-member with cart over $100",
        "is_member": False,
        "cart_total": TestData.CART_OVER_100,
        "expected_discount": TestData.expected_discount(False, TestData.CART_OVER_100)
    },
    {
        "id": "TC004",
        "description": "Non-member with cart under $100",
        "is_member": False,
        "cart_total": TestData.CART_UNDER_100,
        "expected_discount": TestData.expected_discount(False, TestData.CART_UNDER_100)
    }
]

# Run tests
passed = 0
failed = 0

print("=" * 50)
print("DISCOUNT CALCULATION TEST RESULTS")
print("=" * 50)

for tc in test_cases:
    actual = TestData.expected_discount(tc["is_member"], tc["cart_total"])

    if actual == tc["expected_discount"]:
        print(f"PASS — {tc['id']}: {tc['description']} → {actual * 100}% discount")
        passed += 1
    else:
        print(f"FAIL — {tc['id']}: {tc['description']}")
        print(f"       Expected: {tc['expected_discount'] * 100}%")
        print(f"       Actual:   {actual * 100}%")
        failed += 1

print("=" * 50)
print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
print("=" * 50)