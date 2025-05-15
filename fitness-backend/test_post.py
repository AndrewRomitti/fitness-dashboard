import requests

url = "http://localhost:5000/calories"
data = {
    "date": "2025-05-16",
    "calories": 2200,
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response JSON:", response.json())