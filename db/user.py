from datetime import datetime
from uuid import uuid4 as generateKey
from mysql.connector import errorcode

from lib.hasher import checkPassword
from lib.session import createSession
from db.setup import c, db

class User():
	def createUser(self, username, email, password, ip):
		try:
			c.execute(f"INSERT INTO users (id, username, email, _password, ip) VALUES ('{generateKey()}', '{username}', '{email}', '{password}', '{ip}')")
			db.commit()
		except Exception as err:
			if err.errno == errorcode.ER_DUP_ENTRY:
				raise Exception("exists")
			raise Exception(err)
		
	def loginUser(self, ip, username, password):
		c.execute(f"SELECT id, email, _password FROM users WHERE username='{username}'")
		users = c.fetchall()
		
		if len(users) > 0:
			user = users[0]

			if checkPassword(password, user[2]):
				token = createSession(user[0])
				c.execute(f"INSERT INTO logins (loginId, token, userId, date, ip, success) VALUES ('{generateKey()}', '{token}', '{user[0]}', '{str(datetime.now())}', '{ip}', {True})")
				db.commit()

				return token
			else:
				c.execute(f"INSERT INTO logins (loginId, userId, date, ip, success) VALUES ('{generateKey()}', '{user[0]}', '{str(datetime.now())}', '{ip}', {False})")
				db.commit()
				raise Exception("wrong-credentials")
		else:
			raise Exception("wrong-credentials")

