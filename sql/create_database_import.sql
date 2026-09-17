

-- =========================================
-- TABLE : customers
-- =========================================

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL,
    contact_name VARCHAR(100),
    email VARCHAR(150),
    city VARCHAR(100),
    region VARCHAR(100),
    customer_type ENUM('Standard', 'Premium', 'Gold') DEFAULT 'Standard',
    created_at DATE NOT NULL
);


-- =========================================
-- TABLE : sales_reps
-- =========================================

CREATE TABLE sales_reps (
    sales_rep_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    region VARCHAR(100),
    hire_date DATE
);


-- =========================================
-- TABLE : categories
-- =========================================

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description TEXT
);


-- =========================================
-- TABLE : suppliers
-- =========================================

CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(150) NOT NULL,
    country VARCHAR(100),
    contact_email VARCHAR(150)
);


-- =========================================
-- TABLE : products
-- =========================================

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category_id INT NOT NULL,
    supplier_id INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    cost_price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    reorder_level INT DEFAULT 10,
    active BOOLEAN DEFAULT TRUE,

    FOREIGN KEY (category_id)
        REFERENCES categories(category_id),

    FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id)
);


-- =========================================
-- TABLE : orders
-- =========================================

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    sales_rep_id INT NOT NULL,
    order_date DATE NOT NULL,
    status ENUM(
        'Pending',
        'Confirmed',
        'Shipped',
        'Delivered',
        'Cancelled'
    ) DEFAULT 'Pending',

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (sales_rep_id)
        REFERENCES sales_reps(sales_rep_id)
);


-- =========================================
-- TABLE : order_items
-- =========================================

CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount_percent DECIMAL(5,2) DEFAULT 0,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);
------------------------------
USE sales_rag;

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE order_items;
TRUNCATE TABLE orders;
TRUNCATE TABLE products;
TRUNCATE TABLE suppliers;
TRUNCATE TABLE categories;
TRUNCATE TABLE sales_reps;
TRUNCATE TABLE customers;

SET FOREIGN_KEY_CHECKS = 1;


-- =========================================
-- CUSTOMERS
-- =========================================

INSERT INTO customers
(customer_id, company_name, contact_name, email, city, region, customer_type, created_at)
VALUES
(1, 'Brussels Finance', 'Jean Dupont', 'jean.dupont@brusselsfinance.be', 'Bruxelles', 'Bruxelles-Capitale', 'Gold', '2023-01-15'),
(2, 'ABC Consulting', 'Marie Lambert', 'marie.lambert@abc-consulting.be', 'Bruxelles', 'Bruxelles-Capitale', 'Premium', '2023-02-10'),
(3, 'Flanders Business', 'Pieter Janssens', 'pieter.janssens@flandersbusiness.be', 'Anvers', 'Flandre', 'Premium', '2023-03-05'),
(4, 'Startup Factory', 'Thomas Martin', 'thomas.martin@startupfactory.be', 'Bruxelles', 'Bruxelles-Capitale', 'Standard', '2023-04-12'),
(5, 'Construction Pro', 'Sophie Bernard', 'sophie.bernard@constructionpro.be', 'LiÃ¨ge', 'Wallonie', 'Gold', '2023-05-20'),
(6, 'Medical Group', 'Claire Dubois', 'claire.dubois@medicalgroup.be', 'Namur', 'Wallonie', 'Premium', '2023-06-18'),
(7, 'Tech Solutions SA', 'Marc Leroy', 'marc.leroy@techsolutions.be', 'Charleroi', 'Wallonie', 'Gold', '2023-07-01'),
(8, 'Education Belgium', 'Anne Moreau', 'anne.moreau@education.be', 'Mons', 'Wallonie', 'Standard', '2023-08-14'),
(9, 'LogiTrans Belgium', 'Luc Peeters', 'luc.peeters@logitrans.be', 'Anvers', 'Flandre', 'Standard', '2023-09-02'),
(10, 'Retail Plus', 'Nathalie Simon', 'nathalie.simon@retailplus.be', 'Gand', 'Flandre', 'Standard', '2023-10-11');


-- =========================================
-- SALES REPS
-- =========================================

INSERT INTO sales_reps
(sales_rep_id, first_name, last_name, email, region, hire_date)
VALUES
(1, 'Sophie', 'Martin', 'sophie.martin@sales-rag.be', 'Bruxelles', '2022-01-10'),
(2, 'Thomas', 'Dubois', 'thomas.dubois@sales-rag.be', 'Wallonie', '2022-03-15'),
(3, 'Julie', 'Leroy', 'julie.leroy@sales-rag.be', 'Flandre', '2022-06-01'),
(4, 'Marc', 'Janssens', 'marc.janssens@sales-rag.be', 'Bruxelles', '2023-02-20');


-- =========================================
-- CATEGORIES
-- =========================================

INSERT INTO categories
(category_id, category_name, description)
VALUES
(1, 'Informatique', 'Ordinateurs, Ã©crans et pÃ©riphÃ©riques informatiques'),
(2, 'Mobilier', 'Mobilier professionnel pour bureaux'),
(3, 'Bureautique', 'Imprimantes, scanners et fournitures de bureau'),
(4, 'TÃ©lÃ©phonie', 'TÃ©lÃ©phones et accessoires de communication'),
(5, 'RÃ©seau', 'Ã‰quipements rÃ©seau et connectivitÃ©');


-- =========================================
-- SUPPLIERS
-- =========================================

INSERT INTO suppliers
(supplier_id, supplier_name, country, contact_email)
VALUES
(1, 'Tech Distribution Belgium', 'Belgique', 'contact@techdistribution.be'),
(2, 'Office Supply Europe', 'Belgique', 'contact@officesupply.eu'),
(3, 'Business Furniture SA', 'Belgique', 'contact@businessfurniture.be'),
(4, 'Network Solutions Europe', 'Pays-Bas', 'sales@networksolutions.eu'),
(5, 'Mobile Systems Belgium', 'Belgique', 'contact@mobilesystems.be');


-- =========================================
-- PRODUCTS
-- =========================================

INSERT INTO products
(product_id, product_name, category_id, supplier_id,
 unit_price, cost_price, stock_quantity, reorder_level, active)
VALUES
(1, 'Laptop Pro 15', 1, 1, 950.00, 700.00, 25, 10, TRUE),
(2, 'Laptop Business 14', 1, 1, 720.00, 520.00, 30, 10, TRUE),
(3, 'Souris sans fil', 1, 1, 35.00, 18.00, 100, 20, TRUE),
(4, 'Clavier professionnel', 1, 1, 55.00, 30.00, 80, 20, TRUE),
(5, 'Ã‰cran 27 pouces', 1, 1, 220.00, 140.00, 40, 15, TRUE),
(6, 'Ã‰cran 24 pouces', 1, 1, 160.00, 100.00, 8, 18, TRUE),
(7, 'Casque professionnel', 1, 1, 85.00, 45.00, 60, 15, TRUE),
(8, 'Imprimante Laser Pro', 3, 2, 270.00, 180.00, 35, 10, TRUE),
(9, 'Scanner professionnel', 3, 2, 310.00, 210.00, 6, 14, TRUE),
(10, 'Bureau professionnel', 2, 3, 380.00, 240.00, 25, 10, TRUE),
(11, 'Chaise ergonomique', 2, 3, 190.00, 120.00, 45, 15, TRUE),
(12, 'TÃ©lÃ©phone Business', 4, 5, 145.00, 90.00, 50, 15, TRUE),
(13, 'Smartphone Pro', 4, 5, 650.00, 450.00, 35, 10, TRUE),
(14, 'Switch 24 ports', 5, 4, 180.00, 110.00, 40, 15, TRUE),
(15, 'Routeur Business', 5, 4, 240.00, 150.00, 30, 10, TRUE);


-- =========================================
-- ORDERS
-- =========================================

INSERT INTO orders
(order_id, customer_id, sales_rep_id, order_date, status)
VALUES
(1, 1, 1, '2024-01-10', 'Delivered'),
(2, 2, 1, '2024-01-15', 'Delivered'),
(3, 3, 1, '2024-01-20', 'Delivered'),
(4, 4, 1, '2024-02-05', 'Delivered'),
(5, 5, 1, '2024-02-12', 'Delivered'),
(6, 6, 1, '2024-02-20', 'Delivered'),
(7, 7, 1, '2024-03-01', 'Delivered'),
(8, 8, 1, '2024-03-10', 'Delivered'),
(9, 9, 1, '2024-03-15', 'Delivered'),
(10, 10, 1, '2024-03-20', 'Delivered'),

(11, 1, 1, '2024-04-05', 'Delivered'),
(12, 2, 1, '2024-04-12', 'Delivered'),
(13, 3, 1, '2024-04-20', 'Delivered'),
(14, 4, 1, '2024-05-01', 'Delivered'),
(15, 5, 1, '2024-05-10', 'Delivered'),
(16, 6, 1, '2024-05-15', 'Delivered'),
(17, 7, 1, '2024-05-20', 'Delivered'),
(18, 8, 1, '2024-06-01', 'Delivered'),
(19, 9, 1, '2024-06-10', 'Delivered'),
(20, 10, 1, '2024-06-15', 'Delivered'),

(21, 1, 2, '2024-07-01', 'Delivered'),
(22, 2, 2, '2024-07-10', 'Delivered'),
(23, 3, 2, '2024-07-15', 'Delivered'),
(24, 4, 2, '2024-08-01', 'Delivered'),
(25, 5, 2, '2024-08-10', 'Delivered'),
(26, 6, 2, '2024-08-15', 'Delivered'),
(27, 7, 2, '2024-09-01', 'Delivered'),
(28, 8, 2, '2024-09-10', 'Delivered'),
(29, 9, 2, '2024-09-15', 'Delivered'),
(30, 10, 2, '2024-10-01', 'Delivered'),

(31, 1, 3, '2024-10-10', 'Delivered'),
(32, 2, 3, '2024-10-15', 'Delivered'),
(33, 3, 3, '2024-11-01', 'Delivered'),
(34, 4, 3, '2024-11-10', 'Delivered'),
(35, 5, 3, '2024-11-15', 'Delivered'),
(36, 6, 3, '2024-12-01', 'Delivered'),

(37, 7, 4, '2024-12-05', 'Delivered'),
(38, 8, 4, '2024-12-10', 'Delivered'),
(39, 9, 4, '2024-12-15', 'Delivered'),

-- Commande volontairement annulÃ©e
(40, 10, 4, '2024-12-20', 'Cancelled');


-- =========================================
-- ORDER ITEMS
-- =========================================

INSERT INTO order_items
(order_item_id, order_id, product_id, quantity, unit_price, discount_percent)
VALUES

-- Brussels Finance
(1, 1, 1, 3, 950.00, 0),
(2, 1, 5, 5, 220.00, 0),
(3, 1, 3, 10, 35.00, 0),

(4, 11, 2, 4, 720.00, 0),
(5, 11, 7, 10, 85.00, 0),

(6, 21, 13, 4, 650.00, 0),
(7, 21, 4, 10, 55.00, 0),

(8, 31, 8, 5, 270.00, 0),


-- ABC Consulting
(9, 2, 1, 2, 950.00, 0),
(10, 2, 5, 6, 220.00, 0),

(11, 12, 2, 3, 720.00, 0),
(12, 12, 3, 10, 35.00, 0),

(13, 22, 10, 8, 380.00, 0),
(14, 22, 11, 8, 190.00, 0),

(15, 32, 13, 4, 650.00, 0),


-- Flanders Business
(16, 3, 1, 2, 950.00, 0),
(17, 3, 6, 5, 160.00, 0),

(18, 13, 5, 8, 220.00, 0),
(19, 13, 4, 10, 55.00, 0),

(20, 23, 14, 8, 180.00, 0),
(21, 23, 15, 5, 240.00, 0),

(22, 33, 8, 4, 270.00, 0),


-- Startup Factory
(23, 4, 2, 3, 720.00, 0),
(24, 4, 3, 8, 35.00, 0),

(25, 14, 5, 7, 220.00, 0),
(26, 14, 7, 8, 85.00, 0),

(27, 24, 10, 5, 380.00, 0),
(28, 24, 11, 6, 190.00, 0),

(29, 34, 9, 4, 310.00, 0),


-- Construction Pro
(30, 5, 1, 4, 950.00, 0),
(31, 5, 4, 5, 55.00, 0),

(32, 15, 5, 6, 220.00, 0),
(33, 15, 8, 5, 270.00, 0),

(34, 25, 10, 6, 380.00, 0),
(35, 25, 11, 8, 190.00, 0),

(36, 35, 13, 3, 650.00, 0),


-- Medical Group
(37, 6, 2, 3, 720.00, 0),
(38, 6, 6, 6, 160.00, 0),

(39, 16, 7, 8, 85.00, 0),
(40, 16, 9, 3, 310.00, 0),

(41, 26, 12, 8, 145.00, 0),
(42, 26, 14, 5, 180.00, 0),

(43, 36, 15, 5, 240.00, 0),


-- Tech Solutions SA
(44, 7, 1, 3, 950.00, 0),
(45, 7, 5, 4, 220.00, 0),

(46, 17, 3, 8, 35.00, 0),
(47, 17, 4, 8, 55.00, 0),

(48, 27, 10, 5, 380.00, 0),
(49, 27, 11, 6, 190.00, 0),

(50, 37, 13, 2, 650.00, 0),


-- Education Belgium
(51, 8, 2, 2, 720.00, 0),
(52, 8, 8, 4, 270.00, 0),

(53, 18, 9, 3, 310.00, 0),
(54, 18, 10, 3, 380.00, 0),

(55, 28, 11, 5, 190.00, 0),
(56, 28, 12, 4, 145.00, 0),

(57, 38, 4, 5, 55.00, 0),


-- LogiTrans Belgium
(58, 9, 3, 5, 35.00, 0),
(59, 9, 14, 4, 180.00, 0),

(60, 19, 15, 3, 240.00, 0),
(61, 19, 5, 4, 220.00, 0),

(62, 29, 7, 4, 85.00, 0),
(63, 29, 4, 5, 55.00, 0),

(64, 39, 8, 2, 270.00, 0),


-- Retail Plus
(65, 10, 3, 5, 35.00, 0),
(66, 10, 4, 5, 55.00, 0),

(67, 20, 6, 4, 160.00, 0),
(68, 20, 7, 4, 85.00, 0),

(69, 30, 8, 3, 270.00, 0),
(70, 30, 9, 2, 310.00, 0),


-- Commande annulÃ©e :
-- elle doit Ãªtre ignorÃ©e dans le calcul du CA
(71, 40, 1, 10, 950.00, 0),
(72, 40, 13, 10, 650.00, 0);


-- =========================================
-- TESTS RAPIDES
-- =========================================

SELECT COUNT(*) AS nombre_clients
FROM customers;

SELECT COUNT(*) AS nombre_produits
FROM products;

SELECT COUNT(*) AS nombre_commandes
FROM orders;

SELECT COUNT(*) AS nombre_lignes_commandes
FROM order_items;


-- Chiffre d'affaires hors commandes annulÃ©es
SELECT
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS chiffre_affaires
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.status <> 'Cancelled';


-- Top 5 produits
SELECT
    p.product_name,
    SUM(oi.quantity) AS quantite_vendue
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
JOIN products p
    ON oi.product_id = p.product_id
WHERE o.status <> 'Cancelled'
GROUP BY p.product_id, p.product_name
ORDER BY quantite_vendue DESC
LIMIT 5;


-- Produits nÃ©cessitant un rÃ©approvisionnement
SELECT
    product_name,
    stock_quantity,
    reorder_level
FROM products
WHERE stock_quantity < reorder_level;
*************************************
Installation chez ta fille

Une fois ton schema.sql et ce seed.sql dans le dossier database/ :

mysql -u root -p < schema.sql
mysql -u root -p < seed.sql

Puis :

uv run streamlit run streamlit_app.py
