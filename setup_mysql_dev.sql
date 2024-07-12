<<<<<<< HEAD
-- Prepares a MySQL Development Server for the project
-- Database hbnb_dev_db
-- User hbnb_dev with password hbnb_dev_pwd
-- Grants all privileges for hbnb_dev on hbnb_dev_db
-- Grants SELECT privileges for hbnb_dev on performance schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
=======
-- create database hbnb_dev_db if not exists
-- create user hbnb_dev with pwd hbnb_dev_pwd
-- grant hbnb_dev select on performance_schema
-- grant all privileges on hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
>>>>>>> 282a6eac2c664e4fe68b5d2974534cd19c4d3e4e
