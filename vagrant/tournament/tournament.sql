-- Table definitions for the tournament project.

-- 1. create db and connect to db
-- reset DB
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

-- 2. create tables and insert data
CREATE TABLE players ( pid SERIAL primary key, name TEXT );
CREATE TABLE standings ( pid SERIAL primary key, name TEXT, wins SMALLINT, matches SMALLINT );
CREATE TABLE matches ( mid SERIAL primary key, winner TEXT, loser TEXT );
