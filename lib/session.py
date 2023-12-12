import jwt
import os
from datetime import datetime, timezone, timedelta

def createSession(userId):
  session = jwt.encode({
		"id": userId,
		"exp": datetime.now(tz=timezone.utc) + timedelta(days=3)
	}, os.getenv('SECRET'), algorithm="HS256")
  
  return f"{session}"

def verifySession(session):
  try:
    obj = jwt.decode(session.encode(), os.getenv('SECRET'), algorithms=["HS256"])
    return True, obj
  except Exception as err:
    print(err)
    return False, err