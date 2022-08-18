
-- 1번 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

SELECT  smoking,COUNT(*)
FROM healthcare

GROUP BY smoking;

-- 2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.
SELECT  is_drinking,COUNT(is_drinking)
FROM healthcare
GROUP BY is_drinking;

-- 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.

SELECT  is_drinking,COUNT(blood_pressure)
FROM healthcare
where blood_pressure>=200
GROUP BY is_drinking;

-- 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.
SELECT  sido,COUNT(sido)
FROM healthcare
GROUP BY sido
HAVING COUNT(sido) >  50000;

-- 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.
SELECT  height,COUNT(height)
FROM healthcare
GROUP BY height 
ORDER by height Desc
LIMIT 5;

-- 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

SELECT  weight,height,count(*)
FROM healthcare
GROUP BY height , weight
ORDER by height Desc
LIMIT 5
;

-- 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.
SELECT  is_drinking,avg(waist)
FROM healthcare
WHERE waist != ''
GROUP BY is_drinking;

--8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.
SELECT  round(avg(va_left),2) as "평균 왼쪽 시력",round(avg(va_right),2) as "평균 오른쪽 시력"
FROM healthcare
GROUP BY gender;

-- 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.
-- 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

SELECT  age,avg(height) as '평균 키', avg(weight) as "평균 몸무게"
FROM healthcare
GROUP BY age
HAVING avg(height)>=160 and avg(weight)>=60;


-- 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.
SELECT  is_drinking,smoking,avg(weight*10000/(height*height))AS "평균 BMI" 
FROM healthcare 
WHERE is_drinking!="" and smoking!=""
GROUP BY is_drinking,smoking;
