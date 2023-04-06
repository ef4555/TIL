
SELECT first_name, phone, country FROM users 
-- WHERE phone LIKE '%-51__-%' AND country NOT IN ('서울');
WHERE phone LIKE '%-51__-%' AND country != '서울';