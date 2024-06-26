-- 테이블 만들기
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
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare


-- # 문제

--1. 추가되어 있는 모든 데이터의 수를 출력하시오.

SELECT COUNT(*) FROM healthcare;
-- COUNT(*)
-- --------
-- 1000000

--  2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.
select count(*) from healthcare where age <10; 
-- count(*)  
-- ----------
-- 156277

--  3. 성별이 1인 사람의 수를 출력하시오.
select count(*) from healthcare where gender = 1;
-- count(*)  
-- ----------
-- 510689

--  4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.
select count(*) from healthcare where smoking=3 and is_drinking=1;
-- count(*)  
-- ----------
-- 150361

--  5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.
select count(*) from healthcare where va_left >=2  and va_right >=2; 
-- count(*)  
-- ----------
-- 2614

--  6. 시도(sido)를 모두 중복 없이 출력하시오.
select DISTINCT sido from healthcare;
-- sido      
-- ----------
-- 36
-- 27
-- 11
-- 31
-- 41
-- 44
-- 48
-- 30
-- 42
-- 43
-- 46
-- 28
-- 26
-- 47
-- 45
-- 29
-- 49

--  자유롭게 조합해서 원하는 데이터를 출력해보세요.
-- Q. 정상혈압(120~80)을 벗어난 사람의 수를 출력
select count(*) from healthcare where blood_pressure>120 or blood_pressure<80;
-- count(*)  
-- ----------
-- 576816
 
