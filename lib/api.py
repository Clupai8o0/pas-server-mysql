from flask import jsonify
from termcolor import colored

def response(success, msg, data={}):
  return {
    "success": success,
    "msg": msg,
    "data": data
  }

def handleSuccess(msg, data={}, status=200):
  print(colored(f"✅ {msg}", "green"))
  return jsonify(response(True, msg, data)), status

def handleError(msg, error, status=500):
  print(colored(f"❌ {msg}", "red"))
  print(error)
  return jsonify(response(False, msg, str(error))), status
