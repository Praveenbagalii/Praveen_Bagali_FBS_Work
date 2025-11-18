# **Assignment 01**





#### 1\. Login to MySQL and view all databases already present.





mysql> show databases;

+--------------------+

| Database           |

+--------------------+

| fake\_job\_detection |

| fbs                |

| firstbitsolution   |

| information\_schema |

| mysql              |

| performance\_schema |

| praveen            |

| sys                |

+--------------------+

8 rows in set (0.12 sec)





#### 2\. Write an SQL statement to create a simple table countries including columns

#### country\_id, country\_name and region\_id. After this display the structure of

#### table



mysql> use praveen;

Database changed

mysql> create table countries

    -> (country\_id int,

    -> country\_name varchar(20),

    -> region\_id int);

Query OK, 0 rows affected (0.08 sec)



mysql> desc countries;

+--------------+-------------+------+-----+---------+-------+

| Field        | Type        | Null | Key | Default | Extra |

+--------------+-------------+------+-----+---------+-------+

| country\_id   | int         | YES  |     | NULL    |       |

| country\_name | varchar(20) | YES  |     | NULL    |       |

| region\_id    | int         | YES  |     | NULL    |       |

+--------------+-------------+------+-----+---------+-------+

3 rows in set (0.02 sec)





#### 3\. Write an SQL statement to create a table named jobs including columns

#### job\_id, job\_title, min\_salary, max\_salary and check whether the

#### max\_salary amount exceeding the upper limit 25000. Also set job\_id as

#### primary key and entering null values for job\_title is not allowed.





mysql> CREATE TABLE jobs (

    ->     job\_id      INT PRIMARY KEY,

    ->     job\_title   VARCHAR(50) NOT NULL,

    ->     min\_salary  INT,

    ->     max\_salary  INT CHECK (max\_salary <= 25000)

    -> );

Query OK, 0 rows affected (0.22 sec)



mysql> desc jobs;

+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | int         | NO   | PRI | NULL    |       |

| job\_title  | varchar(50) | NO   |     | NULL    |       |

| min\_salary | int         | YES  |     | NULL    |       |

| max\_salary | int         | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+

4 rows in set (0.06 sec)



mysql> INSERT INTO jobs (job\_id, job\_title, min\_salary, max\_salary)

    -> VALUES (1, 'Software Developer', 15000, 24000);

Query OK, 1 row affected (0.02 sec)



mysql> table jobs;

+--------+--------------------+------------+------------+

| job\_id | job\_title          | min\_salary | max\_salary |

+--------+--------------------+------------+------------+

|      1 | Software Developer |      15000 |      24000 |

+--------+--------------------+------------+------------+

1 row in set (0.00 sec)





#### 4\. Write a SQL statement to create a table named job\_histry including columns

#### employee\_id, start\_date, end\_date, job\_id and department\_id



mysql> create table job\_histry (

    -> employee\_id int,

    -> employee\_id date,

    -> ^C

mysql> create table job\_histry (

    -> employee\_id int,

    -> start\_date date,

    -> end\_date date,

    -> job\_id int,

    -> department\_id int);

Query OK, 0 rows affected (0.04 sec)



mysql> insert into job\_histry (employee\_id, start\_date, end\_date, job\_id, department\_id)

    -> values (101, '2024-01-10', '2024-12-31', 1, 10);

Query OK, 1 row affected (0.17 sec)



mysql> table job\_histry;

+-------------+------------+------------+--------+---------------+

| employee\_id | start\_date | end\_date   | job\_id | department\_id |

+-------------+------------+------------+--------+---------------+

|         101 | 2024-01-10 | 2024-12-31 |      1 |            10 |

+-------------+------------+------------+--------+---------------+

1 row in set (0.01 sec)





#### 5\. Write an SQL statement to alter a table named countries to make sure that no

#### duplicate data against column country\_id will be allowed at the time of

#### insertion.



mysql> alter table countries

    -> add primary key (country\_id);

Query OK, 0 rows affected (0.14 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc countries;

+--------------+-------------+------+-----+---------+-------+

| Field        | Type        | Null | Key | Default | Extra |

+--------------+-------------+------+-----+---------+-------+

| country\_id   | int         | NO   | PRI | NULL    |       |

| country\_name | varchar(20) | YES  |     | NULL    |       |

| region\_id    | int         | YES  |     | NULL    |       |

+--------------+-------------+------+-----+---------+-------+

3 rows in set (0.06 sec)





#### 6\. Write an SQL statement to create a table named jobs including columns job\_id,

#### job\_title, min\_salary and max\_salary, and make sure that, the default value

#### for job\_title is blank and min\_salary is 8000 and max\_salary is NULL will be

#### entered automatically at the time of insertion if no value assigned for the

#### specified columns.



mysql> alter table jobs

    -> modify column job\_title VARCHAR(50) NOT NULL DEFAULT '',

    -> modify column min\_salary INT DEFAULT 8000,

    -> modify column max\_salary INT DEFAULT NULL;

Query OK, 0 rows affected (0.02 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> insert into jobs(job\_id) valuse(101);

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'valuse(101)' at line 1

mysql> ^C

mysql> Insert into jobs (job\_id) VALUES (101);

Query OK, 1 row affected (0.01 sec)



mysql> table jobs;

+--------+--------------------+------------+------------+

| job\_id | job\_title          | min\_salary | max\_salary |

+--------+--------------------+------------+------------+

|      1 | Software Developer |      15000 |      24000 |

|    101 |                    |       8000 |       NULL |

+--------+--------------------+------------+------------+

2 rows in set (0.00 sec)







#### 7\. Create a Department table



mysql> desc department;

+-----------------+-------------+------+-----+---------+-------+

| Field           | Type        | Null | Key | Default | Extra |

+-----------------+-------------+------+-----+---------+-------+

| Department\_id   | int         | YES  |     | NULL    |       |

| Department\_name | varchar(30) | YES  |     | NULL    |       |

| manager\_id      | int         | YES  |     | NULL    |       |

| location\_id     | int         | YES  |     | NULL    |       |

+-----------------+-------------+------+-----+---------+-------+

4 rows in set (0.03 sec)



mysql> alter table department

    -> add primary key(Department\_id,manager\_id);

Query OK, 0 rows affected (0.09 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc department;

+-----------------+-------------+------+-----+---------+-------+

| Field           | Type        | Null | Key | Default | Extra |

+-----------------+-------------+------+-----+---------+-------+

| Department\_id   | int         | NO   | PRI | NULL    |       |

| Department\_name | varchar(30) | YES  |     | NULL    |       |

| manager\_id      | int         | NO   | PRI | NULL    |       |

| location\_id     | int         | YES  |     | NULL    |       |

+-----------------+-------------+------+-----+---------+-------+

4 rows in set (0.01 sec)





#### 8\. Write an SQL statement to create a table employees including columns 

#### employee\_id, first\_name, last\_name, email, phone\_number hire\_date, job\_id, 

#### salary, commission, manager\_id and department\_id and make sure that, the 

#### employee\_id column does not contain any duplicate value at the time of 

#### insertion and the foreign key columns combined by department\_id and 

#### manager\_id columns contain only those unique combination values, which 

#### combinations are exists in the departments table.





mysql> create table employees(

&nbsp;   -> employee\_id int primary key,

&nbsp;   -> first\_name varchar(15),

&nbsp;   -> last\_name varchar(15),

&nbsp;   -> email varchar(30),

&nbsp;   -> phone\_number int,

&nbsp;   -> hire\_date date,

&nbsp;   -> job\_id int,

&nbsp;   -> salary decimal(7,2),

&nbsp;   -> commission int,

&nbsp;   -> manager\_id int,

&nbsp;   -> department\_id int)

&nbsp;   -> ;

Query OK, 0 rows affected (0.09 sec)



mysql> alter table employees

&nbsp;   -> add foreign key(employee\_id, manager\_id)

&nbsp;   -> references department(^C

mysql> alter table employees

&nbsp;   -> add foreign key( department\_id, manager\_id)

&nbsp;   -> references department(department\_id, manager\_id);

Query OK, 0 rows affected (0.11 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql>

