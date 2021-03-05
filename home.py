from flask import render_template, redirect, Blueprint, session, jsonify, request, g, url_for
from DB_func import find_id_pw, find_id, insert_user


bp = Blueprint('home', __name__)
bp.secret_key = "check session"

@bp.route('/') #메인페이지
def home():
        return render_template('project.html')


@bp.route('/login', methods=['GET','POST']) #로그인 페이지
def login():
    if request.method=='GET': #GET 이면 로그인 페이지를 띄워줌
        return render_template('login.html')
    else:                       #POST 이면 로그인 페이지에서 ID, PW를 입력받은 상태
        session['userid'] = request.form['u_id'] 
        session['password'] = request.form['password']
        
        if not (session['userid'] and session['password']): #둘 중 하나라도 입력되지 않았으면
            session.clear()
            return "<script type='text/javascript'>alert('모두 입력해주세요.');document.location.href='/login';</script>"

        result_id=find_id_pw(g.db,session['userid'], session['password']) #회원 테이블에서 해당 아이디와 비밀번호의 정보 가져옴
        
        if (result_id): #정보가 존재하면 메인화면
            return redirect('/')
        else:           #없으면 틀린 것. 또는 아이디가 존재하지 않는 것.
            session.clear()
            return "<script type='text/javascript'>alert('아이디나 비밀번호가 틀립니다.');document.location.href='/login';</script>"

@bp.route('/logout') #로그아웃 클릭시
def logout():
   session.pop('userid', None)
   session.pop('password', None)
   return redirect(url_for('home.home'))


@bp.route('/register', methods=['GET','POST']) #회원가입
def register():
    if request.method == 'GET':
        return render_template("register.html") # 처음에 회원가입 페이지 띄워줌
    else:       # 회원가입 페이지에서 값을 입력받았을 때
    
        #회원정보 생성
        userid = request.form['u_id'] 
        password = request.form['password']
        username = request.form['username']
        user_num = request.form['user_num']
        license_num = request.form['license_num']
        email = request.form['email']
        phone = request.form['phone']

        #모두 입력받아야함.
        if not (userid and username and password and user_num and license_num and email and phone) :
            return "<script type='text/javascript'>alert('모두 입력해주세요.');document.location.href='/register';</script>"

        else: #모두 입력이 정상적으로 되었다면 밑에명령실행(DB에 입력됨)

             try:  #일단 회원정보를 DB에 입력해본다. Exception Handling 처리
                insert_user(g.db,userid, password, username, user_num,email,license_num,phone)
                return redirect('/login')
             except: #만약 mysql에러가 발생시 예외처리
                return "<script type='text/javascript'>alert('중복된 아이디가 존재합니다.');document.location.href='/register';</script>"
 

@bp.route('/not')
def nothing():
    ...