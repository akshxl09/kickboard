CREATE TABLE IF NOT EXISTS feedback (
U_ID varchar(45) NOT NULL,
num INT NOT NULL AUTO_INCREMENT,
title varchar(45) NOT NULL,
time varchar(45) NOT NULL,
comment varchar(2000) NOT NULL,
PRIMARY KEY(num),
FOREIGN KEY(U_ID) references user(U_ID) on delete cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;