
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


--3번
select min(height),max(height),min(weight),max(weight)  from healthcare;
--4번
select count(*) from healthcare where height>=160 and height <=170;

--5번
SELECT waist FROM healthcare  where is_drinking=1 ORDER BY waist DESC LIMIT 3;
SELECT waist FROM healthcare ORDER BY waist DESC LIMIT 3;

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

SELECT id,height,weight
  FROM (SELECT height AS RN, height
         FROM(SELECT height
               FROM healthcare
              ORDER BY height DESC))
 WHERE RN = 2;

 -- 11번
 -- BMI는 체중/(키*키)의 계산 결과이다. 
 select (weight/(height*height)) as BMI from healthcare where BMI>=30;