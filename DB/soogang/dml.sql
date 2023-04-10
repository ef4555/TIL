INSERT INTO professors (p_id, p_name, p_age, p_department)
VALUES 
  (1, '연제정', 30, '기계공학과'),
  (2, '최예훈', 30, '화학과'),
  (3, '정예륜', 30, '수학과'),
  (4, '김솔', 30, '심리학과');


INSERT INTO lectures (lecture_id, l_name, p_id)
VALUES 
  ('a001', 'DB', 1),
  ('a002', 'Django', 1),
  ('b001', 'Algo', 3),
  ('b002', 'Lego', 4);

INSERT INTO students (st_id, st_name, st_age, st_department)
VALUES 
  (1001, '정기석', 22, '기계공학과'),
  (1002, '기리보이', 25, '화학과'),
  (1003, '스윙스', 21, '심리학과'),
  (1004, '키드밀리', 22, '수학과'),
  (1005, '슈퍼비', 16, '수학과'),
  (1006, '면도', 27, '기계공학과');


INSERT INTO registers (register_id, l_id, st_id)
VALUES 
  (5, 'zxczcz01', 1001);

DELETE FROM registers WHERE l_id='a001';



SELECT p.p_name, l.l_name FROM professors AS p INNER JOIN lectures AS l ON p.p_id=l.p_id

SELECT s.st_name AS 학생명, r.l_id AS 과목번호 FROM students AS s INNER JOIN registers AS r ON s.st_id = r.st_id;

SELECT s.st_name, l.l_name, p.p_name FROM registers AS r INNER JOIN students AS s ON r.st_id = s.st_id 
INNER JOIN lectures AS l ON r.l_id = l.lecture_id
INNER JOIN professors AS p ON l.p_id = p.p_id
WHERE p.p_name = '연제정';

SELECT l.l_name FROM lectures AS l INNER JOIN registers AS r ON r.l_id = l.lecture_id 
