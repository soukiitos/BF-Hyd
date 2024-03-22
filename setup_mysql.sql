CREATE DATABASE BFHyd_db;
CREATE USER 'BFHyd'@'localhost' IDENTIFIED BY 'kiitos';
GRANT ALL PRIVILEGES ON `BFHyd_db`.*TO 'BFHyd'@'localhost';
GRANT SELECT ON `performance_schema`.*TO 'BFHyd'@'localhost';
FLUSH PRIVILEGES;
