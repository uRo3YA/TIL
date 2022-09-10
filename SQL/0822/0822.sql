-- 1번 

SELECT * FROM playlist_track as A
ORDER BY A.PlaylistId DESC
LIMIT 5;

-- 2번

SELECT * FROM tracks as B
ORDER BY B.TrackId DESC
LIMIT 5;

--3번
SELECT playlist_track.PlaylistId,tracks.Name FROM playlist_track
join tracks
on playlist_track.TrackId=tracks.TrackId
ORDER BY playlist_track.PlaylistId DESC
LIMIT 10;
--4번
SELECT playlist_track.PlaylistId,tracks.Name FROM playlist_track
join tracks
on playlist_track.TrackId=tracks.TrackId
WHERE  playlist_track.PlaylistId=10
ORDER BY playlist_track.PlaylistId DESC
LIMIT 10;

--5번
SELECT count(*) as "작곡가 수(INNER join)" FROM tracks
join artists
on artists.name=tracks.Composer;
--6번
SELECT count(*) as "작곡가 수(left join)" FROM tracks
left join artists
on artists.name=tracks.Composer;

--8번
SELECT InvoiceLineId, InvoiceId FROM invoice_items
ORDER by InvoiceId 
LIMIT 5;
--9번
SELECT InvoiceId, CustomerId FROM invoices
ORDER by InvoiceId 
LIMIT 5; 

--10번
SELECT invoices.InvoiceId, invoice_items.InvoiceLineId FROM invoices
join invoice_items
WHERE invoice_items.InvoiceId=invoices.InvoiceId
ORDER by invoices.InvoiceId desc
LIMIT 5; 
--11번
SELECT invoices.InvoiceId, customers .CustomerId FROM invoices
join customers 
    on  customers .CustomerId=invoices.CustomerId
ORDER by invoices.InvoiceId desc
LIMIT 5; 

-- 12번
SELECT invoices.InvoiceId, invoice_items.InvoiceLineId, customers .CustomerId FROM invoices
join invoice_items
    on  invoice_items.InvoiceId=invoices.InvoiceId
join customers 
    on  customers .CustomerId=invoices.CustomerId
ORDER by invoices.InvoiceId desc
LIMIT 5; 

-- 13번
SELECT C.CustomerId as "고객 ID" , count(*) As "개수" FROM invoice_items as A
INNER JOIN (
    SELECT * FROM invoices as A
    INNER JOIN customers as B
    ON A.CustomerId = B.CustomerId
) as C
ON A.InvoiceId = C.InvoiceId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;
