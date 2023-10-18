-- Creates a DATABASE hbtn_0d_usa
-- Creates a table called states

CREATE DATABASE
       IF NOT EXISTS
       `hbtn_0d_usa`;

CREATE TABLE
       IF NOT EXISTS
       `hbtn_0d_usa.states`(
       PRIMARY KEY(`id`),
       `id` INT NOT NULL AUT0_INCREMENT,
       `name` VARCHAR(256) NOT NULL);
