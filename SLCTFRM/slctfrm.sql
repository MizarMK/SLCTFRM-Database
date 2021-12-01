DROP DATABASE IF EXISTS `SLCTFRM`;
CREATE DATABASE IF NOT EXISTS `SLCTFRM`;
USE `SLCTFRM`;

/* DROP TABLES */
DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS parks;
DROP TABLE IF EXISTS divisions;
DROP TABLE IF EXISTS leagues;

SET NAMES utf8 ;

DROP TABLE IF EXISTS account;
SET character_set_client = utf8mb4 ;
CREATE TABLE `account`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(15) NOT NULL,
  `email` VARCHAR(30) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `favteam` VARCHAR(3),
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS people;
SET character_set_client = utf8mb4 ;
CREATE TABLE `people` (
  `personID` varchar(9) NOT NULL,
  `nameFirst` varchar(255) DEFAULT NULL,
  `nameLast` varchar(255) DEFAULT NULL,
  `nameFull` varchar(255) DEFAULT NULL,
  `birthState` varchar(255) DEFAULT NULL,
  `birthCountry` varchar(255) DEFAULT NULL,
  `birthYear` int(11) DEFAULT NULL,
  `birthMonth` int(11) DEFAULT NULL,
  `birthDay` int(11) DEFAULT NULL,
  `batter` varchar(1) DEFAULT NULL,
  `pitcher` varchar(1) DEFAULT NULL,
  `age` smallint(2) DEFAULT NULL,
  PRIMARY KEY (`personID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS team;
SET character_set_client = utf8mb4 ;
CREATE TABLE `team` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `teamID` varchar(4) NOT NULL,
  `yearID` smallint(4) DEFAULT NULL,
  `lgID` varchar(2) DEFAULT NULL,
  `franchID` varchar(3) DEFAULT NULL,
  `personID` varchar(9) DEFAULT NULL, /* TODO: FIX THE ARRAY THING */
  `GB` int(6) DEFAULT NULL,
  `divWin` varchar(1) DEFAULT NULL,
  `WCWin` varchar(1) DEFAULT NULL,
  `LGWin` varchar(1) DEFAULT NULL,
  `WSWin` varchar(1) DEFAULT NULL,
  `W` int(6) DEFAULT NULL,
  `L` int(6) DEFAULT NULL,
  `G` int(6) DEFAULT NULL,
  `parkID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `yearID` (`yearID`, `lgID`, `teamID`),
  KEY `teamID` (`teamID`),
  KEY `lgID` (`lgID`),
  KEY `franchID` (`franchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS parks;
SET character_set_client = utf8mb4 ;
CREATE TABLE `parks` (
  `parkID` varchar(9) NOT NULL,
  `parkName` varchar(255) DEFAULT NULL,
  `cityID` varchar(255) DEFAULT NULL,
  `stateID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`parkID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS divisions;
SET character_set_client = utf8mb4 ;
CREATE TABLE `divisions` (
  `divID` varchar(9) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`divID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS leagues;
SET character_set_client = utf8mb4 ;
CREATE TABLE `leagues` (
  `leagueID` varchar(2) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`leagueID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;