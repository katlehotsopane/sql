
CREATE TABLE animal_info (
id bigserial,
kind varchar(25),
habitats varchar(50),
weight numeric
);

drop table zoo;

SELECT * From animal_info; 
 
INSERT INTO animal_info (kind, habitats,weight)
values ('lion','grassland',50),
('elephant','grassland',70),
('camel','derset',60);

CREATE TABLE animal(
id bigserial,
kind varchar(25)
);
SELECT * From animal;
INSERT INTO animal(kind)
values('snake'),('camel'),('tortoise'),('lizard')

----------------------------------------------------------------------

CREATE TABLE char_data_types (
varchar_column varchar(10),
char_column char(10),
text_column text
);
INSERT INTO char_data_types
VALUES
('abc', 'abc', 'abc'),
('defghi', 'defghi', 'defghi');

COPY char_data_types TO 'C:\YourDirectory\typetest.txt'
WITH (FORMAT CSV, HEADER, DELIMITER '|');
