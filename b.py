import sqlite3

def get_user(username):
    db = sqlite3.connect("example.db")
    cursor = db.cursor()
    # 사용자 입력을 그대로 쿼리 문자열에 삽입합니다.
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()