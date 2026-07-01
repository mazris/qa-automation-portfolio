import requests

class APIClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_user(self,user_id):
        response = requests.get(f"{self.BASE_URL}/users/{user_id}")
        return response

    def get_all_users(self):
        response = requests.get(f"{self.BASE_URL}/users")
        return response

    def create_user(self,payload):
        response = requests.post(
            f"{self.BASE_URL}/users",
            json=payload
        )
        return response

    def update_user(self,user_id,payload):
        response = requests.put(
            f"{self.BASE_URL}/users/{user_id}",
            json=payload
        )
        return response

    def delete_user(self,user_id):
        response = requests.delete(
            f"{self.BASE_URL}/users/{user_id}"
        )
        return response

class POSAPIClient:
    """Client for the local mock POS backend — connected to real MySQL DB"""
    BASE_URL = "http://127.0.0.1:5050"

    def get_customer(self, customer_id):
        response = requests.get(f"{self.BASE_URL}/customers/{customer_id}")
        return response

    def apply_promo(self, promo_code, cart_total):
        response = requests.post(
            f"{self.BASE_URL}/apply-promo",
            json={"promo_code": promo_code, "cart_total": cart_total}
        )
        return response

    def update_loyalty_points(self, customer_id, points):
        response = requests.put(
            f"{self.BASE_URL}/customers/{customer_id}/loyalty-points",
            json={"points": points}
        )
        return response