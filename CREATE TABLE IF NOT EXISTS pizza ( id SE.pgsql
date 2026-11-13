CREATE TABLE IF NOT EXISTS pizza ( id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL,
description VARCHAR(200) NOT NULL, price FLOAT NOT NULL);
INSERT INTO pizza (name, description, price)
VALUES ('Margherita', ' Tomato sauce, mozzarella cheese, fresh basil', 25.0);
SELECT * FROM pizza;