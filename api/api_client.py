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

