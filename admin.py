from flask import render_template, redirect, Blueprint, session, jsonify, request, g
from DB_func import admin_update_sql, broken_log, kickboard
import datetime

bp = Blueprint('admin',__name__)

@bp.route('/admin') #어드민 페이지
def admin():
    if(session['userid'] == 'admin'):
        return render_template('admin.html')
    else:
        return redirect('/')

@bp.route('/admin_data') #모든 킥보드 정보를 불러와서 보여줌
def damin_data():
    data = kickboard(g.db)
    return jsonify(
        result = "success",
        data = data
    )

@bp.route('/admin_fix') #킥보드 정보 수정창
def admin_fix():
    return render_template('admin_fix.html')

@bp.route('/admin_update', methods=['POST']) #수정할 킥보드 정보를 입력받아서 정보 저장
def admin_update():
    k_id = request.form['knum']
    u_id = "admin"
    time = datetime.datetime.now()
    latitude = request.form['Latitude']
    longtitude = request.form['Longtitude']
    broken = request.form['broken']
    battery = request.form['battery']

    admin_update_sql(g.db,k_id,battery,latitude,longtitude,broken,u_id,time)

    if broken == "yes":    #만약 broken이 yes로 바꼈을 때
        broken_log(g.db,k_id,u_id,time) #broken_log 테이블에 정보 저장
        
    return render_template('admin.html') 