from pymysql import cursors


#id 찾기
def find_id_pw(db, id, pw):
    with db.cursor() as cursor:
        sql = "SELECT * FROM user where u_id=%s and pw=%s"
        data = (id,pw)
        cursor.execute(sql,data)
        result = cursor.fetchall()
    db.commit()
    return result

#해당 회원의 정보 가져오기
def find_id(db, id):
    with db.cursor() as cursor:
        sql = "SELECT * FROM user where u_id=%s"
        data = (id)
        cursor.execute(sql,data)
        result = cursor.fetchall()
    db.commit()
    return result

#user 에 넣어주기
def insert_user(db, u_id, pw, name, user_num, email, l_num, phone):
    with db.cursor() as cursor:
        sql_1 = "INSERT INTO user values(%s,%s,%s,%s)"
        sql_2 = "INSERT INTO user_info values(%s,%s,%s,%s,%s)"
        data_1=(u_id,pw,name,user_num)
        data_2=(name,user_num,email,l_num,phone)
        cursor.execute(sql_1,data_1) #cursor.execute 는 받을 수 있는 인자가 최대 2개. 하나는 쿼리문과 나머지 하나는 인자. 따라서 배열 형태로 넣어줘야함
        cursor.execute(sql_2,data_2)
    db.commit()

#문의내역에 글 작성
def insert_feedback(db,u_id,title,time,comment):
    with db.cursor() as cursor:
        sql = "INSERT INTO feedback values(%s,NULL,%s,%s,%s)"
        data = (u_id,title,time,comment)
        cursor.execute(sql,data)
    db.commit()

#문의내역 가져오기
def get_feedback(db):
    with db.cursor() as cursor:
        sql = "select num,title,u_id,time from feedback order by num"
        cursor.execute(sql)
        result = cursor.fetchall()

    return result

#내 문의내역 가져오기
def get_feedback_mine(db,u_id):
    with db.cursor() as cursor:
        sql = "select num,title,time from feedback where u_id=%s"
        cursor.execute(sql,u_id)
        result = cursor.fetchall()
    
    return result

#제목 찾기
def find_title(db,title,u_id,time):
    with db.cursor() as cursor:
        sql = "select title,time,comment,u_id from feedback where title=%s && u_id=%s && time=%s"
        data=(title,u_id,time)
        cursor.execute(sql,data)
        result = cursor.fetchall()
    
    return result

#해당 번호의 글 내용가져오기
def get_write(db,num):
    with db.cursor() as cursor:
        sql = "select title,time,comment,u_id from feedback where num=%s"
        cursor.execute(sql,num)
        result = cursor.fetchall()
    
    return result

#모든 킥보드 가져오기
def kickboard(db):
    with db.cursor() as cursor:
        sql = "select * from kickboard"
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

#해당 번호의 킥보드에서 정보 가져오기
def get_kickboard(db,k_id):
    with db.cursor() as cursor:
        sql = "select * from kickboard where k_id=%s"
        cursor.execute(sql,k_id)
        result = cursor.fetchone()
    
    return result

#킥보드 마지막 사용자 찾기
def find_kick_log(db,u_id):
    with db.cursor() as cursor:
        sql = "select k_id,payment,borrowed_time, time from kick_log where u_id=%s"
        cursor.execute(sql,u_id)
        result = cursor.fetchall()
    
    return result

#사용 가능한 킥보드 가져오기
def available_kickboard(db):
    with db.cursor() as cursor:
        sql = "select k_id, latitude, longtitude from kickboard where broken='no' and used='no' and Battery>20"
        cursor.execute(sql)
        result = cursor.fetchall()
    
    return result

#처음에 빌릴 때
def update_kickboard(db,k_id,time): 
    with db.cursor() as cursor:
        sql = "update kickboard set Used='yes', time=%s where k_id=%s"
        data = (time, k_id)
        cursor.execute(sql, data)
    db.commit()

#반납할 때(반납 버튼을 눌렀을 때)
def return_kickboard_1(db,k_id,u_id,time,payment,borrowed_time,distance):
    with db.cursor() as cursor:
        sql = "insert into kick_log values(%s,%s,%s,%s,%s,%s)"
        data = (u_id,k_id,time,payment,borrowed_time,distance)
        cursor.execute(sql, data)
    db.commit()

def return_kickboard_2(db,k_id,u_id,Latitude,Longtitude):
    with db.cursor() as cursor:
        sql = "update kickboard set u_id=%s, Battery = Battery - 10, Latitude = %s, Longtitude = %s, Used='no' where k_id=%s"
        data = (u_id,Latitude,Longtitude,k_id)
        cursor.execute(sql, data)
    db.commit()

#고장났을 때(고장 버튼을 눌렀을 때)
def broken_kickboard(db,k_id,u_id,time,Latitude,Longtitude):
    with db.cursor() as cursor:
        sql = "update kickboard set Battery = Battery - 10, Latitude = %s, Longtitude = %s, Used='no',Broken='yes' where k_id=%s"
        data = (Latitude,Longtitude,k_id)
        cursor.execute(sql, data)
    db.commit()

def broken_log(db,k_id,u_id,time):
    with db.cursor() as cursor:
        sql = "insert into broken_log values(%s,%s,%s)"
        data = (u_id,k_id,time)
        cursor.execute(sql,data)
    db.commit()


#최근 결제한 건 보여주기 위해서 조인 연산
def join(db,k_id):
    with db.cursor() as cursor:
        sql = "select a.payment, a.borrowed_time, a.distance from kick_log a LEFT JOIN kickboard b ON a.k_id = b.k_id where a.time = b.time and a.k_id = %s"
        data = (k_id)
        cursor.execute(sql,data)
        result = cursor.fetchone()
    
    return result

#어드민창에서 해당 킥보드의 내용을 변경했을 때
def admin_update_sql(db,k_id,battery,latitude,longtitude,broken,u_id,time):
    with db.cursor() as cursor:
        sql_1 = "update kickboard set battery=%s, latitude=%s, longtitude=%s, broken=%s, u_id=%s, time=%s where k_id=%s"
        sql_2 = "update kick_info set battery_change = battery_change + 1 where k_id=%s"
        data_1 = (battery,latitude,longtitude,broken,u_id,time,k_id)
        cursor.execute(sql_1,data_1)
        cursor.execute(sql_2,k_id)
    db.commit()
