CREATE TABLE IF NOT EXISTS user_info (
    name varchar(10) NOT NULL,
    user_num varchar(14) NOT NULL,
    email varchar(45) NOT NULL,
    l_num varchar(15) NOT NULL,
    phone varchar(15) NOT NULL,
    FOREIGN KEY(user_num) REFERENCES user(user_num) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;