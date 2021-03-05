from flask import Blueprint, g, request, render_template, session, jsonify
from DB_func import get_kickboard, return_kickboard_1, return_kickboard_2, broken_kickboard, broken_log, join
from haversine import haversine
import datetime


bp = Blueprint('pay',__name__)

@bp.route('/pay', methods = ['POST'])  #결제 페이지
def pay():
    #킥보드 이용중인 창에서 입력받은 위도와 경도, 그리고 해당 킥보드
    Latitude = request.form['Latitude']
    Longtitude = request.form['Longtitude']
    num = request.form['knum']
    now = (datetime.datetime.now())

    if request.form['a'] == "반납" :  #킥보드 이용중인 창에서 반납을 눌렀을 때
        
        result = get_kickboard(g.db, num) #킥보드에서 처음 빌린 시간, 위도, 경도 가져옴
        time_result = datetime.datetime.strptime(result['time'],'%Y-%m-%d %H:%M:%S.%f')
        borrowed_time = (int)((now - time_result).seconds) #초단위. 현재 반납한 시간에서 처음 빌린 시간을 빼줘서 얼마나 사용했는지 확인
        first_distance = ((float)(result['Latitude']), (float)(result['Longtitude'])) 
        last_distance = ((float)(Latitude), (float)(Longtitude))
        distance = haversine(first_distance, last_distance) #이동한 거리
        payment = (int)((borrowed_time * 1.6 + distance *3000)) # 빌린시간과 이동한 거리에 비례하여 계산. 분당 100원 (초당 1.6원), 키로당 3000원
        return_kickboard_2(g.db,num,session['userid'],Latitude,Longtitude)
        return_kickboard_1(g.db,num,session['userid'],time_result,payment,borrowed_time,distance)
        return render_template('pay.html')

    else: #킥보드 이용중인 창에서 고장을 눌렀을 때
        data = get_kickboard(g.db,num)
        try:                  #일단 DB에 고장내역을 입력함. Exception Handling 처리
            broken_kickboard(g.db,num,data['U_ID'],now,Latitude,Longtitude)
            broken_log(g.db,num,data['U_ID'],now)
        except:               #만약 마지막 사용자(이전 사용자)가 없는 경우, 어드민이 마지막 사용자라고 판단함.
            broken_kickboard(g.db,num,'admin',now,Latitude,Longtitude)
            broken_log(g.db,num,'admin',now)
        return render_template('project.html')

@bp.route('/pay_data/<int:num>') #최근 결제한 정보를 불러옴
def pay_data(num):
    data = join(g.db,num)
    return jsonify(
        result = "success",
        data = data
    )
