CREATE TABLE IF NOT EXISTS broken_log (
    U_ID varchar(45) NOT NULL,
    K_ID INT NOT NULL,
    time varchar(45) NOT NULL,
    FOREIGN KEY(K_ID) references kickboard(K_ID)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;