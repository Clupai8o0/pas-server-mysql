from lib.api import handleError, handleSuccess
from lib.hasher import hashPassword
from lib.session import verifySession
from db.password import Password

password = Password()

def createPasswordRoute(body, session):
	try:
		if not session:
			raise Exception("Missing auth header authorization")

		# checking if parameters are given
		if not 'title' in body:
			raise Exception("Missing parameter title in body")
		if not 'username' in body:
			raise Exception("Missing parameter username in body")
		if not 'email' in body:
			raise Exception("Missing parameter email in body")
		if not 'password' in body:
			raise Exception("Missing parameter password in body")
		if not 'url' in body:
			raise Exception("Missing parameter url in body")
		
		valid, obj = verifySession(session)

		if valid:
			password.createPassword(
				userId=obj['id'], 
				title=body['title'], 
				url=body['url'], 
				username=body['username'], 
				email=body['email'], 
				password=body['password']
			)
		else:
			raise Exception("expired")

		return handleSuccess("Successfully created password")
	except Exception as err:
		return handleError("There was an error while trying to create password", err)

def getPasswordsRoute(session):
	try:
		if not session:
			raise Exception("Missing session parameter")

		valid, obj = verifySession(session)

		if valid:
			return handleSuccess("Successfully GET passwords of user", password.getPasswords(obj['id']))
		else: 
			raise Exception("expired")
	except Exception as err:
		return handleError( "There was an error while trying to get passwords", err)

def deletePasswordRoute(session, passwordId):
	try:
		if not session:
			raise Exception("Missing session parameter")
		if not passwordId:
			raise Exception("Missing password id parameter")

		valid, obj = verifySession(session)

		if valid:
			return handleSuccess("Successfully delete password", password.deletePassword(obj, passwordId))
		else:
			raise Exception("expired")
	except Exception as err:
		return handleError("There was an error while trying to get passwords", err)

def updatePasswordRoute(session, body):
	try:
		passwordId = body['id']

		d = ""
		if 'title' in body:
			d += f" title = '{body['title']}' "
		if 'username' in body:
			d += f" username = '{body['username']}' "
		if 'password' in body:
			d += f" password = '{body['password']}' "
		if 'url' in body:
			d += f" url = '{body['url']}' "
		if 'email' in body:
			d += f" email = '{body['email']}' "
		
		if not session:
			raise Exception("Missing auth header session")
		if not passwordId:
			raise Exception("Missing parameter password id")

		valid, obj = verifySession(session)

		if valid:
			return handleSuccess("Successfully updated password", password.updatePassword(obj, passwordId, d))
		else:
			raise Exception("expired")
	except Exception as err:
		return handleError("There was an error while trying to update passwords", err)

def searchPasswordsRoute(session, query):
	try:
		if not session:
			raise Exception("No session provided")
		if not query:
			raise Exception("No search query provided")
		
		valid, obj = verifySession(session)

		if valid:
			return handleSuccess("Successfully searched password", password.searchPassword(obj, query))
		else:
			raise Exception("expired")
	except Exception as err:
		return handleError("There was an error while trying to search passwords", err)