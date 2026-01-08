# Purpose: 
This API is to digitally manage pet records for a shelter home using simple API requests.

# Scenario:
Imagine a small animal shelter home that rescues and cares for different kinds of pets — dogs, cats, rabbits, parrots, and more.
The shelter staff needs a simple way to manage information about all the pets in their care.

They want to easily:

- See which pets are currently available for adoption
- Add new pets when new animals arrive
- Adopt a pet
- Update or change adoption status when pets are adopted or returned

**This API helps the shelter staff do all of this in one place.**

# Steps to run the API:

1. Dependencies to install: 
    1. flask - app.py file runs on Flask
    2. mysql-connector-python - used in db_utils.py
    3. requests - used in client.py for API endpoints (GET, POST)

Run this in terminal to install the dependencies: **pip install flask mysql-connector-python requests**

2. In MySQL workbench run the pet_adoption_db.sql script

3. In config.py fill the details

4. Open a new terminal to run the Flask API and enter this: **python app.py**

5. In a new terminal enter this code to run the client.py file: **python client.py**
