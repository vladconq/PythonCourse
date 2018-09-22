CREATE TABLE IF NOT EXISTS employee (
    employee_id SERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    employee_department_temp VARCHAR(255) NOT NULL,
    employee_city INTEGER REFERENCES city(city_id) NOT NULL,
    boss VARCHAR(255) NULL,
    salary DECIMAL(10, 2)
);

UPDATE db_scheme_version SET db_version = '1.3', upgraded_on = now();



