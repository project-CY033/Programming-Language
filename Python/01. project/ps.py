# Smart Campus Navigation System

# Import necessary libraries
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for users and their locations
users = {
    'user1': {'password': 'pass1', 'location': 'Building A'},
    'user2': {'password': 'pass2', 'location': 'Building B'}
}

# User authentication
def authenticate_user(username, password):
    if username in users and users[username]['password'] == password:
        return True
    else:
        return False

# Register new user
def register_user(username, password):
    if username not in users:
        users[username] = {'password': password, 'location': None}
        return True
    else:
        return False

# Real-time location tracking
def track_location(user_id, new_location):
    if user_id in users:
        users[user_id]['location'] = new_location
        return True
    else:
        return False

# Mapping API integration
def display_campus_map():
    # Dummy function for now
    return "Campus Map"

# Flask routes for API endpoints

# Flask route for the root URL
@app.route('/')
def index():
    return 'Welcome to the Smart Campus Navigation System'

# User login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if authenticate_user(username, password):
        return 'Login successful'
    else:
        return 'Login failed'

# User signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if register_user(username, password):
        return 'Signup successful'
    else:
        return 'Username already exists'

# Get user location
@app.route('/location/<user_id>', methods=['GET'])
def get_location(user_id):
    if user_id in users:
        return jsonify({'location': users[user_id]['location']})
    else:
        return 'User not found', 404

# Update user location
@app.route('/update_location/<user_id>', methods=['POST'])
def update_location(user_id):
    data = request.get_json()
    new_location = data['location']
    if track_location(user_id, new_location):
        return 'Location updated successfully'
    else:
        return 'User not found', 404

# Get campus map
@app.route('/map', methods=['GET'])
def get_campus_map():
    return display_campus_map()

if __name__ == '__main__':
    app.run(debug=True)
