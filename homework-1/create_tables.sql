-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id varchar(50) PRIMARY KEY UNIQUE NOT NULL,
	company_name varchar(70) NOT NULL,
	contact_name varchar(70) NOT NULL
);

CREATE TABLE employees
(
	emoployee_id int UNIQUE NOT NULL,
	first_name text NOT NULL,
	last_name text NOT NULL,
	title text NOT NULL,
	birh_date varchar(20) NOT NULL,
	notes text
);

CREATE TABLE orders
(
	order_id int UNIQUE PRIMARY KEY NOT NULL,
	customer_id varchar(50) NOT NULL
	REFERENCES customers(customer_id),
	employee_id int NOT NULL
	REFERENCES employees(emoployee_id),
	order_date varchar(20) NOT NULL,
	ship_city text NOT NULL
);