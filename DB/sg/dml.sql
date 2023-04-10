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
  (1, 'a002', 1001),
  (2, 'a001', 1001),
  (3, 'b001', 1004),
  (4, 'b001', 1004);

SELECT p.p_name, l.l_name FROM professors AS p INNER JOIN lectures AS l ON p.p_id=l.p_id