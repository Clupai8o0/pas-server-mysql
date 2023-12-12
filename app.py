# Imports
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv

# Local Imports
from db.setup import setup

# Routes
from routes.user import createUserRoute, loginRoute, verifySessionRoute
from routes.password import createPasswordRoute, deletePasswordRoute, getPasswordsRoute, searchPasswordsRoute, updatePasswordRoute

#* Initialization
load_dotenv()
app = Flask(__name__)
CORS()
setup()

#* Test Routes
@app.route("/")
def home():
	return "Hello World"
@app.route("/ping")
def ping():
	return "pong"

#* User Routes
# Create User
@app.route("/api/auth/create-user", methods=['POST'])
def create_user():
	return createUserRoute(request.json)

# Login
@app.route("/api/auth/login", methods=['POST'])
def login():
	return loginRoute(request.json)

# Verify Session
@app.route("/api/auth/verify-session", methods=['GET'])
def verify_session():
	return verifySessionRoute()

#* Password Routes
# Create password
@app.route("/api/app/create-password", methods=['POST'])
def create_password():
	return createPasswordRoute(request.json, request.headers.get('authorization').split(' ')[1])

# Get password
@app.route("/api/app/get-passwords", methods=['GET'])
def get_passwords():
	return getPasswordsRoute(request.headers.get('authorization').split(' ')[1])

# Delete password
@app.route("/api/app/delete-password", methods=['DELETE'])
def delete_password():
	return deletePasswordRoute(request.headers.get("authorization").split(' ')[1], request.args.get("id"))

# Update password
@app.route("/api/app/update-password", methods=['PUT'])
def update_password():
	return updatePasswordRoute(request.headers.get("authorization").split(' ')[1], request.json)

# Search password
@app.route("/api/app/search-passwords", methods=['GET'])
def search_passwords():
	return searchPasswordsRoute(request.headers.get('authorization').split(' ')[1], request.args.get('query').lower().split(" "))

