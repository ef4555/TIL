-- CREATE TABLE users (
-- first_name TEXT NOT NULL,
-- last_name TEXT NOT NULL,
-- age INTEGER NOT NULL,
-- country TEXT NOT NULL,
-- phone TEXT NOT NULL,
-- balance INTEGER NOT NULL
-- );

-- SELECT first_name, age, balance FROM users
-- ORDER BY age, balance DESC;

-- SELECT first_name, age, balance FROM users
-- WHERE age >= 30 AND balance > 500000
-- ORDER BY balance ASC;


-- 중복 없이 모든 지역 조회
-- SELECT DISTINCT country FROM users;


-- SELECT first_name, last_name FROM users
-- WHERE first_name LIKE '%준';

-- SELECT first_name, age FROM users
-- WHERE age <= 29 AND age >= 20
-- ORDER BY age;

-- SELECT first_name, age FROM users
-- WHERE age LIKE '2%'
-- ORDER BY age;

-- SELECT first_name, phone FROM users
-- WHERE phone LIKE '%-51__-%';

-- SELECT first_name, country FROM users
-- WHERE country = '경기도' OR country = '강원도' ;


-- SELECT first_name, country FROM users
-- WHERE country IN ('경기도', '강원도');

-- SELECT first_name, country FROM users
-- WHERE country NOT IN ('경기도', '강원도');

-- SELECT rowid, first_name FROM users
-- LIMIT 10

-- SELECT first_name, balance FROM users
-- ORDER BY balance DESC
-- LIMIT 10

-- SELECT first_name, age FROM users
-- ORDER BY age ASC
-- LIMIT 5

-- SELECT first_name, last_name FROM users
-- WHERE first_name Like '예%';

SELECT first_name, country FROM users
WHERE first_name = '건우' AND country = '경기도';

SELECT * FROM users
ORDER BY age
LIMIT 50 OFFSET 20;
