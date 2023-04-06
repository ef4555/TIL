-- users table 생성
-- CREATE TABLE users (
--     first_name TEXT NOT NULL,
--     last_name TEXT NOT NULL,
--     age INTEGER NOT NULL,
--     country TEXT NOT NULL,
--     phone TEXT NOT NULL,
--     balance INTEGER NOT NULL
-- );

-- SELECT country, AVG(balance) FROM users
-- GROUP BY country ORDER BY avg(balance) DESC;


-- SELECT AVG(age) FROM users
-- WHERE age >= 30

-- SELECT country FROM users GROUP BY country;

-- SELECT last_name, COUNT(*) AS number_of_name FROM users
-- GROUP BY last_name ORDER BY COUNT(*) DESC;

-- CREATE TABLE classmates (
--     name TEXT NOT NULL,
--     age INTEGER NOT NULL,
--     address TEXT NOT NULL
-- );

-- INSERT INTO classmates (name, age, address)
-- VALUES ('홍길동', 23, '서울')

-- INSERT INTO classmates 
-- VALUES 
--   ('김철수', 23, '경기'),
--   ('이영미', 23, '강원'),
--   ('박진성', 23, '전라'),
--   ('최지수', 23, '충청'),
--   ('정요한', 23, '경상');

-- UPDATE classmates
-- SET name='김철수한무두루미',
--   address='제주도'
-- WHERE rowid = 2;

-- DELETE FROM classmates WHERE rowid = 5;
-- SELECT rowid, * FROM classmates;

-- DELETE FROM classmates WHERE name LIKE '%영%';