CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

drop table if exists USAGE;
drop table if exists EMPLOYEE;
drop table if exists DEVICE;

drop type if exists brand;
drop type if exists type;
drop type if exists checking;

CREATE TYPE brand AS ENUM ('DELL', 'HP', 'SAMSUNG');
CREATE TYPE type AS ENUM ('COMPUTER', 'PHONE', 'PRINTER');
CREATE TYPE checking AS ENUM ('CHECK_IN', 'CHECK_OUT');


CREATE TABLE EMPLOYEE(
    id uuid DEFAULT uuid_generate_v4 () primary key,
    first_name varchar not null,
    last_name varchar not null,
    email varchar not null,
    code varchar unique not null
);

CREATE TABLE DEVICE(
    id uuid DEFAULT uuid_generate_v4 () primary key,
    description varchar not null,
    brand brand not null,
    type type not null,
    code varchar unique not null
);

CREATE TABLE USAGE(
    id uuid DEFAULT uuid_generate_v4 () primary key,
    date timestamp,
    employee_id uuid references EMPLOYEE(id),
    device_id uuid references DEVICE(id),
    Type checking not null
);