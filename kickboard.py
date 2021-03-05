from flask import render_template, jsonify, g, session, Blueprint
from DB_func import available_kickboard, update_kickboard
import datetime

bp = Blueprint('kickboard',__name__)

@bp.route('/reservation')  #킥보드 이용중인 창
def reservation():
    return render_template('reservation.html')


@bp.route('/select_kickboard') #킥보드 선택창
def select_kickboard():
    if 'userid' in session:
        return render_template('select_kickboard.html')
    else:
        return render_template('login.html')

@bp.route('/select_kickboard_data')
def select_kickboard_data():
    data=available_kickboard(g.db)   #사용가능한 킥보드 받아오기.
    return jsonify(
        result="success",
        data=data
    )

@bp.route('/select_kickboard_data_num/<int:num>') 
def select_kickboard_data_num(num):
    now = datetime.datetime.now()
    update_kickboard(g.db,num,now)    #사용 시작과 동시에 해당 킥보드에 사용시작시간 넣어줌.
    return jsonify(
        result = 'success'
    )
