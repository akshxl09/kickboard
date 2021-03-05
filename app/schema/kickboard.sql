CREATE TABLE IF NOT EXISTS kickboard (
    K_ID INT NOT NULL AUTO_INCREMENT,
    Battery INT NOT NULL,
    Latitude DOUBLE NOT NULL,
    Longtitude DOUBLE NOT NULL,
    Broken varchar(5) NOT NULL,
    U_ID varchar(45),
    Used varchar(5) NOT NULL,
    time varchar(45),
    PRIMARY KEY(K_ID)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
