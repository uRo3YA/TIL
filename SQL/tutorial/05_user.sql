-- SQLite
CREATE TABLE users (

last_name Text NOT NULL,
first_name Text NOT NULL,
age INTEGER NOT NULL,
country Text NOT NULL,
phone INTEGER NOT NULL,

);

-- csv import 하기
.mode csv 
.import users.csv users