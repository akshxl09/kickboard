CREATE TABLE IF NOT EXISTS user (
    U_ID varchar(45) NOT NULL,
    Pw varchar(45) NOT NULL,
    name varchar(10) NOT NULL,
    user_num varchar(14) NOT NULL,
    PRIMARY KEY(U_ID),
    UNIQUE KEY(user_num)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
