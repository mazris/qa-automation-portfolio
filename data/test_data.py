class TestData:

    #Valid User
    STANDARD_USER = {
        "username": "standard_user",
        "password": "secret_sauce"
    }

    # Invalid users
    INVALID_USER = {
        "username": "standard_user",
        "password": "wrong_password"
    }

    LOCKED_USER = {
        "username": "locked_out_user",
        "password": "secret_sauce"
    }

    # Customer details for checkout
    CUSTOMER = {
        "first_name": "Sarah",
        "last_name": "Johnson",
        "postal_code": "10001"
    }

    # Expected text
    PRODUCTS_TITLE = "Products"
    LOGIN_ERROR = "Epic sadface: Username and password do not match any user in this service"
    LOCKED_ERROR = "Epic sadface: Sorry, this user has been locked out."
    ORDER_CONFIRMATION = "Thank you for your order!"
