from uuid import uuid4 as generateKey

from db.setup import c, db

class Password():
  def createPassword(self, userId, title, url, username, email, password):
    c.execute(f"INSERT INTO passwords (id, title, userId, url, username, email, password) VALUES ('{generateKey()}', '{title}', '{userId}', '{url}', '{username}', '{email}', '{password}')")
    db.commit()

  def getPasswords(self, userId):
    c.execute(f"SELECT * FROM passwords WHERE userId = '{userId}'")
    data = c.fetchall()
    return data

  def updatePassword(self, obj, passwordId, update):
    c.execute(f"SELECT * FROM passwords WHERE userId = '{obj['id']}'")
    data = c.fetchall()

    if len(data) > 0:
      c.execute(f"UPDATE passwords SET {update} WHERE id = '{passwordId}'")
      db.commit()
    else:
      raise Exception("Password does not exist")
    
  def searchPassword(self, obj, query):
    passwords_list = []
    for word in query:
      c.execute(f"SELECT * FROM passwords (id, title, userId, url, username, email, password) WHERE (title LIKE '%{word}%' OR username LIKE '%{word}%' OR email LIKE '%{word}%' OR url LIKE '%{word}%') AND userId = '{obj['id']}'")
      passwords_list.extend(c.fetchall())
    
    data = []
    for p in passwords_list:
      password = {
        'id': p[0],
        'title': p[1],
        'userId': p[2],
        'url': p[3],
        'username': p[4],
        'email': p[5],
        'password': p[6],
      }
      data.append(password)
      
    return data

  def deletePassword(self, obj, passwordId):
    c.execute(f"SELECT id FROM passwords WHERE userId = '{obj['id']}' AND id = '{passwordId}'")
    data = c.fetchall()

    if len(data) > 0: # it exists
      c.execute(f"DELETE FROM passwords WHERE id = '{passwordId}'")
      db.commit()
    else:
      raise Exception("Password does not exist")