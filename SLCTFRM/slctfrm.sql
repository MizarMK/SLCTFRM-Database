DROP DATABASE IF EXISTS `SLCTFRM`;
CREATE DATABASE IF NOT EXISTS `SLCTFRM`;
USE `SLCTFRM`;

/* DROP TABLES */
DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS parks;
DROP TABLE IF EXISTS divisions;
DROP TABLE IF EXISTS leagues;
DROP TABLE IF EXISTS batting;
DROP TABLE IF EXISTS pitching;
DROP TABLE IF EXISTS appearances;

SET NAMES utf8 ;

DROP TABLE IF EXISTS account;
SET character_set_client = utf8mb4 ;
CREATE TABLE `account`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(15) NOT NULL,
  `email` VARCHAR(30) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `favteamid` VARCHAR(3),
  `favteam` VARCHAR(30),
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
  PRIMARY KEY (`personID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS teams;
SET character_set_client = utf8mb4 ;
CREATE TABLE `teams` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `teamID` varchar(4) NOT NULL,
  `yearID` smallint(4) DEFAULT NULL,
  `lgID` varchar(2) DEFAULT NULL,
  `franchID` varchar(3) DEFAULT NULL,
  `divID` varchar(3) DEFAULT NULL,
  `divWin` varchar(1) DEFAULT NULL,
  `WCWin` varchar(1) DEFAULT NULL,
  `LGWin` varchar(1) DEFAULT NULL,
  `WSWin` varchar(1) DEFAULT NULL,
  `W` int(6) DEFAULT NULL,
  `L` int(6) DEFAULT NULL,
  `G` int(6) DEFAULT NULL,
  `parkName` varchar(255) DEFAULT NULL,
  `teamName` varchar(255) DEFAULT NULL,
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
  lgID varchar(9) NOT NULL,
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

DROP TABLE IF EXISTS batting;
SET character_set_client = utf8mb4 ;
CREATE TABLE `batting` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `stint` smallint(6) NOT NULL,
  `teamID` varchar(3) DEFAULT NULL,
  `lgID` varchar(2) DEFAULT NULL,
  `G` smallint(6) DEFAULT NULL,
  `AB` smallint(6) DEFAULT NULL,
  `R` smallint(6) DEFAULT NULL,
  `H` smallint(6) DEFAULT NULL,
  `2B` smallint(6) DEFAULT NULL,
  `3B` smallint(6) DEFAULT NULL,
  `HR` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`stint`),
  KEY `lgID` (`lgID`),
  KEY `teamID` (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS pitching;
SET character_set_client = utf8mb4 ;
CREATE TABLE `pitching` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `stint` smallint(6) NOT NULL,
  `teamID` char(3) DEFAULT NULL,
  `lgID` char(2) DEFAULT NULL,
  `W` smallint(6) DEFAULT NULL,
  `L` smallint(6) DEFAULT NULL,
  `G` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `playerID` (`playerID`,`yearID`,`stint`),
  KEY `lgID` (`lgID`),
  KEY `teamID` (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS appearances;
SET character_set_client = utf8mb4 ;
CREATE TABLE `appearances` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `playerID` varchar(9) NOT NULL,
  `G_all` smallint(6) DEFAULT NULL,
  `G_batting` smallint(6) DEFAULT NULL,
  `G_pitcher` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `yearID` (`yearID`,`teamID`,`playerID`),
  KEY `lgID` (`lgID`),
  KEY `teamID` (`teamID`),
  KEY `playerID` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
