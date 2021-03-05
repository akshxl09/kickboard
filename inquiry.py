from flask import render_template, jsonify, Blueprint, redirect, session, request, g
from DB_func import get_feedback, get_write, insert_feedback
import datetime

bp = Blueprint('inquiry',__name__)

@bp.route('/inquiry')
def inquiry():
    return render_template('inquiry.html')

@bp.route('/inquiry_data') #문의내역 전체 띄우기
def inquiry_data():
    data = get_feedback(g.db)
    print(data)
    return jsonify( 
        result = "success",
        data = data
    )

@bp.route('/inquiry_data_num/<int:num>')
def inquiry_data_num(num): #클릭한 문의내역의 내용 띄우기
    data = get_write(g.db,num)
    return jsonify(
        result = "success",
        data = data
    )

@bp.route('/write', methods=['GET','POST']) #글쓰기
def write():
    if request.method == 'GET':    
        if 'userid' in session:      #로그인 된 상태일 때
            return render_template('write.html')
        else:                        #로그인 안된 상태일 때
            return render_template('login.html')
    else:
        #글 제목과 내용 생성
        title = request.form['title']
        content = request.form['content']

        now = datetime.datetime.now() #현재시간을 받아주는 파이썬 함수

        insert_feedback(g.db,session['userid'],title,now,content)
        return redirect('/inquiry')
