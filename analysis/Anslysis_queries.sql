CREATE TABLE teachers (
id bigserial,
first_name varchar(25),
last_name varchar(50),
school varchar(50),
hire_date date,
salary numeric
);
SELECT first_name, last_name FROM teachers;

INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
 VALUES ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000),
('Samuel', 'Cole', 'Myers Middle School', '2005-08-01', 43500),
('Samantha', 'Bush', 'Myers Middle School', '2011-10-30', 36200),
('Betty', 'Diaz', 'Myers Middle School', '2005-08-30', 43500),
('Kathleen', 'Roush', 'F.D. Roosevelt HS', '2010-10-22', 38500);

SELECT * FROM teachers;

INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
values('kamo','maile','carlton jones','2021-03-23',2400),
('lime','john','wonnies','2020-02-11',11000),
('kelvin','moses','cj','2020-08-03',10000);

SELECT * FROM teachers;