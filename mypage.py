from flask import Blueprint, session, render_template, jsonify, g
from DB_func import get_feedback_mine, find_kick_log

bp = Blueprint('mypage',__name__)

@bp.route('/mypage')
def mypage():
        if 'userid' in session: #현재 로그인 된 상태일 때만 마이페이지에 들어갈 수 있음
            data1 = get_feedback_mine(g.db,session['userid'])
            data2= find_kick_log(g.db,session['userid'])
            return render_template('mypage.html', data_list = data1, data_list2 = data2)
        else:
            return render_template('login.html')


@bp.route('/mypage_data/<u_id>')
def mypage_data(u_id):
    data=get_feedback_mine(g.db,u_id) #내 문의내역 받아와서
    return jsonify(                   #요청값을 다시 보내주는 함수 ajax와 연동
        result = "success",
        data = data
    )
