CREATE DATABASE pet_adoption_db;
USE pet_adoption_db;

CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pet_name VARCHAR(50) NOT NULL,
    species VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    status VARCHAR(20) DEFAULT 'available'
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255)
);

CREATE TABLE adoptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT NOT NULL,
    user_id INT NOT NULL,
    adoption_date DATE DEFAULT (CURRENT_DATE),
    return_status VARCHAR(20) DEFAULT 'not returned',
    FOREIGN KEY (pet_id) REFERENCES pets(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE returns (
    id INT AUTO_INCREMENT PRIMARY KEY,
    adoption_id INT NOT NULL,
    return_date DATE DEFAULT (CURRENT_DATE),
    reason VARCHAR(255),
    FOREIGN KEY (adoption_id) REFERENCES adoptions(id) ON DELETE CASCADE
);

INSERT INTO pets (pet_name, species, gender, age, status) VALUES
('Bella', 'Dog', 'Female', 2, 'available'),
('Milo', 'Cat', 'Male', 1, 'available'),
('Luna', 'Dog', 'Female', 4, 'adopted'),
('Charlie', 'Rabbit', 'Male', 3, 'available'),
('Coco', 'Parrot', 'Female', 5, 'available'),
('Rocky', 'Dog', 'Male', 2, 'adopted'),
('Daisy', 'Cat', 'Female', 1, 'available'),
('Max', 'Dog', 'Male', 6, 'available'),
('Nala', 'Cat', 'Female', 2, 'adopted'),
('Oscar', 'Hamster', 'Male', 1, 'available'),
('Ruby', 'Dog', 'Female', 3, 'available'),
('Buddy', 'Dog', 'Male', 5, 'available'),
('Zoe', 'Rabbit', 'Female', 4, 'adopted'),
('Simba', 'Cat', 'Male', 2, 'available'),
('Lola', 'Parrot', 'Female', 6, 'available'),
('Jack', 'Dog', 'Male', 1, 'available'),
('Chloe', 'Cat', 'Female', 3, 'available'),
('Leo', 'Dog', 'Male', 4, 'adopted'),
('Penny', 'Guinea Pig', 'Female', 2, 'available'),
('Shadow', 'Dog', 'Male', 7, 'available');

INSERT INTO users (user_name, email, phone, address) VALUES
('Ana Singh', 'ana@example.com', '9876543210', '12 Green Street, Delhi'),
('Birda', 'birda@example.com', '9988776655', '45 Rose Avenue, Mumbai'),
('Lily Fernandez', 'lily@example.com', '9123456789', '22 Sunset Blvd, Bangalore'),
('Ravi Patel', 'ravi@example.com', '9012345678', '9 MG Road, Pune'),
('Sophia Dsouza', 'sophia@example.com', '9345678123', '77 Lake View, Chennai');

INSERT INTO adoptions (pet_id, user_id, adoption_date, return_status) VALUES
(3, 1, '2025-09-10', 'not returned'),  
(6, 2, '2025-09-18', 'returned'),     
(9, 3, '2025-10-01', 'not returned'), 
(2, 4, '2025-10-05', 'not returned'),  
(1, 5, '2025-10-08', 'not returned');  

INSERT INTO returns (adoption_id, return_date, reason) VALUES
(2, '2025-10-10', 'Pet was not adjusting well');

-- Stored procedure to mark a pet returned

DELIMITER $$
CREATE PROCEDURE mark_pet_returned(IN adoptionId INT)
BEGIN
    DECLARE petId INT;

    -- fetch the pet_id from the adoptions table for the given adoption record
    SELECT pet_id INTO petId FROM adoptions WHERE id = adoptionId;

    -- Mark the pet as available again
    UPDATE pets SET status = 'available' WHERE id = petId;

    -- Update adoption record
    UPDATE adoptions SET return_status = 'returned' WHERE id = adoptionId;
END$$
DELIMITER ;

SELECT * FROM pets;
SELECT * FROM returns;
SELECT * FROM users;
SELECT * FROM adoptions;
