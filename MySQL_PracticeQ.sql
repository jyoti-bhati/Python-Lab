create database School ;
use School ;
create table Student(rollno varchar(10) ,Name varchar(5), class varchar(5));
ALTER TABLE Student MODIFY name varchar(25);
ALTER TABLE Student ADD PRIMARY KEY(rollno);
insert into Student ( rollno,Name, class) values(101,'Anvika','10'),(102,'Rohan','12') ,(103,'Tanisha','12') ,(104,'Maheshwari','11') ;
alter table Student  add marks int;
SELECT * from Student;

-- Add a new column 'age' 
ALTER TABLE Student ADD COLUMN age INT;

-- Modify the 'class' column
ALTER TABLE Student MODIFY COLUMN class VARCHAR(10);

-- Remove the primary key 
ALTER TABLE Student DROP PRIMARY KEY;

-- Change the data type 
ALTER TABLE Student MODIFY COLUMN rollno INT AUTO_INCREMENT PRIMARY KEY;

-- Drop the column 'age' 
ALTER TABLE Student DROP COLUMN age;

-- Retrieve all students whose names start with 'A'
SELECT * FROM Student WHERE Name LIKE 'A%';

-- Display all students who belong to class '10'
SELECT * FROM Student WHERE class = '10';

-- Fetch the total number of students in each class
SELECT class, COUNT(*) AS total_students FROM Student GROUP BY class;

-- Select students whose roll number
SELECT * FROM Student WHERE rollno LIKE '%0%';

-- Retrieve distinct class names 
SELECT DISTINCT class FROM Student;

-- Retrieve the highest marks obtained by any student
SELECT MAX(marks) AS highest_marks FROM student;

-- List the students 
SELECT * FROM Student WHERE marks < 80;

-- Find the average marks of students in each class
SELECT class, AVG(marks) AS average_marks FROM Student GROUP BY class;

-- Retrieve the details of students who do not have marks recorded in the marks table
SELECT * FROM Student WHERE rollno NOT IN (SELECT rollno FROM marks);


-- Find the students who have the second-highest marks
SELECT * FROM Student WHERE marks = (SELECT DISTINCT marks FROM student ORDER BY marks DESC LIMIT 1 OFFSET 1);

-- Retrieve the top 5 students based on their marks
SELECT * FROM Student ORDER BY marks DESC LIMIT 5;

-- Display students sorted by name in ascending order and class in descending order
SELECT * FROM Student ORDER BY name ASC, class DESC;
