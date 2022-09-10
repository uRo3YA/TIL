
CREATE TABLE healthcare (
    id PRIMARY KEY,        
    sido INTEGER NOT NULL, 
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,  
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,   
    va_left REAL NOT NULL, 
    va_right REAL NOT NULL,

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);


--2번
select min(age),max(age) from healthcare ; 

--3번
select min(height),max(height),min(weight),max(weight)  from healthcare;
--4번
select count(*) from healthcare where height>=160 and height <=170;
select count(*) from healthcare where  height BETWEEN 160 and 170;

--5번
SELECT waist FROM healthcare WHERE is_drinking = 1 AND waist != '' ORDER BY waist DESC LIMIT 5;

--6번
select count(*) from healthcare where (va_left>=1.5 and va_right>=1.5) and is_drinking=1;
--7번
select count(*) from healthcare where blood_pressure<120;
--8번
select avg(waist) from healthcare where blood_pressure>=140;
--9번
SELECT avg(height),avg(weight) from healthcare WHERE gender=1;
--10번

SELECT DISTINCT id,height,weight from healthcare WHERE height=(SELECT max(height) FROM healthcare );
-- 11번
-- BMI는 체중/(키*키)의 계산 결과이다. 
SELECT COUNT(*) FROM healthcare WHERE weight*10000/(height*height) >= 30;
SELECT id,weight/(height*height*0.0001) AS BMI FROM healthcare WHERE smoking=3 ORDER BY BMI DESC LIMIT 5;
--12번
SELECT  ID, weight*10000/(height*height)AS BMI 
    FROM healthcare 
    WHERE smoking=3 
    ORDER BY BMI DESC LIMIT 5;

