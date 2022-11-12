create database sqs;
use sqs;
CREATE TABLE IF NOT EXISTS sqs_messages (
	`sqs_message_id` VARCHAR(255), 
	`sqs_message` VARCHAR(255),
	 PRIMARY KEY (sqs_message_id));
