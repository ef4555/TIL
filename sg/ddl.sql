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
  p_id INT NOT NULL
);


CREATE TABLE registers (
  register_id TEXT NOT NULL PRIMARY KEY,
  st_id INT NOT NULL,
  l_id TEXT NOT NULL
);

