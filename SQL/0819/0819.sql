-- 1번
.tables

-- 2번
.schema

-- 3번

SELECT Title FROM albums ORDER BY Title DESC LIMIT 5;

-- 4번
SELECT Count(*) as "고객 수"  from customers;

-- 5번
SELECT FirstName,LastName FROM customers 
WHERE Country="USA" ORDER by FirstName DESC
LIMIT 5; 

-- 6번
SELECT count(BillingPostalCode) as "송장수"
FROM invoices
WHERE BillingPostalCode not null;

-- 7번 
SELECT *
FROM invoices
WHERE BillingState is NULL
ORDER by InvoiceDate DESC
LIMIT 5;

-- 8번 
SELECT COUNT(InvoiceDate) 
FROM invoices 
WHERE strftime("%Y", InvoiceDate) = '2013'; 

-- 9번 
SELECT CustomerId as"고객ID", FirstName as "이름", LastName as "성"
FROM customers
WHERE FirstName like 'L%'
ORDER by CustomerId;

-- 10번
SELECT count(Country) as "고객 수 ",Country as "나라"
FROM customers
GROUP by (Country)
HAVING count(Country)
ORDER by count(Country) DESC 
LIMIT 5;

-- 11번
SELECT ArtistId, count(ArtistId) as "앨범 수"
FROM albums
GROUP by ArtistId
ORDER by count(ArtistId) DESC
LIMIT 1;

-- 12번
SELECT ArtistId, count(ArtistId) as "앨범 수"
FROM albums
GROUP by ArtistId
HAVING count(ArtistId) >=10
ORDER by count(ArtistId) DESC
;

-- 13번
SELECT count(Country) as "고객 수" , Country, State
FROM customers
GROUP by Country, State
HAVING count(Country)
ORDER by count(Country) DESC
LIMIT 5;

-- 14번
SELECT CustomerId, 
             case
                WHEN Fax IS NULL THEN 'X'
                ELSE  'O'
             END as "Fax 유/무"
FROM customers
ORDER by CustomerId
LIMIT 5;

-- 15번
SELECT LastName, FirstName, (strftime('%Y','now')-BirthDate +1) as "나이"
from employees
ORDER by EmployeeId;



-- 16번

SELECT Name FROM artists 
WHERE ArtistId =
(
    SELECT ArtistId FROM albums 
    GROUP BY ArtistId 
    HAVING COUNT(*) 
    ORDER BY COUNT(*)
    DESC LIMIT 1
);

-- 17번
SELECT Name FROM genres 
WHERE GenreId = 
(
    SELECT GenreId FROM tracks 
    GROUP BY GenreId 
    ORDER BY COUNT(*) LIMIT 1
);

