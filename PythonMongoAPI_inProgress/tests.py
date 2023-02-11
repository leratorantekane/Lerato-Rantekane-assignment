import unittest
import requests
 
class TestProfileFunctions(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:5003"

    def test_get_profile(self):
        url = f"{self.base_url}/profile?username=test_user"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"profile": {"username": "test_user", "password": "test_pass"}})

    def test_update_profile(self):
        url = f"{self.base_url}/profile?username=test_user"
        data = {"password": "new_pass"}
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"profile": {"username": "test_user", "password": "new_pass"}})
    
    def test_delete_profile(self):
        url = f"{self.base_url}/profile?username=test_user"
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Profile deleted"})
 

