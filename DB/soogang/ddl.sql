CREATE TABLE professors (
  p_id INT NOT NULL PRIMARY KEY, 
  p_name TEXT NOT NULL,
  p_age INT NOT NULL,
  p_department TEXT NOT NULL
);

CREATE TABLE students (
  st_id INT NOT NULL PRIMARY KEY,
  st_name TEXT NOT NULL,
  st_age INT NOT NULL,
  st_department TEXT NOT NULL
);


CREATE TABLE lectures (
  lecture_id TEXT NOT NULL PRIMARY KEY,
  l_name TEXT NOT NULL,
  p_id INT NOT NULL,
  CONSTRAINT p_id_fk FOREIGN KEY (p_id) REFERENCES professors(p_id)
);


CREATE TABLE registers (
  register_id TEXT NOT NULL PRIMARY KEY,
  st_id INT NOT NULL,
  l_id TEXT NOT NULL,
  CONSTRAINT st_id_fk FOREIGN KEY (st_id) REFERENCES students(st_id),
  CONSTRAINT l_id_fk FOREIGN KEY (l_id) REFERENCES lectures(lecture_id)
);


