from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Rishitha", "email": "rishitha@gmail.com"},
    {"id": 2, "name": "Priya", "email": "priya@gmail.com"}
]

# GET
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# POST
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

# PUT route
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_data = request.json

    for user in users:
        if user['id'] == user_id:
            user.update(updated_data)
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404

# DELETE route
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"}), 200

    return jsonify({"message": "User not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)