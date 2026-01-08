# create how a user or another app would use the api
# Uses the requests library to call the API endpoints (GET, POST)
# Demonstrates the API in action

import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def get_all_pets():
    res = requests.get(f"{BASE_URL}/pets")
    return res.json()

def add_new_pet():
    pet = {
        "pet_name": input("Enter pet name: "),
        "species": input("Enter species: "),
        "gender": input("Enter gender: "),
        "age": int(input("Enter age: ")),
        "status": "available"
    }
    res = requests.post(f"{BASE_URL}/pets", json=pet)
    print(res.json())

def adopt_pet():
    pet_id = int(input("Enter the pet ID: "))
    user_id = int(input("Enter user ID: "))
    res = requests.post(f"{BASE_URL}/adopt", json={"pet_id": pet_id, "user_id": user_id})
    print(res.json())

def return_pet():
    adoption_id = int(input("Enter adoption ID: "))
    reason = input("Your reason for returning the pet: ")
    res = requests.post(f"{BASE_URL}/return", json={"adoption_id": adoption_id, "reason": reason})
    print(res.json())

def view_available_pets():
    res = requests.get(f"{BASE_URL}/available")
    pets = res.json()
    for p in pets:
        print(f"ID: {p[0]}, Name: {p[1]}, Species: {p[2]}, Gender: {p[3]}, Age: {p[4]}, Status: {p[5]}")

def run():
    print("----Welcome to the Pet Adoption API----")
    while True:
        print("\n1. View all pets")
        print("2. Add new pet")
        print("3. Adopt pet")
        print("4. Return pet")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            pets = get_all_pets()
            for p in pets:
                print(f"ID: {p[0]}, Name: {p[1]}, Species: {p[2]}, Gender: {p[3]}, Age: {p[4]}, Status: {p[5]}")
        elif choice == "2":
            add_new_pet()
        elif choice == "3":
            adopt_pet()
        elif choice == "4":
            return_pet()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!Please enter a number from 1 to 5.")

if __name__ == '__main__':
    run()
