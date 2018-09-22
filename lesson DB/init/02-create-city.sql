CREATE TABLE IF NOT EXISTS city (
    city_id SERIAL NOT NULL PRIMARY KEY,
    city_name VARCHAR(255) NOT NULL UNIQUE
);

UPDATE db_scheme_version SET db_version = '1.1', upgraded_on = now();
