from flask import Flask, jsonify, request
from db_utils import get_all_pets, insert_new_pet, adopt_pet, return_pet

app = Flask(__name__)

# GET endpoint1: fetch pets 
@app.route('/pets', methods=['GET'])
def api_get_pets():
    pets = get_all_pets()
    return jsonify(pets)

# POST endpoint: add a new pet
@app.route('/pets', methods=['POST'])
def api_add_pet():
    data = request.json
    insert_new_pet(data)
    return jsonify({"message": "New pet added successfully!"})

#POST endpoint 3: adopt a pet
@app.route('/adopt', methods=['POST'])
def api_adopt_pet():
    data = request.json
    pet_id = data['pet_id']
    user_id = data['user_id']
    adopt_pet(pet_id, user_id)
    return jsonify({"message": f"Pet {pet_id} adopted by user {user_id}"})

#POST endpoint 4: return a pet
@app.route('/return', methods=['POST'])
def api_return_pet():
    data = request.json
    adoption_id = data['adoption_id']
    reason = data['reason']
    return_pet(adoption_id, reason)
    return jsonify({"message": f"Pet with adoption ID {adoption_id} marked as returned"})

if __name__ == '__main__':
    app.run(debug=True)
