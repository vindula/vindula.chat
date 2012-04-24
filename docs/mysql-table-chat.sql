SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `myvindulaDB` DEFAULT CHARACTER SET latin1 ;
USE `myvindulaDB` ;

-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_food_specialty`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_food_specialty` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_food_specialty` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_food_restaurant`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_food_restaurant` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_food_restaurant` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL DEFAULT NULL ,
  `address` VARCHAR(100) NULL DEFAULT NULL ,
  `phone_number` VARCHAR(45) NULL DEFAULT NULL ,
  `delivery` TINYINT(1) NULL DEFAULT NULL ,
  `opening_hours` VARCHAR(45) NULL DEFAULT NULL ,
  `has_agreement` INT(1) NULL DEFAULT NULL ,
  `agreement` VARCHAR(45) NULL DEFAULT NULL ,
  `vin_food_specialty_id` INT(11) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_vin_food_restaurant_vin_food_specialty1` (`vin_food_specialty_id` ASC) ,
  CONSTRAINT `fk_vin_food_restaurant_vin_food_specialty1`
    FOREIGN KEY (`vin_food_specialty_id` )
    REFERENCES `myvindulaDB`.`vin_food_specialty` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_comments`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_comments` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_comments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(45) NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `type` VARCHAR(45) NULL DEFAULT NULL ,
  `id_obj` VARCHAR(45) NULL DEFAULT NULL ,
  `isPlone` TINYINT(1) NOT NULL DEFAULT '0' ,
  `text` TEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 25
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_confgfuncdetails`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_confgfuncdetails` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_confgfuncdetails` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `name` TINYINT(1) NULL DEFAULT '0' ,
  `phone_number` TINYINT(1) NULL DEFAULT '0' ,
  `cell_phone` TINYINT(1) NULL DEFAULT '0' ,
  `email` TINYINT(1) NULL DEFAULT '0' ,
  `employee_id` TINYINT(1) NULL DEFAULT '0' ,
  `date_birth` TINYINT(1) NULL DEFAULT '0' ,
  `registration` TINYINT(1) NULL DEFAULT '0' ,
  `enterprise` TINYINT(1) NULL DEFAULT '0' ,
  `position` TINYINT(1) NULL DEFAULT '0' ,
  `admission_date` TINYINT(1) NULL DEFAULT '0' ,
  `cost_center` TINYINT(1) NULL DEFAULT '0' ,
  `job_role` TINYINT(1) NULL DEFAULT '0' ,
  `organisational_unit` TINYINT(1) NULL DEFAULT '0' ,
  `reports_to` TINYINT(1) NULL DEFAULT '0' ,
  `location` TINYINT(1) NULL DEFAULT '0' ,
  `postal_address` TINYINT(1) NULL DEFAULT '0' ,
  `special_roles` TINYINT(1) NULL DEFAULT '0' ,
  `photograph` TINYINT(1) NULL DEFAULT '0' ,
  `nickname` TINYINT(1) NULL DEFAULT '0' ,
  `pronunciation_name` TINYINT(1) NULL DEFAULT '0' ,
  `committess` TINYINT(1) NULL DEFAULT '0' ,
  `projetcs` TINYINT(1) NULL DEFAULT '0' ,
  `personal_information` TINYINT(1) NULL DEFAULT '0' ,
  `skills_expertise` TINYINT(1) NULL DEFAULT '0' ,
  `license_plate_numbers` TINYINT(1) NULL DEFAULT '0' ,
  `profit_centre` TINYINT(1) NULL DEFAULT '0' ,
  `languages` TINYINT(1) NULL DEFAULT '0' ,
  `availability` TINYINT(1) NULL DEFAULT '0' ,
  `papers_published` TINYINT(1) NULL DEFAULT '0' ,
  `teaching_research` TINYINT(1) NULL DEFAULT '0' ,
  `delegations` TINYINT(1) NULL DEFAULT '0' ,
  `resume` TINYINT(1) NULL DEFAULT '0' ,
  `blogs` TINYINT(1) NULL DEFAULT '0' ,
  `customised_message` TINYINT(1) NULL DEFAULT '0' ,
  `vin_myvindula_department` TINYINT(1) NULL DEFAULT '0' ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_courses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_courses` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_courses` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(45) NOT NULL ,
  `length` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_department` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_department` (
  `uid_plone` VARCHAR(45) NOT NULL ,
  `vin_myvindula_funcdetails_id` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`uid_plone`, `vin_myvindula_funcdetails_id`) )
ENGINE = MyISAM
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_funcdetail_couses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_funcdetail_couses` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_funcdetail_couses` (
  `vin_myvindula_courses_id` INT(11) NOT NULL ,
  `vin_myvindula_funcdetail_username` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`vin_myvindula_courses_id`, `vin_myvindula_funcdetail_username`) ,
  INDEX `fk_vin_myvindula_funcdetail_couses_vin_myvindula_courses1` (`vin_myvindula_courses_id` ASC) ,
  CONSTRAINT `fk_vin_myvindula_funcdetail_couses_vin_myvindula_courses1`
    FOREIGN KEY (`vin_myvindula_courses_id` )
    REFERENCES `myvindulaDB`.`vin_myvindula_courses` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_languages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_languages` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_languages` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(45) NOT NULL ,
  `level` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_funcdetail_languages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_funcdetail_languages` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_funcdetail_languages` (
  `vin_myvindula_languages_id` INT(11) NOT NULL ,
  `vin_myvindula_funcdetail_username` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`vin_myvindula_languages_id`, `vin_myvindula_funcdetail_username`) ,
  INDEX `fk_vin_myvindula_funcdetail_languages_vin_myvindula_languages1` (`vin_myvindula_languages_id` ASC) ,
  CONSTRAINT `fk_vin_myvindula_funcdetail_languages_vin_myvindula_languages1`
    FOREIGN KEY (`vin_myvindula_languages_id` )
    REFERENCES `myvindulaDB`.`vin_myvindula_languages` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_funcdetails`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_funcdetails` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_funcdetails` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL DEFAULT NULL ,
  `phone_number` VARCHAR(45) NULL DEFAULT NULL ,
  `cell_phone` VARCHAR(45) NULL DEFAULT NULL ,
  `email` VARCHAR(45) NULL DEFAULT NULL ,
  `employee_id` VARCHAR(45) NULL DEFAULT NULL ,
  `username` VARCHAR(45) NULL DEFAULT NULL ,
  `date_birth` DATE NULL DEFAULT NULL ,
  `registration` VARCHAR(45) NULL DEFAULT NULL ,
  `position` VARCHAR(45) NULL DEFAULT NULL ,
  `enterprise` VARCHAR(45) NULL DEFAULT NULL ,
  `cost_center` VARCHAR(45) NULL DEFAULT NULL ,
  `admission_date` DATE NULL DEFAULT NULL ,
  `organisational_unit` VARCHAR(45) NULL DEFAULT NULL ,
  `reports_to` VARCHAR(45) NULL DEFAULT NULL ,
  `location` VARCHAR(45) NULL DEFAULT NULL ,
  `postal_address` VARCHAR(45) NULL DEFAULT NULL ,
  `special_roles` VARCHAR(45) NULL DEFAULT NULL ,
  `photograph` TEXT NULL DEFAULT NULL ,
  `nickname` VARCHAR(45) NULL DEFAULT NULL ,
  `pronunciation_name` VARCHAR(45) NULL DEFAULT NULL ,
  `committess` VARCHAR(45) NULL DEFAULT NULL ,
  `projetcs` VARCHAR(45) NULL DEFAULT NULL ,
  `personal_information` VARCHAR(45) NULL DEFAULT NULL ,
  `profit_centre` VARCHAR(45) NULL DEFAULT NULL ,
  `availability` VARCHAR(45) NULL DEFAULT NULL ,
  `papers_published` VARCHAR(45) NULL DEFAULT NULL ,
  `teaching_research` VARCHAR(45) NULL DEFAULT NULL ,
  `delegations` VARCHAR(45) NULL DEFAULT NULL ,
  `resume` VARCHAR(45) NULL DEFAULT NULL ,
  `blogs` VARCHAR(45) NULL DEFAULT NULL ,
  `customised_message` TEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_howareu`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_howareu` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_howareu` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(45) NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `visible_area` VARCHAR(45) NULL DEFAULT NULL ,
  `text` TEXT NULL DEFAULT NULL ,
  `upload_image` LONGBLOB NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 30
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_like`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_like` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_like` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(45) NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `type` VARCHAR(45) NULL DEFAULT NULL ,
  `id_obj` VARCHAR(45) NULL DEFAULT NULL ,
  `isPlone` TINYINT(1) NOT NULL DEFAULT '0' ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_recados`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_recados` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_recados` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(45) NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `destination` VARCHAR(45) NOT NULL ,
  `text` TEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 30
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_controlpanel_company_information`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_controlpanel_company_information` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_controlpanel_company_information` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `short_name` VARCHAR(45) NOT NULL ,
  `corporate_name` VARCHAR(45) NOT NULL ,
  `cnpj` VARCHAR(45) NOT NULL ,
  `phone_number` VARCHAR(45) NULL ,
  `address` VARCHAR(45) NULL ,
  `date_creation` DATETIME NOT NULL ,
  `city` VARCHAR(45) NULL ,
  `stade` VARCHAR(45) NULL ,
  `postal_code` VARCHAR(45) NULL ,
  `email` VARCHAR(45) NULL ,
  `website` VARCHAR(45) NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_suporte_confgsuporte`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_suporte_confgsuporte` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_suporte_confgsuporte` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `date_creation` DATETIME NOT NULL ,
  `key_contrato` TEXT NULL DEFAULT NULL ,
  `name_intranet` VARCHAR(45) NULL DEFAULT NULL ,
  `username` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_helpdesk_config`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_helpdesk_config` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_helpdesk_config` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(45) NOT NULL ,
  `email_corp` TINYINT(1)  NULL ,
  `email_user` TINYINT(1)  NULL ,
  `email_group` TINYINT(1)  NULL ,
  `email` VARCHAR(45) NULL ,
  `id_form` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_helpdesk_email`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_helpdesk_email` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_helpdesk_email` (
  `id` INT NOT NULL ,
  `user-group` VARCHAR(45) NULL ,
  `vin_helpdesk_config_id` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_table1_vin_helpdesk_config1` (`vin_helpdesk_config_id` ASC) ,
  CONSTRAINT `fk_table1_vin_helpdesk_config1`
    FOREIGN KEY (`vin_helpdesk_config_id` )
    REFERENCES `myvindulaDB`.`vin_helpdesk_config` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_contentcore_forms`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_contentcore_forms` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_contentcore_forms` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name_form` VARCHAR(45) NOT NULL ,
  `date_creation` VARCHAR(45) NOT NULL ,
  `description_form` VARCHAR(45) NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_contentcore_fields`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_contentcore_fields` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_contentcore_fields` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name_field` VARCHAR(45) NOT NULL ,
  `type_fields` VARCHAR(45) NOT NULL ,
  `list_values` TEXT NULL ,
  `date_creation` VARCHAR(45) NOT NULL ,
  `title` VARCHAR(45) NOT NULL ,
  `value_default` TEXT NULL DEFAULT NULL ,
  `description_fields` TEXT NULL DEFAULT NULL ,
  `ordenacao` INT NOT NULL ,
  `required` TINYINT(1)  NULL DEFAULT False ,
  `flag_ativo` TINYINT(1)  NULL DEFAULT True ,
  `forms_id` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_vin_contentcore_fields_vin_contentcore_forms1` (`forms_id` ASC) ,
  CONSTRAINT `fk_vin_contentcore_fields_vin_contentcore_forms1`
    FOREIGN KEY (`forms_id` )
    REFERENCES `myvindulaDB`.`vin_contentcore_forms` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_contentcore_form_instance`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_contentcore_form_instance` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_contentcore_form_instance` (
  `instance_id` INT NOT NULL AUTO_INCREMENT ,
  `forms_id` INT NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  PRIMARY KEY (`instance_id`, `forms_id`) ,
  INDEX `fk_vin_contentcore_form_instance_vin_contentcore_forms1` (`forms_id` ASC) ,
  CONSTRAINT `fk_vin_contentcore_form_instance_vin_contentcore_forms1`
    FOREIGN KEY (`forms_id` )
    REFERENCES `myvindulaDB`.`vin_contentcore_forms` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_contentcore_form_values`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_contentcore_form_values` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_contentcore_form_values` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `value` TEXT NULL DEFAULT NULL ,
  `value_blob` LONGBLOB NULL DEFAULT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `forms_id` INT NOT NULL ,
  `instance_id` INT NOT NULL ,
  `fields` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_vin_helpdesk_from_values_vin_helpdesk_forms1` (`forms_id` ASC) ,
  CONSTRAINT `fk_vin_helpdesk_from_values_vin_helpdesk_forms1`
    FOREIGN KEY (`forms_id` )
    REFERENCES `myvindulaDB`.`vin_contentcore_forms` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_backend_plane`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_backend_plane` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_backend_plane` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `nome_plano` VARCHAR(50) NOT NULL ,
  `qtd_servidores` VARCHAR(45) NOT NULL ,
  `acesso_forum` TINYINT(1)  NOT NULL ,
  `horario_plano` VARCHAR(45) NOT NULL ,
  `acesso_tickets` TINYINT(1)  NOT NULL ,
  `qtd_armazena_dados` VARCHAR(45) NOT NULL ,
  `qtd_transfer_dados` VARCHAR(45) NOT NULL ,
  `valor_plano` DECIMAL(10,2) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_backend_client`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_backend_client` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_backend_client` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `razao_social` VARCHAR(100) NOT NULL ,
  `cnpj` VARCHAR(45) NOT NULL ,
  `tel_comercial` VARCHAR(45) NULL DEFAULT NULL ,
  `tel_celular` VARCHAR(45) NULL DEFAULT NULL ,
  `endereco` VARCHAR(100) NULL DEFAULT NULL ,
  `numero` VARCHAR(10) NULL DEFAULT NULL ,
  `complemento` VARCHAR(100) NULL DEFAULT NULL ,
  `bairro` VARCHAR(100) NULL DEFAULT NULL ,
  `cidade` VARCHAR(100) NULL DEFAULT NULL ,
  `estado` VARCHAR(45) NULL DEFAULT NULL ,
  `pais` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_backend_contrato`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_backend_contrato` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_backend_contrato` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `vin_backend_client_id` INT(11) NOT NULL ,
  `vin_backend_plane_id` INT(11) NOT NULL ,
  `data_inicial` DATE NOT NULL ,
  `data_final` DATE NOT NULL ,
  `observacao` TEXT NULL DEFAULT NULL ,
  `chave_licenca` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_vin_backend_contrato_vin_backend_client1` (`vin_backend_client_id` ASC) ,
  INDEX `fk_vin_backend_contrato_vin_backend_plane1` (`vin_backend_plane_id` ASC) ,
  CONSTRAINT `fk_vin_backend_contrato_vin_backend_client1`
    FOREIGN KEY (`vin_backend_client_id` )
    REFERENCES `myvindulaDB`.`vin_backend_client` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vin_backend_contrato_vin_backend_plane1`
    FOREIGN KEY (`vin_backend_plane_id` )
    REFERENCES `myvindulaDB`.`vin_backend_plane` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_backend_addons`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_backend_addons` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_backend_addons` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `nome_addon` VARCHAR(100) NOT NULL ,
  `descricao_addon` TEXT NULL DEFAULT NULL ,
  `valor_addon` DECIMAL(10,2) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_backed_contrato_addons`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_backed_contrato_addons` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_backed_contrato_addons` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `vin_backend_contrato_id` INT(11) NOT NULL ,
  `vin_backend_addons_id` INT(11) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_vin_backed_contrato_addons_vin_backend_contrato1` (`vin_backend_contrato_id` ASC) ,
  INDEX `fk_vin_backed_contrato_addons_vin_backend_addons1` (`vin_backend_addons_id` ASC) ,
  CONSTRAINT `fk_vin_backed_contrato_addons_vin_backend_contrato1`
    FOREIGN KEY (`vin_backend_contrato_id` )
    REFERENCES `myvindulaDB`.`vin_backend_contrato` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vin_backed_contrato_addons_vin_backend_addons1`
    FOREIGN KEY (`vin_backend_addons_id` )
    REFERENCES `myvindulaDB`.`vin_backend_addons` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_contentcore_default_value`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_contentcore_default_value` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_contentcore_default_value` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `value` TEXT NOT NULL ,
  `lable` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_contentcore_parameters`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_contentcore_parameters` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_contentcore_parameters` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `forms_id` INT NOT NULL ,
  `fields_id` INT NULL ,
  `parameters` VARCHAR(45) NULL ,
  `value_parameters` VARCHAR(45) NULL ,
  PRIMARY KEY (`id`, `forms_id`) ,
  INDEX `fk_vin_contentcore_parameters_vin_contentcore_forms1` (`forms_id` ASC) ,
  INDEX `fk_vin_contentcore_parameters_vin_contentcore_fields1` (`fields_id` ASC) ,
  CONSTRAINT `fk_vin_contentcore_parameters_vin_contentcore_forms1`
    FOREIGN KEY (`forms_id` )
    REFERENCES `myvindulaDB`.`vin_contentcore_forms` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vin_contentcore_parameters_vin_contentcore_fields1`
    FOREIGN KEY (`fields_id` )
    REFERENCES `myvindulaDB`.`vin_contentcore_fields` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_holerite`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_holerite` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_holerite` (
  `id` INT(100) NOT NULL AUTO_INCREMENT ,
  `nome` VARCHAR(45) NULL DEFAULT NULL ,
  `matricula` VARCHAR(45) NULL DEFAULT NULL ,
  `cargo` VARCHAR(45) NULL DEFAULT NULL ,
  `cod_cargo` VARCHAR(45) NULL DEFAULT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `competencia` VARCHAR(45) NULL DEFAULT NULL ,
  `empresa` VARCHAR(45) NULL DEFAULT NULL ,
  `cod_empresa` VARCHAR(45) NULL DEFAULT NULL ,
  `endereco_empresa` VARCHAR(70) NULL DEFAULT NULL ,
  `cidade_empresa` VARCHAR(45) NULL DEFAULT NULL ,
  `estado_empresa` VARCHAR(45) NULL DEFAULT NULL ,
  `cnpj_empresa` VARCHAR(45) NULL DEFAULT NULL ,
  `total_vencimento` VARCHAR(45) NULL DEFAULT NULL ,
  `total_desconto` VARCHAR(45) NULL DEFAULT NULL ,
  `valor_liquido` VARCHAR(45) NULL DEFAULT NULL ,
  `salario_base` VARCHAR(45) NULL DEFAULT NULL ,
  `base_Inss` VARCHAR(45) NULL DEFAULT NULL ,
  `base_fgts` VARCHAR(45) NULL DEFAULT NULL ,
  `fgts_mes` VARCHAR(45) NULL DEFAULT NULL ,
  `base_irrf` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_descricao_holerite`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_descricao_holerite` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_descricao_holerite` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `codigo` VARCHAR(45) NULL DEFAULT NULL ,
  `descricao` VARCHAR(45) NULL DEFAULT NULL ,
  `ref` VARCHAR(45) NULL DEFAULT NULL ,
  `vencimentos` VARCHAR(45) NULL DEFAULT NULL ,
  `descontos` VARCHAR(45) NULL DEFAULT NULL ,
  `vin_myvindula_holerite_id` INT(100) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_vin_myvindula_descricao_holerite_vin_myvindula_holerite1` (`vin_myvindula_holerite_id` ASC) ,
  CONSTRAINT `fk_vin_myvindula_descricao_holerite_vin_myvindula_holerite1`
    FOREIGN KEY (`vin_myvindula_holerite_id` )
    REFERENCES `myvindulaDB`.`vin_myvindula_holerite` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_controlpanel_products`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_controlpanel_products` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_controlpanel_products` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL DEFAULT NULL ,
  `title` VARCHAR(45) NULL DEFAULT NULL ,
  `active` TINYINT(1) NULL DEFAULT NULL ,
  `installed` TINYINT(1) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1
COLLATE = latin1_swedish_ci;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_config_documents`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_config_documents` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_config_documents` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name_document` VARCHAR(45) NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `flag_ativo` TINYINT(1)  NOT NULL DEFAULT TRUE ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_user_documents`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_user_documents` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_user_documents` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `documento` LONGBLOB NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `vin_myvindula_funcdetails_username` VARCHAR(45) NOT NULL ,
  `vin_myvindula_config_documents_id` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_vin_myvindula_user_documents_vin_myvindula_config_documents1` (`vin_myvindula_config_documents_id` ASC) ,
  CONSTRAINT `fk_vin_myvindula_user_documents_vin_myvindula_config_documents1`
    FOREIGN KEY (`vin_myvindula_config_documents_id` )
    REFERENCES `myvindulaDB`.`vin_myvindula_config_documents` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
