import sys
sys.path.insert(0,"./")
sys.path.insert(0,"../")
sys.path.insert(0,"../../")
from flask import Flask
from DB_init import get_db, close_db, init_db
from flask_cors import CORS
import home, mypage, inquiry, kickboard, pay, admin


app=Flask(__name__, instance_relative_config=True)
app.secret_key="check session"

CORS(app)

def main(test_config = None):
    init_db() #DB 초기화

    app.register_blueprint(home.bp)
    app.register_blueprint(mypage.bp)
    app.register_blueprint(inquiry.bp)
    app.register_blueprint(kickboard.bp)
    app.register_blueprint(pay.bp)
    app.register_blueprint(admin.bp)


@app.before_request # 요청이 오기 직전에 db 연결
def before_request():
    get_db()

@app.teardown_request # 요청이 끝난 직후에 db 연결 해제
def teardown_request(exception):
    close_db()

if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', debug=True)

