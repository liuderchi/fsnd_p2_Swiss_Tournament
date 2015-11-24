-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- 1. create db and connect to db
-- reset DB
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

-- 2. create tables and insert data
CREATE TABLE players ( pid SERIAL primary key, name TEXT );
CREATE TABLE standings ( pid SERIAL primary key, name TEXT, wins SMALLINT, matches SMALLINT );
CREATE TABLE matches ( mid SERIAL primary key, winner TEXT, loser TEXT );

--CREATE TABLE posts ( content TEXT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, id SERIAL );
--INSERT INTO players (name) VALUES ( 'Kobe');
--INSERT INTO players (name) VALUES ( 'Paul');
--INSERT INTO matches (winner, loser) VALUES ( 'Paul','Kobe');
--INSERT INTO matches (winner, loser) VALUES ( 'Paul', 'Curry');
--INSERT INTO standings (name, wins, matches) VALUES ( 'Paul', 0, 20 );

-- 3. create views
--CREATE VIEW PlayerNamesView AS
--SELECT name FROM players;
--CREATE VIEW MatchNamesView AS
--SELECT winner, loser FROM matches;
--SELECT pid,name,wins,matches FROM standings WHERE name='Paul';

-- 4. some Application query
--SELECT loser FROM MatchNamesView;
