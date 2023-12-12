from lib.api import handleError, handleSuccess
from lib.hasher import hashPassword
from lib.session import verifySession
from db.user import User

user = User()

def createUserRoute(body):
	try:
		if not 'ip' in body:
			raise Exception("Missing ip parameter in body")
		if not 'email' in body:
			raise Exception("Missing email parameter in body")
		if not 'username' in body:
			raise Exception("Missing username parameter in body")
		if not 'password' in body:
			raise Exception("Missing password parameter in body")
		
		user.createUser(body['username'], body['email'], hashPassword(body['password']), body['ip'])
		session = user.loginUser(body['ip'], body['username'], body['password'])

		return handleSuccess("Successfully created user", session)
	except Exception as err:
		return handleError("Could not create user", err)
	
def loginRoute(body):
	try:
		if not 'ip' in body:
			raise Exception("Missing parameter ip in body")
		if not 'username' in body:
			raise Exception("Missing parameter username in body")
		if not 'password' in body:
			raise Exception("Missing parameter password in body")
		
		session = user.loginUser(body['ip'], body['username'], body['password'])

		return handleSuccess("Successfully logged user", session)
	except Exception as err:
		return handleError("There was an error while trying to login user", err)
	
def verifySessionRoute(session):
	try:
		if not session:
			raise Exception("Missing session parameter")

		valid, obj = verifySession(session)

		if valid:
			return handleSuccess("Session verified")
		else:
			raise Exception("not-verified")
	except Exception as err:
		return handleError("Could not verify session")