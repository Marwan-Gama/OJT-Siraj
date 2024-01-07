USE northwind;

-- Q1 --
SELECT 
    FirstName, 
    HireDate,
    Region,
    Country
FROM Employees 
;

-- Q2 --
SELECT 
    ProductID, 
    ProductName,
    UnitPrice AS Price
FROM Products 
;

-- Q3 --
SELECT
	CustomerID,
	CONCAT(City,' - ' ,Address) AS Full_Address  
FROM Customers 
;

-- Q4 --
SELECT
	DISTINCT Country
FROM employees
;

-- Q5 --
SELECT
	ProductName,
    UnitPrice AS Prise,
    UnitPrice*0.8 AS Prise_without_VAT
FROM products
;

-- Q6 --
SELECT * 
FROM orders 
WHERE ShippedDate > RequiredDate
;

-- Q7 --
SELECT * 
FROM employees
WHERE City = 'London' OR City = 'Seattle ' OR City = 'Tacoma'
;

-- Q8 --
SELECT * 
FROM customers
WHERE Region IS NULL
;

-- Q9 --
SELECT *
FROM orders
ORDER BY OrderDate DESC
LIMIT 7
;

-- Q10 --
SELECT 
	LEFT(ProductName, 10) AS truncated_name
FROM products
;

-- Q11 --
SELECT 
	CONCAT(FirstName,' ' ,LastName),
    replace(Title,'Sales','Marketing')
FROM employees
;

-- Q12 --
SELECT 
    CONCAT(ProductID, ' AND ', SupplierID) AS 'Product id + Supplier id',
    FLOOR(UnitPrice * 0.8) AS 'No VAT'
FROM 
    Products
WHERE 
    FLOOR(UnitPrice * 0.8) > 30
;

-- Q13 --
SELECT 
    LOWER(FirstName) AS lowercase_first_name,
    REVERSE(LastName) AS reversed_last_name
FROM 
    employees
WHERE 
    ReportsTo IS NOT NULL
;

-- Q14 --
SELECT *
FROM employees
WHERE LENGTH(LastName) > LENGTH(FirstName);
;

-- Q15 --
SELECT 
    OrderID,
    EmployeeID,
    OrderDate,
    RequiredDate,
    ShipName
FROM 
    orders
WHERE 
    EmployeeID = 7
    AND ShipName IN ('QUICK-Stop', 'Around the Horn', 'Frankenversand')
    AND DATEDIFF(RequiredDate, OrderDate) < 14
;

-- Q16 --
SELECT 
    ProductID,
    ProductName,
    UnitPrice
FROM 
    products
WHERE 
    UnitPrice > (SELECT UnitPrice FROM products WHERE ProductName = 'Chocolade')
;

-- Q17 --
SELECT 
    o.OrderID,
    o.OrderDate,
    o.ShipAddress,
    c.CustomerID,
    c.ContactName,
    c.Phone
FROM 
    orders o
JOIN 
    customers c ON o.CustomerID = c.CustomerID
WHERE 
    YEAR(o.OrderDate) = 1996
    AND (c.CustomerID LIKE 'A%' OR c.CustomerID LIKE 'C%')
;

-- Q18 --
SELECT 
    FirstName,
    LastName,
    HireDate
FROM 
    employees
WHERE 
    HireDate > (
        SELECT HireDate 
        FROM employees 
        WHERE EmployeeID = 6
    )
;

-- Q19 --
SELECT 
    ProductID,
    ProductName,
    UnitPrice
FROM 
    products
WHERE 
    UnitPrice > (
        SELECT AVG(UnitPrice) 
        FROM products
    )
;

-- Q20 --
SELECT 
    ProductName,
    QuantityPerUnit
FROM 
    products 
WHERE 
    QuantityPerUnit < (
        SELECT MIN(QuantityPerUnit)
        FROM products
        WHERE ProductID = 5
    )
;

-- Q21 --
SELECT *
FROM products
WHERE CategoryID = (
    SELECT CategoryID
    FROM products
    WHERE ProductName = 'Chai'
) AND ProductName != 'Chai'
;

-- Q22 --
SELECT 
	ProductName,
	UnitPrice
FROM 
	products
WHERE 
	UnitPrice IN (
	SELECT DISTINCT UnitPrice
	FROM products
	WHERE CategoryID = 5
	)
    AND CategoryID != 5
;

-- Q23 --
SELECT 
	ProductName,
	UnitPrice
FROM 
	products
WHERE 
	UnitPrice > (
	SELECT  MIN(UnitPrice)
	FROM products
	WHERE CategoryID = 5
	)
    AND CategoryID != 5
;

-- Q24 --
SELECT 
	ProductName,
	UnitPrice
FROM 
	products
WHERE 
	UnitPrice > (
	SELECT  MAX(UnitPrice)
	FROM products
	WHERE CategoryID = 5
	)
    AND CategoryID != 5
;

-- Q25 --
SELECT 
    OrderID,
    OrderDate
FROM 
    orders
WHERE 
    YEAR(OrderDate) = 1997
    AND CustomerID IN (
        SELECT CustomerID
        FROM customers
        WHERE Country IN ('Franch', 'Germany', 'Sweden')
    )
;

-- Q26 --
SELECT 
    ProductName,
    ProductID
FROM 
    products
WHERE 
    UnitPrice > (
        SELECT AVG(UnitPrice)
        FROM products
        WHERE UnitsInStock > 50
    )
;

-- Q27 --
SELECT 
    ProductName
FROM 
    products
WHERE 
    CategoryID IN (
        SELECT CategoryID
        FROM categories
        WHERE CategoryName IN ('Beverages','Condiments')
    )
    AND SupplierID IN (
        SELECT SupplierID
        FROM suppliers
        WHERE Region IS NULL
    )
;

-- Q28 --
SELECT 
    SupplierID,
    MAX(UnitPrice) AS max_price
FROM 
    products
GROUP BY 
    SupplierID
ORDER BY 
    SupplierID DESC;
;

-- Q29 --
SELECT 
    CategoryID,
    AVG(UnitPrice) AS avg_price
FROM 
    products
WHERE 
    UnitPrice > 42
GROUP BY 
    CategoryID;
    
-- Q30 --
SELECT 
    c.CategoryName,
    SUM(p.QuantityPerUnit) AS total_ordered_units,
    SUM(p.UnitsInStock) AS total_units_in_stock
FROM 
    products p
JOIN 
    categories c ON p.CategoryID = c.CategoryID
WHERE 
    c.CategoryName LIKE '%c%' 
    AND p.QuantityPerUnit > 95
GROUP BY 
    c.CategoryName
ORDER BY 
    c.CategoryName;