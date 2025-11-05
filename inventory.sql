
CREATE TABLE supplier (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    contact_email VARCHAR(255) NULL,
    phone       VARCHAR(50)  NULL,
    address     TEXT NULL,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE warehouse(
    id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    code        VARCHAR(32) NOT NULL UNIQUE,
    name        VARCHAR(255) NOT NULL,
    address     TEXT,
    status      ENUM('active','inactive') NOT NULL DEFAULT 'active',
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE product (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    sku         VARCHAR(64) NOT NULL UNIQUE,
    name        VARCHAR(255) NOT NULL,
    description TEXT,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE product_variant (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_id  BIGINT UNSIGNED NOT NULL,
    name        VARCHAR(255) NOT NULL,          -- e.g. “Red – Large”
    extra_json  JSON NULL,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
);

CREATE TABLE inventory (
    id                BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_id        BIGINT UNSIGNED NOT NULL,
    variant_id        BIGINT UNSIGNED NULL,
    warehouse_id      INT UNSIGNED NOT NULL,
    supplier_id       BIGINT UNSIGNED NULL,
    quantity_on_hand  INT UNSIGNED NOT NULL DEFAULT 0,
    quantity_reserved INT UNSIGNED NOT NULL DEFAULT 0,
    cost_price        DECIMAL(12,4) NULL,
    retail_price      DECIMAL(12,4) NULL,
    currency_code     CHAR(3) DEFAULT 'USD',
    status            ENUM('active','inactive','discontinued') NOT NULL DEFAULT 'active',
    last_stock_update DATETIME NULL,
    created_at        DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at        DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id)   REFERENCES product(id)   ON DELETE CASCADE,
    FOREIGN KEY (variant_id)   REFERENCES product_variant(id) ON DELETE SET NULL,
    FOREIGN KEY (warehouse_id) REFERENCES warehouse(id) ON DELETE RESTRICT,
    FOREIGN KEY (supplier_id)  REFERENCES supplier(id)  ON DELETE RESTRICT,
    UNIQUE KEY uq_prod_variant_wh (product_id, variant_id, warehouse_id)
);


-- -------------------------------------------------
-- 1. Suppliers
-- -------------------------------------------------
INSERT INTO supplier (name, contact_email, phone, address) VALUES
('Acme Textiles',      'sales@acme.com',      '555-0100', '100 Industrial Way, Springfield'),
('Global Fabrics',     'info@globalfabrics.com','555-0200','200 Market St, Metropolis');

-- -------------------------------------------------
-- 2. Warehouses
-- -------------------------------------------------
INSERT INTO warehouse (code, name, address) VALUES
('NYC', 'New York Distribution Center', '123 5th Ave, New York, NY 10001'),
('LAX', 'Los Angeles Fulfillment Hub',   '456 Sunset Blvd, Los Angeles, CA 90028');

-- -------------------------------------------------
-- 3. Products
-- -------------------------------------------------
INSERT INTO product (sku, name, description) VALUES
('TSHIRT001', 'Basic T‑Shirt', '100% cotton, unisex'),
('HOODIE002', 'Premium Hoodie', 'Heavy‑weight fleece, zip‑up');

-- -------------------------------------------------
-- 4. Product variants (only for the hoodie)
-- -------------------------------------------------
INSERT INTO product_variant (product_id, name, extra_json) VALUES
(2, 'Black – Small',  JSON_OBJECT('size','S','color','Black')),
(2, 'Black – Medium', JSON_OBJECT('size','M','color','Black')),
(2, 'Gray – Large',   JSON_OBJECT('size','L','color','Gray'));

-- -------------------------------------------------
-- 5. Inventory rows
-- -------------------------------------------------
-- T‑Shirt (no variant) stocked in both warehouses, supplied by Acme (supplier_id = 1)
INSERT INTO inventory (product_id, variant_id, warehouse_id, supplier_id,
                       quantity_on_hand, quantity_reserved, cost_price, retail_price)
VALUES
(1, NULL, 1, 1, 250, 10, 5.00, 12.99),   -- NYC
(1, NULL, 2, 1, 180,  5, 5.00, 12.99);   -- LAX

-- Hoodie variants
-- Black – Small (variant_id = 1) in NYC, supplied by Global Fabrics (supplier_id = 2)
INSERT INTO inventory (product_id, variant_id, warehouse_id, supplier_id,
                       quantity_on_hand, quantity_reserved, cost_price, retail_price)
VALUES
(2, 1, 1, 2, 40, 2, 15.00, 34.99),

-- Black – Medium (variant_id = 2) in NYC, supplied by Acme
(2, 2, 1, 1, 55, 4, 15.00, 34.99),

-- Gray – Large (variant_id = 3) in LAX, supplied by Global Fabrics
(2, 3, 2, 2, 30, 1, 16.00, 35.99);




-- Some Query:

SELECT
    p.sku,
    p.name               AS product_name,
    pv.name               AS variant_name,
    w.code                AS warehouse,
    s.name                AS supplier,
    i.quantity_on_hand,
    i.quantity_reserved,
    i.cost_price,
    i.retail_price
FROM inventory AS i
JOIN product   AS p  ON p.id = i.product_id
LEFT JOIN product_variant AS pv ON pv.id = i.variant_id
JOIN warehouse AS w  ON w.id = i.warehouse_id
JOIN supplier  AS s  ON s.id = i.supplier_id
ORDER BY p.sku, pv.id, w.code;

