import os
import bcrypt

def hashPassword(password):
  password = password.encode()
  return (bcrypt.hashpw(password, bcrypt.gensalt(8))).decode()

def checkPassword(password, hash):
  return bcrypt.checkpw(password.encode(), hash.encode())