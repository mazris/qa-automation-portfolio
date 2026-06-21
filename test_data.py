# TestData class — centralized test data for POS app tests

class TestData:

    # Valid products
    COFFEE_MUG = {
        "name": "Coffee Mug",
        "price": 24.99,
        "barcode": "00123"
    }

    WATER_BOTTLE = {
        "name": "Water Bottle",
        "price": 19.99,
        "barcode": "00456"
    }

    # Loyalty customers
    LOYALTY_CUSTOMER = {
        "name": "Sarah Johnson",
        "loyalty_id": "LY-8821",
        "points": 500,
        "discount": 5.00
    }

    NON_LOYALTY_CUSTOMER = {
        "name": "John Smith",
        "loyalty_id": None,
        "points": 0,
        "discount": 0
    }

    # Promo codes
    VALID_PROMO = "SAVE5"
    EXPIRED_PROMO = "OLD10"
    INVALID_PROMO = "FAKE99"

    # Cart totals for boundary testing
    CART_UNDER_100 = 44.98
    CART_OVER_100 = 149.99
    CART_EMPTY = 0
    CART_EXACTLY_100 = 100.00

    # Expected discounts
    @staticmethod
    def expected_discount(is_member, cart_total):
        if is_member and cart_total > 100:
            return 0.25
        elif is_member and cart_total <= 100:
            return 0.10
        elif not is_member and cart_total > 100:
            return 0.05
        else:
            return 0