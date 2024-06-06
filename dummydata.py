import requests
import json
from faker import Faker

# Initialize the Faker instance
fake = Faker()

# Function to generate a random user dictionary
def generate_random_user():
    fakename = fake.name()
    fakeemail = fakename.replace(" ","").lower() + "@trimetracker.com"
    return {
        "name": fakename,
        "email": fakeemail,
        "password": fake.password(length=12),
        "age": fake.random_int(min=18, max=80)
    }

# URL of the FastAPI endpoint
url = "http://localhost:8000/users/"  # Replace with your actual URL if different

# Loop to create 30 random users
for _ in range(30):
    user_data = generate_random_user()
    response = requests.post(url, data=json.dumps(user_data), headers={"Content-Type": "application/json"})
    if response.status_code == 201:
        print(f"User created successfully: {response.json()}")
    else:
        print(f"Failed to create user: {response.status_code}, {response.text}")
