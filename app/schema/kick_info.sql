CREATE TABLE IF NOT EXISTS kick_info (
    K_ID INT NOT NULL,
    Battery_change INT NOT NULL,
    Kind varchar(45) NOT NULL,
    Company varchar(45) NOT NULL,
    FOREIGN KEY(K_ID) references kickboard(K_ID) on delete cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;