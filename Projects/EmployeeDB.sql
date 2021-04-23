select * from employee; //query_ to display the results

CREATE TABLE employee
(
	employee_id bigserial ,
	first_name varchar(50),
	surname varchar(50),
	gender varchar(50),
	address varchar(50),
	email character(30),
 	depart_id int REFERENCES department(depart_id),
	role_id int REFERENCES roles(role_id),
	salary_id int REFERENCES salaries(salary_id),
	overtime_id int REFERENCES overtime(overtime_id),
	CONSTRAINT emp_key PRIMARY KEY (employee_id)
);

	
SELECT * FROM employee;
SELECT * FROM overtime;
SELECT * FROM department;
SELECT * FROM Salaries;
SELECT * from Roles;

CREATE TABLE Department(
	Depart_id serial,
	Depart_name varchar(25),
	depart_city varchar(50),
	CONSTRAINT Depart_key PRIMARY KEY (depart_id)
	);	
drop table department;
	
CREATE TABLE Roles(
	role_id serial,
	role_name varchar(25),
	CONSTRAINT roles_key PRIMARY KEY (role_id)
);
drop table roles;

SELECT * FROM Roles;


CREATE TABLE salaries(
	salary_id serial,
	salary_pa varchar(25),
	CONSTRAINT salaries_key PRIMARY KEY (salary_id)
);

		
CREATE TABLE overtime(
	overtime_id serial,
	overtime_hours time,
	CONSTRAINT overtime_key PRIMARY KEY(overtime_id)
);


INSERT INTO employee(first_name,surname,gender,address,email,depart_id,role_id,salary_id,Overtime_id)
VALUES
('Calvin','Moses','Male','32 Calcite kgrugersdorp','calvin@gmail.com',1,2,3,4),
('katleho','maile','male','111 eastgate','kat@gmail.com',2,1,3,4),
('william','nicole','male','22 east johannesburg','wiliam@yahoo.com',2,4,3,1),
('retha','mosedi','female','3 colian street','retha@gmail.com',1,3,4,2),
('taelo','chief','male','4 igret street','taelo@gmail.com',2,4,1,3),
('tumi','linder','female','122 robet','tumi@gmail.com',3,2,1,4),
('molefe','molete','male','133 flamengo','molefe@yahoo.com',2,4,3,1),
('mpoche','kgahliso','male','155 thembelihle','mpoche#gmail.com',4,1,2,3),
('liame','james','male','120 bonus','liame@gmail.com',1,2,4,3),
('morena','alias','male','9 robet stret','morena@gmail.com',4,3,1,2),
('celine','dion','male','10 king fisher','celine@gmail.com',2,3,4,2),
('bold','bolomo','male','1 cresent','bold@gmail.com',2,4,1,3);

 
INSERT INTO Department(depart_name,depart_city) 
VALUES
('Marketing','capetown'),
('technology','kgrugersdorp'),
('Finance','Sandton'),
('Human Resource', 'Randfontain');


INSERT INTO Roles(role_name)
VALUES
('manager'),
('trainee'),
('secretary'),
('director'),
('Junior developer'),
('Administrator'),
('Backend Developer'),
('Frondend developer'),
('IT manager');



INSERT INTO salaries(salary_pa)
VALUES
(8000),
(7000),
(6000),
(5000),
(4000),
(2000),
(1000),
(3000),
(9000),
(200),
(1230),
(450);

INSERT INTO overtime(overtime_hours)
VALUES
('02:00'),
('03:00'),
('04:00'),
('03:00'),
('05:00'),
('06:00'),
('12:00'),
('08:00'),
('13:00'),
('19:00');
