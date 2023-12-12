-- setting up db
CREATE DATABASE IF NOT EXISTS pas;
USE pas;

-- setting up tables
-- users
CREATE TABLE IF NOT EXISTS users (
  id VARCHAR(256) PRIMARY KEY, 
  username VARCHAR(256) UNIQUE NOT NULL, 
  email VARCHAR(256) UNIQUE NOT NULL, 
  _password VARCHAR(256) NOT NULL, 
  ip VARCHAR(256)
);

-- logins
CREATE TABLE IF NOT EXISTS logins (
  loginId VARCHAR(256) PRIMARY KEY,
  token VARCHAR(512), 
  userId VARCHAR(256) NOT NULL,
  date DATE NOT NULL,
  ip VARCHAR(256),
  success BOOLEAN NOT NULL DEFAULT false,
  FOREIGN KEY (userId) REFERENCES users(id)
);

-- passwords
CREATE TABLE IF NOT EXISTS passwords (
  id VARCHAR(256) PRIMARY KEY,
  title VARCHAR(256) NOT NULL,
  userId VARCHAR(256) NOT NULL,
  url VARCHAR(256) NOT NULL,
  username VARCHAR(256),
  email VARCHAR(256),
  password VARCHAR(256) NOT NULL,
  FOREIGN KEY (userId) REFERENCES users(id)
);