from mysql.connector import connect
from termcolor import colored

db = connect(host="localhost", user="root", passwd="root")
c = db.cursor()

def setup():
  with open("db/setup.sql", 'r') as f:
    final = ""
    for line in f.readlines():
      if len(line) != 0 and not line.startswith("--"):
        if ";" in line:
          final += line.strip()[:-1]
        else:
          final += line.strip()

      if ";" in line:
        c.execute(final)
        final = ""

  print(colored("✅ Successfully setup DB", "green"))
  return c

setup()