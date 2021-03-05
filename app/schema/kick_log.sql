CREATE TABLE IF NOT EXISTS kick_log (
    U_ID varchar(45) NOT NULL,
    K_ID INT NOT NULL,
    time varchar(45)NOT NULL,
    Payment varchar(45) NOT NULL,
    borrowed_time varchar(45) NOT NULL,
    distance varchar(45) NOT NULL,
    FOREIGN KEY(U_ID) references user(U_ID) on delete cascade,
    FOREIGN KEY(K_ID) references kickboard(K_ID) on delete cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;