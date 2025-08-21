import os
import sqlite3
import pickle
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key-that-should-be-more-secure' # 취약점 5: 예측 가능한 약한 시크릿 키 사용

DATABASE = 'users.db'

def init_db():
    with app.app_context():
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
        cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'password123')")
        db.commit()
        db.close()

# 사용자 이름으로 사용자 정보 조회
@app.route('/user')
def get_user():
    username = request.args.get('username')
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    
    # 취약점 1: SQL 인젝션 (SQL Injection)
    # 사용자 입력을 그대로 쿼리문에 삽입하여 악의적인 SQL 구문 실행 가능
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    db.close()
    
    return jsonify(user) if user else ('User not found', 404)

# 시스템 명령어 실행
@app.route('/exec')
def execute_command():
    command = request.args.get('cmd')
    
    # 취약점 2: 명령어 인젝션 (Command Injection)
    # 사용자로부터 받은 명령어를 검증 없이 시스템에서 실행하여 원격 코드 실행 가능
    os.system(command)
    
    return 'Command executed'

# 사용자 프로필 데이터 처리
@app.route('/profile', methods=['POST'])
def update_profile():
    encoded_data = request.data
    
    # 취약점 3: 안전하지 않은 역직렬화 (Insecure Deserialization)
    # 신뢰할 수 없는 데이터를 pickle로 역직렬화하여 임의 코드 실행 가능
    profile_data = pickle.loads(base64.b64decode(encoded_data))
    
    return f"Profile for {profile_data.get('username')} updated."

# 관리자 비밀번호 (예시)
# 취약점 4: 하드코딩된 비밀번호 (Hardcoded Password)
# 소스 코드에 민감한 정보(비밀번호)를 직접 저장하여 노출 위험
ADMIN_PASSWORD = "supersecretadminpassword"

if __name__ == '__main__':
    init_db()
    # 디버그 모드는 개발 환경에서만 사용해야 함
    app.run(debug=True) # 운영 환경에서는 False로 설정해야 함