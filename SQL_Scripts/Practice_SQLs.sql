/*--------------------------------------------------------------------------*/
/* Some of the sql practice queries that i have done                        */
/* Various concepts like window functions, recursive queries, sub queries,  */
/* pivoting data, deleting duplicates, finding nth max sal, etc             */
/*--------------------------------------------------------------------------*/
create table temp_user (euser_id int primary key, euser_name varchar(30), email varchar(50) );

insert into temp_user values(5, 'Robin','Robin@gmail.com');

select * from temp_user;

select * from (select euser_name, count(euser_name) cnt from temp_user group by euser_name ) a;

select euser_id, euser_name, email from (
select *, ROW_NUMBER() over (partition by euser_name order by euser_id) rn from temp_user) x
where x.rn > 1;

/*--------------------------------------------------------------------------*/

select euser_id, euser_name, email from 
(select *, ROW_NUMBER() over (order by euser_id desc ) rn from temp_user) x
where x.rn = 2;

/*--------------------------------------------------------------------------*/
create table employee (emp_id int primary key, emp_name varchar(50), dept_name varchar(50), salary int);

insert into employee values(101,'Gautam', 'Admin', 2000);
insert into employee values(111,'Alok', 'Admin', 3500);
insert into employee values(121,'Tom', 'Admin', 3000);
insert into employee values(131,'Bran', 'Admin', 2000);
insert into employee values(107,'Khal', 'Finance', 4000);
insert into employee values(117,'Zora', 'Finance', 2900);
insert into employee values(127,'Sam', 'Finance', 3500);
insert into employee values(137,'Drogo', 'Finance', 3700);
insert into employee values(109,'Ed', 'HR', 1200);
insert into employee values(119,'Sansa', 'HR', 1350);
insert into employee values(129,'Arya', 'HR', 1570);
insert into employee values(139,'Hodor', 'HR', 1440);
insert into employee values(173,'Namiria', 'IT', 8500);
insert into employee values(167,'Ghost', 'IT', 7600);
insert into employee values(146,'Raven', 'IT', 7750);
insert into employee values(198,'White', 'IT', 8350);
insert into employee values(123,'Knight', 'IT', 9125);
insert into employee values(145,'King', 'IT', 11000);
insert into employee values(169,'Tyrian', 'IT', 5570);
insert into employee values(165,'Tywin', 'IT', 6750);

select * from employee;

select emp_id, emp_name, e.dept_name, e.salary,  x.max_sal, x.min_sal  from employee e, 
(select  dept_name, min(salary) min_sal, max(salary) max_sal from employee group by dept_name ) x 
where x.dept_name = e.dept_name and e.salary in (x.min_sal, x.max_sal);

/*--------------------------------------------------------------------------*/
create table DOCTORS(id int primary key, name varchar(50), speciality varchar(100), hospital varchar(50), city varchar(50), consultaion_fee integer);

insert into DOCTORS values(1,'Dr. Shashank','Ayurveda','Apollo Hospital','Bangalore',2500);
insert into DOCTORS values(2,'Dr. Abdul','Homeopathy','Fortis Hospital','Bangalore',2000);
insert into DOCTORS values(3,'Dr. Shwetha','Homeopathy','KMC Hospital','Manipal',1000);
insert into DOCTORS values(4,'Dr. Murphy','Dermatology','KMC Hospital','Manipal',1500);
insert into DOCTORS values(5,'Dr. Farhana','Physician','Gleneagles Hospital','Bangalore',1700);
insert into DOCTORS values(6,'Dr. Maryan','Physician','Gleneagles Hospital','Bangalore',1500);

select * from DOCTORS;

/*4. From the doctors table, fetch the details of doctors who work in the same hospital but in different specialty.*/

select * FROM DOCTORS A, DOCTORS B where A.HOSPITAL=B.HOSPITAL and A.SPECIALITY <> B.SPECIALITY;

/*Write SQL query to fetch the doctors who work in same hospital irrespective of their specialty.*/

SELECT * FROM DOCTORS A, 
(SELECT HOSPITAL, COUNT(HOSPITAL) CNT FROM DOCTORS GROUP BY HOSPITAL HAVING COUNT(HOSPITAL) > 1 ) B
where A.HOSPITAL = B.HOSPITAL;

/*--------------------------------------------------------------------------*/
create table LOGIN_DETAILS (login_id int primary key, user_name varchar(50), login_date date);

insert into LOGIN_DETAILS values(101, 'Michael','8/21/2021');
insert into LOGIN_DETAILS values(102, 'James', '8/21/2021');
insert into LOGIN_DETAILS values(103, 'Stewart','8/22/2021');
insert into LOGIN_DETAILS values(104, 'Stewart','8/22/2021');
insert into LOGIN_DETAILS values(105, 'Stewart','8/22/2021');
insert into LOGIN_DETAILS values(106, 'Michael','8/23/2021');
insert into LOGIN_DETAILS values(107, 'Michael','8/23/2021');
insert into LOGIN_DETAILS values(108, 'Stewart', '8/24/2021');
insert into LOGIN_DETAILS values(109, 'Stewart', '8/24/2021');
insert into LOGIN_DETAILS values(110, 'James','8/25/2021');
insert into LOGIN_DETAILS values(111, 'James','8/25/2021');
insert into LOGIN_DETAILS values(112, 'James','8/26/2021');
insert into LOGIN_DETAILS values(113, 'James','8/27/2021');

select * from LOGIN_DETAILS;

/*From the login_details table, fetch the users who logged in consecutively 3 or more times.*/

with cte as 
(select *, 
case when user_name = lead(user_name) over (order by login_id) -- here we compare the current record user name with next record user name
	 and user_name = lead(user_name, 2) over (order by login_id) -- here we gave offset 2 in lead function to check next to next record
	 then user_name -- if both the above conditions are true we get user name else null in repeated_users columns
	 else null
end as repeated_users
from LOGIN_DETAILS )

select distinct user_name from cte where repeated_users is not null;

/*--------------------------------------------------------------------------*/

/*6. From the students table, write a SQL query to interchange the adjacent student names.
Note: If there are no adjacent student then the student name should stay the same.
Table Name: STUDENTS
Approach: Assuming id will be a sequential number always. If id is an odd number then fetch the student name from the following record. If id is an even number then fetch the student name from the preceding record. Try to figure out the window function which can be used to fetch the preceding the following record data. 
If the last record is an odd number then it wont have any adjacent even number hence figure out a way to not interchange the last record data.*/

create table STUDENTS(id int primary key, student_name varchar(50));

insert into STUDENTS VALUES (1, 'James');
insert into STUDENTS VALUES (2, 'Michael');
insert into STUDENTS VALUES (3, 'George');
insert into STUDENTS VALUES (4, 'Stewart');
insert into STUDENTS VALUES (5, 'Robin');

select * from STUDENTS;

select *, 
case when id%2 <> 0 
	then lead(student_name,1,student_name) over (order by id) 
	else lag(student_name) over (order by id)
end as adjacent_student 
from STUDENTS;

select *, lead(student_name,1,student_name) over (order by id)  from STUDENTS;
select *, lag(student_name) over (order by id)  from STUDENTS;
/*--------------------------------------------------------------------------*/

/*7. From the weather table, fetch all the records when London had extremely cold temperature for 3 consecutive days 
or more.
Note: Weather is considered to be extremely cold when its temperature is less than zero.
Table Name: WEATHER
Approach: First using a sub query identify all the records where the temperature was very cold and then use a 
main query to fetch only the records returned as very cold from the sub query. You will not only need to compare 
the records following the current row but also need to compare the records preceding the current row. And may also 
need to compare rows preceding and following the current row. Identify a window function which can do this comparison 
pretty easily.*/

create table weather (id int, city varchar(20), temperature int, day date);

insert into  weather values(1,'LONDON',-1, '2021-01-01');
insert into  weather values(2,'LONDON',-2, '2021-01-02');
insert into  weather values(3,'LONDON',4, '2021-01-03');
insert into  weather values(4,'LONDON',1, '2021-01-04');
insert into  weather values(5,'LONDON',-2, '2021-01-05');
insert into  weather values(6,'LONDON',-5, '2021-01-06');
insert into  weather values(7,'LONDON',-7, '2021-01-07');
insert into  weather values(8,'LONDON',5, '2021-01-08');

select * from weather;

with cte as 
(select *, 
case 
	when temperature < 0 --current day should be less than 0
	 and lead (temperature, 1) over (order by day) < 0 -- next day should be less than 0 as well 
	 and lead(temperature, 2) over (order by day) < 0 --next to next day also should be less than 0 
	then 'YES'

	when temperature < 0  --current day should be less than 0
	 and lag (temperature) over (order by day) < 0 --previous day should be less than 0
	 and lead(temperature) over (order by day) < 0 --next day should be less than 0 
	then 'YES'

	when temperature < 0 --current day should be less than 0 
	 and lag (temperature, 1) over (order by day) < 0 --previous day should be less than 0
	 and lag(temperature, 2) over (order by day) < 0 --2 days prior also shouls be less than 0
	then 'YES'

	else null 
end extreme_day
from weather)

select id, city, temperature, day from cte where extreme_day = 'YES'-- dump all the days which are extreme weather set of 3 days;


/*--------------------------------------------------------------------------*/
/*8. From the following 3 tables (event_category, physician_speciality, patient_treatment), write a SQL query to 
get the histogram of specialties of the unique physicians who have done the procedures but never did prescribe anything.
Table Name: EVENT_CATEGORY, PHYSICIAN_SPECIALITY, PATIENT_TREATMENT
Approach: Using the patient treatment and event category table, identify all the physicians who have done 
“Prescription”. Have this recorded in a sub query. 
Then in the main query join the patient treatment, event category and physician speciality table to identify all 
the physician who have done “Procedure”. From these physicians, remove those physicians you got from sub query to 
return the physicians who have done Procedure but never did Prescription.*/

create table EVENT_CATEGORY (event_name varchar(50), category varchar(100));

insert into EVENT_CATEGORY values ('Chemotherapy','Procedure');
insert into EVENT_CATEGORY values ('Radiation','Procedure');
insert into EVENT_CATEGORY values ('Immunosuppressants','Prescription');
insert into EVENT_CATEGORY values ('BTKI','Prescription');
insert into EVENT_CATEGORY values ('Biopsy','Test');

create table PHYSICIAN_SPECIALITY (physician_id int, speciality varchar(50));

insert into PHYSICIAN_SPECIALITY values (1000,'Radiologist');
insert into PHYSICIAN_SPECIALITY values (2000,'Oncologist');
insert into PHYSICIAN_SPECIALITY values (3000,'Hermatologist');
insert into PHYSICIAN_SPECIALITY values (4000,'Oncologist');
insert into PHYSICIAN_SPECIALITY values (5000,'Pathologist');
insert into PHYSICIAN_SPECIALITY values (6000,'Oncologist');

create table PATIENT_TREATMENT(patient_id int, event_name varchar(50), physician_id int);

insert into PATIENT_TREATMENT values (1,'Radiation', 1000 );
insert into PATIENT_TREATMENT values (2,'Chemotherapy', 2000 );
insert into PATIENT_TREATMENT values (1,'Biopsy', 1000 );
insert into PATIENT_TREATMENT values (3,'Immunosuppressants', 2000 );
insert into PATIENT_TREATMENT values (4,'BTKI' ,3000 );
insert into PATIENT_TREATMENT values (5,'Radiation', 4000 );
insert into PATIENT_TREATMENT values (4,'Chemotherapy', 2000 );
insert into PATIENT_TREATMENT values (1,'Biopsy', 5000 );
insert into PATIENT_TREATMENT values (6,'Chemotherapy', 6000 );

select * from EVENT_CATEGORY;
select * from PHYSICIAN_SPECIALITY;
select * from PATIENT_TREATMENT;

TBD: 
select * from PHYSICIAN_SPECIALITY PS
join PATIENT_TREATMENT PT on PS.physician_id = PT.physician_id
join EVENT_CATEGORY EC on PT.event_name = EC.event_name
and EC.category =  'Procedure';

select * from PHYSICIAN_SPECIALITY PS
join PATIENT_TREATMENT PT on PS.physician_id = PT.physician_id
join EVENT_CATEGORY EC on PT.event_name = EC.event_name;
-- we need to eliminate doctor 2000 as he has done both precedure and prescription 

/*--------------------------------------------------------------------------*/


/*9. Find the top 2 accounts with the maximum number of unique patients on a monthly basis.
Note: Prefer the account id with the least value in case of same number of unique patients*/ 

create table PATIENT_LOGS (account_id int, treatment_date date, patient_id int);

insert into PATIENT_LOGS values (1,'2020-01-02',100);
insert into PATIENT_LOGS values (1,'2020-01-27',200);
insert into PATIENT_LOGS values (2,'2020-01-01',300);
insert into PATIENT_LOGS values (2,'2020-01-21',400);
insert into PATIENT_LOGS values (2,'2020-01-21',300);
insert into PATIENT_LOGS values (2,'2020-01-01',500);
insert into PATIENT_LOGS values (3,'2020-01-20',400);
insert into PATIENT_LOGS values (1,'2020-03-04',500);
insert into PATIENT_LOGS values (3,'2020-01-20',450);

select *,treatment_date from PATIENT_LOGS;

select mnth, account_id, cnt  from 
(select X.account_id, X.mnth,  count(X.patient_id) cnt, RANK() over (partition by mnth order by count(X.patient_id) desc, account_id ) rnk 
from 
(select  account_id, MONTH(treatment_date) mnth,  patient_id 
from PATIENT_LOGS
group by MONTH(treatment_date), account_id, patient_id )
X group by account_id, mnth ) Z
where rnk <=2 order by mnth, account_id desc 

/*--------------------------------------------------------------------------*/

/*10. SQL Query to fetch “N” consecutive records from a table based on a certain condition
Note: Write separate queries to satisfy following scenarios:
10a. when the table has a primary key*/

create table WEATHER1 (ID int Primary Key, city varchar(50), temp int, recorded_day date);
insert into WEATHER1 values (1, 'LONDON',-1,'2021-01-01');
insert into WEATHER1 values (2, 'LONDON',-2,'2021-01-02');
insert into WEATHER1 values (3, 'LONDON',4,'2021-01-03');
insert into WEATHER1 values (4, 'LONDON',1,'2021-01-04');
insert into WEATHER1 values (5, 'LONDON',-2,'2021-01-05');
insert into WEATHER1 values (6, 'LONDON',-5,'2021-01-06');
insert into WEATHER1 values (7, 'LONDON',-7,'2021-01-07');
insert into WEATHER1 values (8, 'LONDON',5,'2021-01-08');
insert into WEATHER1 values (9, 'LONDON',-20,'2021-01-09');
insert into WEATHER1 values (10, 'LONDON',20,'2021-01-10');
insert into WEATHER1 values (11, 'LONDON',22,'2021-01-11');
insert into WEATHER1 values (12, 'LONDON',-1,'2021-01-12');
insert into WEATHER1 values (13, 'LONDON',-2,'2021-01-13');
insert into WEATHER1 values (14, 'LONDON',-2,'2021-01-14');
insert into WEATHER1 values (15, 'LONDON',-4,'2021-01-15');
insert into WEATHER1 values (16, 'LONDON',-9,'2021-01-16');
insert into WEATHER1 values (17, 'LONDON',0,'2021-01-17');
insert into WEATHER1 values (18, 'LONDON',-10,'2021-01-18');
insert into WEATHER1 values (19, 'LONDON',-11,'2021-01-19');
insert into WEATHER1 values (20, 'LONDON',-12,'2021-01-20');
insert into WEATHER1 values (21, 'LONDON',-11,'2021-01-21');

select * from WEATHER1;

/*EXPECTED O/P: 
12 LONDDON -1 2021-01-12
13 LONDDON -2 2021-01-13
14 LONDDON -2 2021-01-14
15 LONDDON -4 2021-01-15
16 LONDDON -9 2021-01-16

*/
/* 
1) we need to eliminate the days where temp is > 0 and consider only <0 records
	select * from WEATHER1 where temp <0;
2) assign a row muner for each record in the table order by id since id is a primary key and in sequence
	select *,ROW_NUMBER() over (order by id)  from WEATHER1 where temp <0
3) the difference between consecutive days of id and row_number will remain same as ids are in sequence 
	select *,id - ROW_NUMBER() over (order by id)  from WEATHER1 	where temp <0
4) put the above data in a subquery 
4) now partition the records by number of difference of id and row_number count and give an alian like cnt 
	
5) now fetch cnt = N based on N value 
*/

with T11 as 
	(select *,id - ROW_NUMBER() over (order by id) difference from WEATHER1 
	where temp <0),
	T12 as 
	(select *, count(*) over (partition by difference order by difference ) cnt from T11)
select id, city, temp, recorded_day from T12
where cnt = 4;

with
	t1 as
		(select *,	id - row_number() over (order by id) as diff
		from weather1 w
		where w.temp < 0),
	t2 as
		(select *,
		count(*) over (partition by diff order by diff) as cnt
		from t1)
select id, city, temp, recorded_day
from t2
where t2.cnt = 5;

/*10b. When table does not have a primary key*/
/* 
1) Lets create view without id column and only non-zero records 
		create view weather_vw as select city, temp from WEATHER1
2) Now that the view doesnt have id/PK column, create a subquery with clause add a row_num column, it will work as id
3) proceed as 10.a

*/
create view weather_vw as select city, temp from WEATHER1;

select * from weather_vw;

with
	w as
		(select *, row_number() over (order by city) as id
		from weather_vw),
	t1 as
		(select *,	id - row_number() over (order by id) as diff
		from w
		where w.temp < 0),
	t2 as
		(select *,
		count(*) over (partition by diff order by diff) as cnt
		from t1)
select city, temp, id, cnt
from t2
where t2.cnt = 5;



/*10c. Query logic based on data field*/
create table ORDERS (order_id varchar(20) primary key, order_date date);
insert into ORDERS values('ORD1001','2021-01-01');
insert into ORDERS values('ORD1002','2021-02-01');
insert into ORDERS values('ORD1003','2021-02-02');
insert into ORDERS values('ORD1004','2021-02-03');
insert into ORDERS values('ORD1005','2021-03-01');
insert into ORDERS values('ORD1006','2021-06-01');
insert into ORDERS values('ORD1007','2021-12-25');
insert into ORDERS values('ORD1008','2021-12-26');

/*Expected O/P
ORD_1002	2021-02-01
ORD_1003	2021-02-02
ORD_1004	2021-02-03 */

/* 1) since the data doesnt have an id column, lets add one by using Row_num function, and put it in an alias
		select *, ROW_NUMBER () over (order by ORDER_ID) id from ORDERS
	2) Now, subtract the ROW_NUM function from order_date to get a unique difference like we did in previous queries.
		(select *, ROW_NUMBER () over (order by ORDER_ID) id, DATEADD(day,-ROW_NUMBER () over (order by ORDER_ID),ORDER_DATE) difference from ORDERS)
	3) create a count based on each unique partition in another subquery
	4) finally fetch the records based on count X
*/
select * from orders;

with 
	a1 as 
		(select *, ROW_NUMBER () over (order by ORDER_ID) id, DATEADD(day,-ROW_NUMBER () over (order by ORDER_ID),ORDER_DATE) difference from ORDERS),
	a2 as 
		(select *, count(order_id) over (partition by difference) cnt from a1 )
	select * from a2
	where cnt = 3;

/*---------------alternate approach--------------------*/
select ORDER_ID, ORDER_DATE FROM 
(select ORDER_ID, ORDER_DATE,
case when DATEDIFF(DAY, ORDER_DATE,LEAD(ORDER_DATE) OVER (ORDER BY ORDER_DATE)) = 1 
	then 'YES'
	when DATEDIFF(DAY, ORDER_DATE,LAG(ORDER_DATE) OVER (ORDER BY ORDER_DATE)) = -1 
	then 'YES'
	else 'NO'
end cont_days
from ORDERS) X 
where cont_days = 'YES'; --works for all the consecutive days 

/*--------------------------------------------------------------------------*/
/*--------------------------Window functions--------------------------------*/
select * from employee;

--display max sal by each dept
select dept_name, max(salary) max_sal from employee group by dept_name;
--here we didnt display the rest of the values... in case we need to show the max sal for each record, 
--thats when window functions come into picture. see example below. 
select *, max(salary) over (partition by dept_name) from employee;
--there will be partitions created based on the column specified (in this case its dept_name) 
--and aggregate function(in this case its max function) will be executed on each partition 

--row_num, rank, dense_rank, lead, lag 
--are functions, which just assign a value for each record which has been detected/identified by the arguments 
--mentioned in over clause, thats why we dont pass any argument inside the function name unline aggregate functions.

select *, ROW_NUMBER() over (order by emp_id) rownum from employee; --order by is mandatory in row_number function in sql server, 
--in this case it can be used as a PK to uniquely identify every record in the table. 

--we can create windows for each partition and then given row_numbers as well 
select *, ROW_NUMBER() over (partition by dept_name order by emp_id) rownum from employee;

--lets say use case where they need first two employees joined in each dept, here row_number is useful.
select * from 
(select *, row_number() over (partition by dept_name order by emp_id) rownum from employee ) x
where x.rownum < 3;

--RANK ; duplicate values will have same rank and next number will be skipped. 
--Fetch top 3 sal in each dept 
select *, rank() over (partition by dept_name order by salary desc) ranks from employee; -- will assign ranks to 
--each employee based on salary, we just need to pick top 3 salaries from above 

select * from 
(select *, rank() over (partition by dept_name order by salary desc) ranks from employee) y
where y.ranks <=3;

--similarly faq is find nth max salary from table, lets see how we can build it below.
select * from 
(select *, rank() over (order by salary desc) ranks from employee) y
where y.ranks = 15; -- here 4 can be replaced by any rank within table 

--dense_rank... same as rank but when duplicate values encountered, next rank will not be skipped... 
--lets see all rank, dense_rank, and row_number in one example 
--you may observe the difference at records with salary 2000 below. 

select *, 
rank() over (order by salary desc) ranks,
dense_rank() over (order by salary desc) dense,
row_number() over (order by salary desc) rownum 
from employee;

--lead and lag
--sal of current employee is higher/lower than next/prev employee
--LEAD: will always have last record null, it has 4 arguments
--		1) on which column the function need to perform 
--		2) what is the skip value... by default 1, e.g: if we give 2, it will compare the following second record.
--		3) default value to replace the last record
--	    4) over function in general to define windows and orders 
select *, lead(salary,1,9999) over (order by emp_id) next_emp_sal from employee;
--similarly check per dept by creating paritions 
select *, lead(salary) over (partition by dept_name order by emp_id) next_emp_sal from employee;

--lag is also similar but as name suggest it will check with previous record and display in window...
select *, lag(salary) over (partition by dept_name order by emp_id) next_emp_sal from employee;

--lets see how we can display some meaningful summary based on lead, lag for salary comparision 

select *, 
case 
	when salary < lead(salary) over (partition by dept_name order by emp_id)  
	then 'Lower Salary than next employee'
	when salary > lead(salary) over (partition by dept_name order by emp_id)  
	then 'Higher Salary than next employee'
	when salary = lead(salary) over (partition by dept_name order by emp_id)  
	then 'Equal Salary as next employee'
else NULL 
end next_emp_sal 
from employee;
/*--------------------------------------------------------------------------*/
/* Windows functions advanced topics */

CREATE TABLE product
( 
    product_category varchar(255),
    brand varchar(255),
    product_name varchar(255),
    price int
);

INSERT INTO product VALUES
('Phone', 'Apple', 'iPhone 12 Pro Max', 1300),
('Phone', 'Apple', 'iPhone 12 Pro', 1100),
('Phone', 'Apple', 'iPhone 12', 1000),
('Phone', 'Samsung', 'Galaxy Z Fold 3', 1800),
('Phone', 'Samsung', 'Galaxy Z Flip 3', 1000),
('Phone', 'Samsung', 'Galaxy Note 20', 1200),
('Phone', 'Samsung', 'Galaxy S21', 1000),
('Phone', 'OnePlus', 'OnePlus Nord', 300),
('Phone', 'OnePlus', 'OnePlus 9', 800),
('Phone', 'Google', 'Pixel 5', 600),
('Laptop', 'Apple', 'MacBook Pro 13', 2000),
('Laptop', 'Apple', 'MacBook Air', 1200),
('Laptop', 'Microsoft', 'Surface Laptop 4', 2100),
('Laptop', 'Dell', 'XPS 13', 2000),
('Laptop', 'Dell', 'XPS 15', 2300),
('Laptop', 'Dell', 'XPS 17', 2500),
('Earphone', 'Apple', 'AirPods Pro', 280),
('Earphone', 'Samsung', 'Galaxy Buds Pro', 220),
('Earphone', 'Samsung', 'Galaxy Buds Live', 170),
('Earphone', 'Sony', 'WF-1000XM4', 250),
('Headphone', 'Sony', 'WH-1000XM4', 400),
('Headphone', 'Apple', 'AirPods Max', 550),
('Headphone', 'Microsoft', 'Surface Headphones 2', 250),
('Smartwatch', 'Apple', 'Apple Watch Series 6', 1000),
('Smartwatch', 'Apple', 'Apple Watch SE', 400),
('Smartwatch', 'Samsung', 'Galaxy Watch 4', 600),
('Smartwatch', 'OnePlus', 'OnePlus Watch', 220);

--FIRST_VALUE : function extracts very  first record value from a partition mentioned in the function. 
--E.g: write a query to display the most expensive product under each category (corresponding to each record). 

select *,
first_value(product_name) over (partition by product_category order by price desc) most_exp_prod
from product;

--LAST VALUE: function extracts very last record value from a partition mentioned in the function. 
--write a query to display the least expensive product under each category (corresponding to each record). 

select *,
last_value(product_name) over (partition by product_category order by price desc) least_exp_prod
from product;
/*writing the query like first_value is not going to help here .... because of frame clause 
FRAME Clause: when data is divided into partition, when controller read data in each partition, it treats them in frames.
each frame can be defined by combination of considering from first record in the partition to end of the last record
in the parition. Then on that frame entire last_value function will be applied. 
condition to built tha frame is by using "range between unbounded preceding and unbounded following", this will tell controller 
that use the entire partition from first record to last.
defaule behavior condition is "range between unbounded preceeding and current row following"... in our result set, since we 
didnt mention any condition inside last_value over clause, it has taken default and as every new record is being added 
into the frame, it is showing new least_exp_prod.
We can change keyword from 'range' to 'row', which will give different results when duplicate values present in data. 
Instead of unbounded, we can give numeric value, and controller will consider only those number of records. 
Lets see below with range condition to tell the FRAME to use entire parition
*/

select *,
last_value(product_name) over (partition by product_category order by price desc
range between unbounded preceding and unbounded following) least_exp_prod
from product;

--lets display both most expensive and least expensive in same query 

select *,
first_value(product_name) over (partition by product_category order by price desc) most_exp_prod,
last_value(product_name) over (partition by product_category order by price desc
range between unbounded preceding and unbounded following) least_exp_prod
from product;

--here if we are using same OVER() function multiple times in a query, it can be shorted by below alternate approach 

select *,
first_value(product_name) over W most_exp_prod,
last_value(product_name) over W least_exp_prod
from product
window W as (partition by product_category order by price desc
range between unbounded preceding and unbounded following) ;

--another alternate approach to get the results using just FIRST_VALUE 
select *,
first_value(product_name) over (partition by product_category order by price desc) most_exp_prod,
first_value(product_name) over (partition by product_category order by price ) least_exp_prod
from product;

--NTH_Value: Similar to FIRST and LAST Value, will result Nth value in the partition/table
--second most expensive product 
--in sql server its not there, and nth_value also depends on frame clause 
select *,
first_value(product_name) over W most_exp_prod,
last_value(product_name) over W least_exp_prod,
nth_value(product_name, 2) over W second_most_exp_product
from product
window W as (partition by product_category order by price desc
range between unbounded preceding and unbounded following) ;

--NTILE: used to group data in certain partition and treat it as a bucket based on single numric argument we pass; 
--mostlikely SQL will create equal number of buckets, if not will distribute rows to one bucket at a time.
--write a query to categorize phones in expensive, mid-range and cheper phones buckets
select * ,
NTILE(3)  OVER (order by price )
from product ;

with CTE as 
	(select * ,
	NTILE(3)  OVER (order by price ) TILE
	from product)
	select *, 
	case 
	when TILE = 1 then 'cheper phone'
	when TILE = 2 then 'mid range phone'
	when TILE = 3 then 'expensive phone'
	end phone_Category
	from CTE 
	where product_category='Phone';

/*CUME_DIST: (cumulative distribution) 
 value --> 1 <= CUME_DIST >0 
 FORMULA = current rownum (or rownum with value same as current row num) /Total num of rows 
 basically if each row position will be divided by total number of rows.*/

 --Query to fetch all records which constitutes first 30% of table based on price 
 with X as 
 (select *,
 CUME_DIST() over (order by price desc) cum_dist,  -- will display in fractions, we need to convert into numeric by below
 round(CUME_DIST() over (order by price desc)*100, 2) cum_dist_percentage
 from product ) 
 select product_name, concat(cum_dist_percentage,'%' )
 from X 
 where cum_dist_percentage <= 30 ;

 /*PERCENT_RANK (relative rank of the current row/percentage ranking)
 value --> 1 <= PERCENT_RANK > 0 
 FORMULA: Current row num -1 / Total number of rows -1 
 */
 --Query to find out how much percentage more expensive is 'Galaxy Z fold 3' when compared to all other products 

 WITH K as 
 (select *,
 PERCENT_RANK() over (order by price ) percent_rank, -- this displays in fractions, we need to convert to numbers 
 round(PERCENT_RANK() over (order by price )*100, 2) percent_rank_num
 from product) 
 select percent_rank_num from K where product_name = 'Galaxy Z Fold 3';


/*--------------------------------------------------------------------------*/

/* Recursive Queries 
Syntax: 
with [Recursive] --recursive key word is optional in some of the databases 
	CTE_NAME as 
	(
	select  query -- this is non recursive query or base query 
	union [all] -- union all is optional in some of the databases 
	select query (recursive query using CTE_NAME [with a termination condition])
	)
select * from CTE_NAME 
*/
--Q1. Return numbers 1 to 10 without using any built in functions

WITH 
	CTE AS 
		( select 1 num 
		  union all
		  select num+1 from CTE 
		  where num < 10
		)
	select * from CTE;

--Q2. Find the hierarchy of employees under a given manager 

create table emp_details (id int primary key, emp_name varchar(20), manager_id int, salary int, designation varchar(20));

insert into emp_details values (1, 'Shripadh', NULL , 10000, 'CEO');
insert into emp_details values (2, 'Satya', 5 , 1400, 'Software Engineer');
insert into emp_details values (3, 'Jia', 5 , 500, 'Data Analyst');
insert into emp_details values (4, 'David', 5 , 1800, 'Data Scientist');
insert into emp_details values (5, 'Michael', 7 , 3000, 'Manager');
insert into emp_details values (6, 'Arvind', 7 , 2400, 'Architect');
insert into emp_details values (7, 'Asha', 1 , 4200, 'CTO');
insert into emp_details values (8, 'Maryam', 1 , 3500, 'Manager');
insert into emp_details values (9, 'Reshma', 8 , 2000, 'Business Analyst');
insert into emp_details values (10, 'Akshay', 8 , 2500, 'Java Developer');

select * from emp_details 
where manager_id = 7;

with rec_manager_emp as 
	(select id, emp_name, manager_id, designation,1 lvl from emp_details  where emp_name = 'Asha'
	union all 
	select E.id, E.emp_name, E.manager_id, E.designation, H.lvl+1 from rec_manager_emp H 
	join emp_details E
	on H.id = E.manager_id)
	
	select * from rec_manager_emp; 

--Q3. Find the hierarchy of managers for a given employee 

with rec_emp_manger as 
	(select id, emp_name, manager_id, designation, 1 lvl from emp_details where emp_name = 'David' 
	union all 
	select E.id, E.emp_name, E.manager_id, E.designation, H.lvl+1 from rec_emp_manger H
	join emp_details e 
	on H.manager_id = e.id)

	select H2.emp_name EMP_NAME, E2.EMP_NAME MANAGER_NAME, H2.DESIGNATION, H2.LVL  from rec_emp_manger H2
	join emp_details E2 on 
	E2.id = H2.manager_id;

/*--------------------------------------------------------------------------*/

/*Pivoting rows to columns*/ 

create table sales_data (sales_date date, customer_id varchar(10), amount varchar(10));

insert into sales_data values ('1-Jan-21','Cust-1','50$');
insert into sales_data values ('2-Jan-21','Cust-1','50$');
insert into sales_data values ('3-Jan-21','Cust-1','50$');
insert into sales_data values ('1-Jan-21','Cust-2','100$');
insert into sales_data values ('2-Jan-21','Cust-2','100$');
insert into sales_data values ('3-Jan-21','Cust-2','100$');
insert into sales_data values ('1-Feb-21','Cust-2','-100$');
insert into sales_data values ('2-Feb-21','Cust-2','-100$');
insert into sales_data values ('3-Feb-21','Cust-2','-100$');
insert into sales_data values ('1-Mar-21','Cust-3','1$');
insert into sales_data values ('1-Apr-21','Cust-3','1$');
insert into sales_data values ('1-May-21','Cust-3','1$');
insert into sales_data values ('1-Jun-21','Cust-3','1$');
insert into sales_data values ('1-Jul-21','Cust-3','-1$');
insert into sales_data values ('1-Aug-21','Cust-3','-1$');
insert into sales_data values ('1-Sep-21','Cust-3','-1$');
insert into sales_data values ('1-Oct-21','Cust-3','-1$');
insert into sales_data values ('1-Nov-21','Cust-3','-1$');
insert into sales_data values ('1-Dec-21','Cust-3','-1$');

/* Expected o/p: Negative values are surrounded by () 
Customer	Jan-21	Feb-21	Mar-21	Apr-21	May-21	Jun-21	Jul-21	Aug-21	Sep-21	Oct-21	Nov-21	Dec-21	Total
Cust-1	150$	0$	0$	0$	0$	0$	0$	0$	0$	0$	0$	0$	150$
Cust-2	300$	(300)$	0$	0$	0$	0$	0$	0$	0$	0$	0$	0$	0$
Cust-3	0$	0$	1$	1$	1$	1$	(1)$	(1)$	(1)$	(1)$	(1)$	(1)$	(2)$
Total	450$	(300)$	1$	1$	1$	1$	(1)$	(1)$	(1)$	(1)$	(1)$	(1)$	
*/ 

select * from sales_data ;

/*Syntax

select * from 
	( base query) 
pivot 
	(aggregate function 
	 columns values to be selected --(in this case its like "Jan-21", "Feb-21", "Mar-21", ...etc)
	 )
--base query should have at least 3 columns, 1st column is an unique identifies like different customers in this case, treated as row
--2nd column shold provide all the values/column names that we want to display 
--3rd column should be a value that we want to put in each row and column 
--any additional columns will be more or less hard coded same for all values 
*/

-- Lets capture the data first as expected format, like only mon-yy and no $ symbol 

		select customer_id  as Customer,
		FORMAT(sales_date, 'MMM-yy') as sales_date,
		replace(amount,'$','') as amount 
		from sales_data;

	--base query is ready, put it in syntax 
	with pivot_data as 
	(
			select * from 
				(select customer_id  as Customer,
				FORMAT(sales_date, 'MMM-yy') as sales_date,
				cast(replace(amount,'$','') as int) as amount 
				from sales_data) as sales_data --(since sql server needs alias for a subquery
			pivot 
				(--aggregate function :here we want to sum the amount so
					sum(amount)
				 --for columns values to be selected --(in this case its like "Jan-21", "Feb-21", "Mar-21", ...etc)
					for sales_date in ( [Jan-21],[Feb-21],[Mar-21],[Apr-21],[May-21],[Jun-21],
								[Jul-21],[Aug-21],[Sep-21],[Oct-21],[Nov-21],[Dec-21] )
				 ) as pivot_table 

			-- at this point we need to build the same data for TOTAL record so join the above data with additional data by union
			UNION 

			select * from 
				(select 'Total'  as Customer,
				FORMAT(sales_date, 'MMM-yy') as sales_date,
				cast(replace(amount,'$','') as int) as amount 
				from sales_data) as sales_data --(since sql server needs alias for a subquery
			pivot 
				(--aggregate function :here we want to sum the amount so
					sum(amount)
				 --for columns values to be selected --(in this case its like "Jan-21", "Feb-21", "Mar-21", ...etc)
					for sales_date in ( [Jan-21],[Feb-21],[Mar-21],[Apr-21],[May-21],[Jun-21],
								[Jul-21],[Aug-21],[Sep-21],[Oct-21],[Nov-21],[Dec-21] )
				 ) as pivot_table 
		),
		final_data as 
		(
		select customer, 
		coalesce([Jan-21],0) as 'Jan-21',
		coalesce([Feb-21],0) as 'Feb-21',
		coalesce([Mar-21],0) as 'Mar-21',
		coalesce([Apr-21],0) as 'Apr-21',
		coalesce([May-21],0) as 'May-21',
		coalesce([Jun-21],0) as 'Jun-21',
		coalesce([Jul-21],0) as 'Jul-21',
		coalesce([Aug-21],0) as 'Aug-21',
		coalesce([Sep-21],0) as 'Sep-21',
		coalesce([Oct-21],0) as 'Oct-21',
		coalesce([Nov-21],0) as 'Nov-21',
		coalesce([Dec-21],0) as 'Dec-21'
		from  pivot_data 
				)
		select customer, 
		case when [Jan-21]  < 0 then concat('(',[Jan-21]*-1,')$') else concat ([Jan-21],'$') end as 'Jan-21',
		case when [Feb-21]  < 0 then concat('(',[Feb-21]*-1,')$') else concat ([Feb-21],'$') end as 'Feb-21',
		case when [Mar-21]  < 0 then concat('(',[Mar-21]*-1,')$') else concat ([Mar-21],'$') end as 'Mar-21',
		case when [Apr-21]  < 0 then concat('(',[Apr-21]*-1,')$') else concat ([Apr-21],'$') end as 'Apr-21',
		case when [May-21]  < 0 then concat('(',[May-21]*-1,')$') else concat ([May-21],'$') end as 'May-21',
		case when [Jun-21]  < 0 then concat('(',[Jun-21]*-1,')$') else concat ([Jun-21],'$') end as 'Jun-21',
		case when [Jul-21]  < 0 then concat('(',[Jul-21]*-1,')$') else concat ([Jul-21],'$') end as 'Jul-21',
		case when [Aug-21]  < 0 then concat('(',[Aug-21]*-1,')$') else concat ([Aug-21],'$') end as 'Aug-21',
		case when [Sep-21]  < 0 then concat('(',[Sep-21]*-1,')$') else concat ([Sep-21],'$') end as 'Sep-21',
		case when [Oct-21]  < 0 then concat('(',[Oct-21]*-1,')$') else concat ([Oct-21],'$') end as 'Oct-21',
		case when [Nov-21]  < 0 then concat('(',[Nov-21]*-1,')$') else concat ([Nov-21],'$') end as 'Nov-21',
		case when [Dec-21]  < 0 then concat('(',[Dec-21]*-1,')$') else concat ([Dec-21],'$') end as 'Dec-21',
		case when customer = 'Total' then ''
			else case when [Jan-21]+[Feb-21]+[Mar-21]+[Apr-21]+[May-21]+[Jun-21]+[Jul-21]+[Aug-21]+[Sep-21]+[Oct-21]+[Nov-21]+[Dec-21] < 0 
					  then CONCAT('(',	([Jan-21]+[Feb-21]+[Mar-21]+[Apr-21]+[May-21]+[Jun-21]+[Jul-21]+[Aug-21]+[Sep-21]+[Oct-21]+[Nov-21]+[Dec-21])*-1 ,')$')
					  else 
							CONCAT([Jan-21]+[Feb-21]+[Mar-21]+[Apr-21]+[May-21]+[Jun-21]+[Jul-21]+[Aug-21]+[Sep-21]+[Oct-21]+[Nov-21]+[Dec-21],'$')
							end 
		end as 'Total'
		from final_data ;

--now we need to remove nulls and treat them as 0s, it can by done by coalesce in sql server; we need to build it 
--from existing result set so, lets give it an alias name inside with clause now. 

--now we need to come up with Total column and add $, and () for -ve values; this can be done in final_data extraction itself. 


/*--------------------------------------------------------------------------*/

/*Further Pivot Syntax: 

SELECT column_list
FROM (table_expression ) alias 
  PIVOT
  (
    aggregate_function(aggregate_column)
    FOR pivot_column
    IN( pivot_column_values )
  ) [AS] pivot_table_alias
[ORDER BY column_list];
*/

CREATE TABLE BookSales
(BookType VARCHAR(20), SalesYear INT, Sales INT);


INSERT INTO BookSales VALUES('Fiction', 2014, 11201);
INSERT INTO BookSales VALUES('Fiction', 2014, 12939);
INSERT INTO BookSales VALUES('Fiction', 2013, 10436);
INSERT INTO BookSales VALUES('Fiction', 2013, 9346);
INSERT INTO BookSales VALUES('Nonfiction', 2014, 7214);
INSERT INTO BookSales VALUES('Nonfiction', 2014, 5800);
INSERT INTO BookSales VALUES('Nonfiction', 2013, 8922);
INSERT INTO BookSales VALUES('Nonfiction', 2013, 7462);

select * from BookSales;

select * from (
select BookType, 
	SalesYear,
	Sales
	From BookSales) as book_sales
pivot 
(
	sum(Sales)
	for SalesYear in ([2013], [2014])
) as pivot_table 

--trying with case statement, and trying to print output like above example 

with base_query as --there is no need to build base query, but as a standard practice doing it. 
		(select BookType, 
			SalesYear,
			Sales
			From BookSales),
	final_query   as 
		(select BookType, 
		sum(case when SalesYear = 2014 then Sales else 0 end) '2014',
		sum(case when SalesYear = 2013 then Sales else 0 end) '2013'
		--sum(Sales) as 'Total'
		from base_query 
		group by BookType 
		Union 
		select 'Total' as BookType,
		sum(case when SalesYear = 2014 then Sales else 0 end) '2014',
		sum(case when SalesYear = 2013 then Sales else 0 end) '2013'
		--'' as 'Total'
		from base_query )
select 
BookType, [2014], [2013]
,case when BookType = 'Total' then ''  else (concat('',[2014]+[2013])) end as 'Total'
from final_query;



/*--------------------------------------------------------------------------*/
/* working on dupilcate data removel */

create table cars (id int, model varchar(20), brand varchar(20), color varchar(20), make int);

insert into cars values (1, 'Model S', 'Tesla', 'Blue', 2018),
(2, 'EQS', 'Mercedes-Benz', 'Black', 2022),
(3, 'iX', 'BMW', 'Red', 2022),
(4, 'ioniq 5', 'Hyundai', 'White', 2021),
(5, 'Model S', 'Tesla', 'Silver', 2018),
(6, 'ioniq 5', 'Hyundai', 'Green', 2021);

select * from cars order by model, brand;

/* Scenario-1: Data duplicated based on SOME of the columns , 
write a query to delete duplicate data from cars table.
duplicate record is identified based on model and brand 
*/
--> Solution 1:- Delete using unique identifier 
delete 
--select *
from cars where id in (
select max(id) from cars group by model, brand having count(*) > 1);

--> Solution 2:- Using Self join 
delete 
--select * 
from cars where id in (
select c2.id from cars c1 join cars c2  on c1.model = c2.model and c1.brand = c2.brand and c1.id<c2.id)

--> Solution 3:- Window Function 

delete
--select * 
from cars where id in (select id from (
select  *, row_number() over (partition by model, brand order by make) rn from cars ) x where x.rn>1);
 
--> Solution 4:- Using Min function-- this even deletes multiple records 

 delete 
--select *
from cars where id not in (
select min(id) from cars group by model, brand );


--> Solution 5:- Using Backup Table , not very effective for prod tables, table availabitlity and permissions may be lost

create table cars_backup from 
	select * from cars where id in (select min(id) from cars group by model, brand ));

--drop table cars ;

alter table rename cars_backup rename to cars; 

 --> Solution 6:- Using backup table, without dropping actual table, same as above, not very effective. 

create table cars_backup from 
	select * from cars where id in (select min(id) from cars group by model, brand ));

truncate table cars;

insert into cars select * from cars_backup ;

/*Scenario -2: Data is duplicated based on all columns 
write a query to delete a duplicate entry for a car in cars table */

insert into cars values (1, 'Model S', 'Tesla', 'Blue', 2018),
(4, 'ioniq 5', 'Hyundai', 'White', 2021) ;

select * from cars order by id;
--> Solution 1:- Delete using CTID 

select *, rowid from cars; 
delete from cars where rowid in (select max(rowid) from cars group by model, brand having count(*)>1);
--this is similar to delete using MIN fn or unique id, only difference is that rowid is specific to Oracle, 
--and CTID can be used in postgre sql, but no such column in SQLServer and MYSQL. Solution-2 will work across DBs. 

--> Solution 2:- By creating temporary unique id column 
alter table cars add row_num int IDENTITY (1,1); --for sql server 
--alter table cars add column row_num int generated always as IDENTITY; for other dbs

select * from cars;

delete from cars 
where row_num in (
select max(row_num) from 
cars group by model, brand having count(row_num)> 1
);

--dropping the additionally created column after delete 
alter table cars drop column row_num; 

--> Solution 3:- by creating a backup table 

create table cars_bkp as 
select distinct * from cars;

drop cars;

alter table rename cars_bkp to cars ;

--> Solution 4:- by creating a backup table but not dropping the original table 

create table cars_bkp as 
select distinct * from cars;

truncate table cars;

insert into cars select * from cars_bkp;

drop table cars_bkp;

/*--------------------------------------------------------------------------*/

/* find actual distance each car travelled corresponding to each day */
create table cars_distance (cars varchar(10), days varchar(10), cumulative_distance int);

insert into cars_distance values ('car1','day1',50), 
('car1','day2',100), 
('car1','day3',200),
('car2','day1',0),
('car3','day1',0),
('car3','day2',50),
('car3','day3',50),
('car3','day4',100);

/* Expected O/P: 
cars days cumulative_distace actual_distance 
car1 day1 50				  50
car1 day2 100				  50
car1 day3 200				  100
car2 day1 0					  0
car3 day1 0					  0
car3 day2 50				  50
car3 day3 50				  0
car3 day4 100				  100
*/ 

select *, cumulative_distance  - lag(cumulative_distance,1,0) over(partition by cars order by days) actual_distance
from cars_distance;
/*--------------------------------------------------------------------------*/

/*input to output
display given data in below format

Source		Destination			Distance 
Bangalore	Hyderabad			400
Chennai		Pune				400
Mumbai		Delhi				400

*/ 

Create table src_dest_table (source varchar(20), destination varchar(20), distance int);

insert into src_dest_table values ('Bangalore','Hyderabad',400),
('Hyderabad','Bangalore',400),
('Chennai','Pune',400),
('Pune','Chennai',400),
('Mumbai','Delhi',400),
('Delhi','Mumbai',400);

select source, destination, distance from (
select *, ntile(2) over (ORDER BY source) route_group from src_dest_table) s 
where route_group = 1;
--here we got only one set but not exact output source and destination for Mumbai to Delhi

with cte as 
	(select *, ROW_NUMBER () over (order by distance) rn from src_dest_table) 

select a.source, a.destination, a.distance from cte as a join cte b
on a.rn < b.rn
and a.source = b.destination 
and a.destination = b.source;
/*--------------------------------------------------------------------------*/
/* ungroup the given input data 
expected output is that each item should be displayed total_count times along with its id, in separate record*/ 

create table travel_items (id int, item_name varchar(20), total_count int);


insert into travel_items values (1, 'water bottle', 2),
(2,'tent', 1), (3, 'apple', 4);
insert into travel_items values  (4, 'chairs',6);
with cte as 
(
select id, item_name, total_count,  1 iter from travel_items 
union all 
select id,item_name, total_count, iter+1 iter from cte where total_count > iter) 
select id, item_name, iter from cte order by id;


/*--------------------------------------------------------------------------*/
/* Derive IPL Matches 
There are 10 IPL teams
1) Write a query such that each team plays with every other team only once
2) Write a query such that each team plays with every other team twice */

create table ipl_teams(team_code varchar(5), team_name varchar(50));

insert into ipl_teams values ('MI', 'Mumbai Indians'),
('CSK', 'Chennai SuperKings'),
('KKR', 'Kolkatha Knight Riders'),
('SRG', 'Sunrisers Hyderabad'),
('DC', 'Delhi Capitals'),
('PBKS', 'Punjab Kings'),
('GT', 'Gujrat Titans'),
('RCB', 'Royal Challengers Bengalooru'),
('RR', 'Rajasthan Royals'),
('LSG', 'Lucknow Super Giants');

--Solution-1: one time with each other, total 45 teams 

select * from ipl_teams order by team_name;

with cte1 as 
	(select team_code, team_name, 
	row_number() over (order by team_code) rn from ipl_teams)

select concat(t1.team_name, ' Vs ', t2.team_name) matches from cte1 t1 join cte1 t2 on 
t1.rn > t2.rn
order by matches ;



--Solution-2: two times with each other, total 10 teams, so 90 mathes. 

select concat(t1.team_name, ' Vs ', t2.team_name) matches from ipl_teams t1 join ipl_teams t2 on 
t1.team_name != t2.team_name
order by matches ;

--alternate approach based on query 1 
with cte1 as 
	(select team_code, team_name, 
	row_number() over (order by team_code) rn from ipl_teams)

select concat(t1.team_name, ' Vs ', t2.team_name) matches from cte1 t1 join cte1 t2 on 
t1.rn <> t2.rn
order by matches ;
/*--------------------------------------------------------------------------*/
/*Pizza Delivery Status 
A pizza company is taking orders from customers, and each pizza ordered is added to their database as a separate order
Each order has an associated status "Created", "Submitted", or "Delivered"
An order's final status is calculated based on status as follows: 
1) When all orders of a customer have a status of "Delivered" then Final status of the customer is "Completed"
2) when a customer has some orders "Delivered" and some orders "Submitted" then final status is "WIP" 
3) when all custumers orders are "submitted" then final status is "Awaiting progress" 
4) Otherwise final status is "Awaiting Submission" 

Write a query of each customer and his final_status order by customer name 
*/
create table pizza_delivery (cust_name varchar(20), order_id varchar(10), status varchar(20));
insert into pizza_delivery values ('John','J1','DELIVERED'),
('John','J2','DELIVERED'),
('Smith','S1','SUBMITTED'),
('David','D1','SUBMITTED'),
('David','D2','DELIVERED'),
('David','D3','CREATED'),
('Krish','K1','CREATED');

select * from pizza_delivery;

select distinct cust_name, 'COMPLETED' as Final_Status from pizza_delivery T1 
where T1.status = 'DELIVERED' 
and  not exists
( select * from pizza_delivery T2 where status in ('SUBMITTED','CREATED')
and T1.cust_name = T2.cust_name)
union 
select distinct cust_name, 'IN PROGRESS' as Final_Status from pizza_delivery T1 
where T1.status = 'DELIVERED' 
and  exists 
( select * from pizza_delivery T2 where status in ('SUBMITTED','CREATED')
and T1.cust_name = T2.cust_name)
union 
select distinct cust_name, 'AWAITING PROGRESS' as Final_Status from pizza_delivery T1 
where T1.status = 'SUBMITTED' 
and  not exists
( select * from pizza_delivery T2 where status in ('DELIVERED','CREATED')
and T1.cust_name = T2.cust_name)
union
select distinct cust_name, 'AWAITING SUBMISSION' as Final_Status from pizza_delivery T1 
where T1.status = 'CREATED' 
and not exists
( select * from pizza_delivery T2 where status in ('DELIVERED','SUBMITTED')
and T1.cust_name = T2.cust_name)

/*--------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------*/