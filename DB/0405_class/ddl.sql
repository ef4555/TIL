-- 여러 명령어를 한번에 실행시키기 위해 이 파일 사용


-- CREATE TABLE contacts (
--   name TEXT NOT NULL,
--   age INTEGER NOT NULL,
--   email TEXT NOT NULL UNIQUE
-- );

-- ALTER TABLE contacts RENAME TO new_contracts

-- DROP TABLE new_contracts;
ALTER TABLE users DROP COLUMN age;