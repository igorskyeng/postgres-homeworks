-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customers_id varchar(100) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE employees
(
	employees_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
);

CREATE TABLE orders
(
	orders_id int PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customers_id) NOT NULL,
	employee_id int REFERENCES employees(employees_id) NOT NULL,
	order_date date,
	ship_city text
);