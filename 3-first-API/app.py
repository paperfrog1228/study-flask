from flask import Flask
app = Flask(__name__)
@app.route("/ping".methods=['GET']) #route 데코레이터를 사용하여 엔드포인트를 등록. -> ping 
#고유 주소는 "ping"이며 HTTP 메소드는 GET으로 설정되어 등록되어있다는데 무슨 뜻..
def ping():
    return "pong"
app.run(host='0.0.0.0') # 내가 외부에서 접속하려고 임의로 작성한 코드.
