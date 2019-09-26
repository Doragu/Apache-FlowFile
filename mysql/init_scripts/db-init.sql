CREATE TABLE payment (
    payment_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    customer_id SMALLINT UNSIGNED NOT NULL,
    staff_id TINYINT UNSIGNED NOT NULL,
    rental_id INT DEFAULT NULL,
    amount DECIMAL(5,2) NOT NULL,
    payment_date DATETIME NOT NULL,
    last_update DATETIME NOT NULL,
    PRIMARY KEY (payment_id));

CREATE TABLE paymentDate (
    paymentDate_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATE NOT NULL,
    PRIMARY KEY (paymentDate_id),
    UNIQUE KEY (payment_date));

CREATE TABLE aggregation (
    aggregation_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    aggregation_date DATETIME NOT NULL,
    aggregation_table VARCHAR(20) NOT NULL ,
    PRIMARY KEY (aggregation_id));

INSERT INTO aggregation (aggregation_date, aggregation_table) VALUES (now(), 'payment');
