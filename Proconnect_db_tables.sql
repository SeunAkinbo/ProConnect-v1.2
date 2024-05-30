USE ProConnectDB;
CREATE TABLE IF NOT EXISTS Users (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lasttname VARCHAR(50) NOT NULL,
    profile_picture VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Education (
    user_id VARCHAR(255) NOT NULL,
    education_level VARCHAR(255) NOT NULL,
    field_of_study VARCHAR(255) NOT NULL,
    name_of_institution VARCHAR(255) NOT NULL,
    year_of_graduation DATE NOT NULL,
    country_of_study VARCHAR(255) NOT NULL,
    degree VARCHAR(255) NOT NULL,
    certification VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS error_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    object_affected VARCHAR(255) NOT NULL,
    level VARCHAR(255) NOT NULL,
    message VARCHAR(255) NOT NULL,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Profile (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id VARCHAR(128) NOT NULL,
    category_id INT NOT NULL,
    description TEXT,
    address VARCHAR(255),
    payment VARCHAR(128),
    availability VARCHAR(128),
    linkedin VARCHAR(255),
    github VARCHAR(255),
    reviews TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (category_id) REFERENCES Category(id)
);

CREATE TABLE Skills (
    id INT PRIMARY KEY AUTO_INCREMENT,
    profile_id INT NOT NULL,
    duration VARCHAR(128) NOT NULL,
    skill_name VARCHAR(128) NOT NULL,
    FOREIGN KEY (profile_id) REFERENCES Profile(id)
);

CREATE TABLE Category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(128) UNIQUE NOT NULL
);




