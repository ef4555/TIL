INSERT INTO articles VALUES
    ('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 3);


INSERT INTO users VALUES
    ('aiden', 1),
    ('ken', 2),
    ('lynda', 3);
  

INSERT INTO roles VALUES
    ('admin'),
    ('staff'),
    ('student');


SELECT u.name, r.role FROM users AS u INNER JOIN roles AS r WHERE u.role_id = r.rowid
