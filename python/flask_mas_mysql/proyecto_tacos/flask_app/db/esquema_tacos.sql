-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_tacos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_tacos` DEFAULT CHARACTER SET utf8 ;
USE `esquema_tacos` ;

-- -----------------------------------------------------
-- Table `esquema_tacos`.`restaurantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tacos`.`restaurantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `esquema_tacos`.`tacos`
-- Relación uno a muchos: un restaurante tiene muchos tacos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tacos`.`tacos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tortilla` VARCHAR(45) NULL,
  `guiso` VARCHAR(45) NULL,
  `salsa` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `restaurante_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tacos_restaurantes_idx` (`restaurante_id` ASC),
  CONSTRAINT `fk_tacos_restaurantes`
    FOREIGN KEY (`restaurante_id`)
    REFERENCES `esquema_tacos`.`restaurantes` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `esquema_tacos`.`complementos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tacos`.`complementos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_complemento` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `esquema_tacos`.`complementos_en_tacos`
-- Tabla intermedia de la relación muchos a muchos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tacos`.`complementos_en_tacos` (
  `taco_id` INT NOT NULL,
  `complemento_id` INT NOT NULL,
  PRIMARY KEY (`taco_id`, `complemento_id`),
  INDEX `fk_cet_complementos_idx` (`complemento_id` ASC),
  CONSTRAINT `fk_cet_tacos`
    FOREIGN KEY (`taco_id`)
    REFERENCES `esquema_tacos`.`tacos` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_cet_complementos`
    FOREIGN KEY (`complemento_id`)
    REFERENCES `esquema_tacos`.`complementos` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
