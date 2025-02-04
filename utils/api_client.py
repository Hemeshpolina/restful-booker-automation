import requests

class RestfulBookerClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def authenticate(self, username, password):
        response = requests.post(f"{self.base_url}/auth", json={"username": username, "password": password})
        response.raise_for_status()
        self.token = response.json()['token']

    def create_booking(self, booking_data):
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        response = requests.post(f"{self.base_url}/booking", json=booking_data, headers=headers)
        response.raise_for_status()
        return response.json()

    def update_booking(self, booking_id, booking_data):
        headers = {"Content-Type": "application/json", "Cookie": f"token={self.token}"}
        response = requests.put(f"{self.base_url}/booking/{booking_id}", json=booking_data, headers=headers)
        response.raise_for_status()
        return response.json()

    def delete_booking(self, booking_id):
        headers = {"Content-Type": "application/json", "Cookie": f"token={self.token}"}
        response = requests.delete(f"{self.base_url}/booking/{booking_id}", headers=headers)
        response.raise_for_status()
        return response.status_code