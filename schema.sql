CREATE DATABASE SpeedWatcher;

drop table if exists entry;
CREATE TABLE entry (
  `entry_id` BIGINT NOT NULL AUTO_INCREMENT,
  `entry_ping` INT NULL,
  `entry_speed_down` DECIMAL(5,2) NULL,
  `entry_speed_up` DECIMAL(5,2) NULL,
  `entry_status` VARCHAR(32) NULL,
  `entry_date_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`entry_id`)
);
