import sqlite3
import hashlib

db_part="auth.db"

def md5(data):
    return hashlib.md5(str(data).encode()).hexdigest()

def create_table():
    conn = sqlite3.connect(db_part)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE "user" (
    "username"	varchar(32) UNIQUE,
    "password" varchar(32),
    "id" INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
    );
    """)
    conn.commit()
    conn.close()

def create_account(username, password):## if success return True
    if duplicate_username(username) == True:
        print("can not create account because this username used")
        return False
    password=md5(password)
    conn = sqlite3.connect(db_part)
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO user('username','password')
    VALUES(?,?);
    """,[username,password])
    conn.commit()
    conn.close()
    return True

def get_all():
    conn = sqlite3.connect(db_part)
    cur = conn.cursor()
    cur.execute("""
    SELECT *
    FROM user;
    """)
    conn.commit()
    ls = cur.fetchall()
    conn.close()
    return ls

def auth(username, password):## login success return TRUE
    password = md5(password)
    conn = sqlite3.connect(db_part)
    cur = conn.cursor()
    cur.execute("""
    SELECT *
    FROM user
    WHERE username=? and password=?
    """,[username,password])
    conn.commit()
    if len(cur.fetchall()) > 0 :
        conn.close()
        return True
    else:
        conn.close()
        return False

def get_account_by_id(id_int):
    conn = sqlite3.connect(db_part)
    cur = conn.cursor()
    cur.execute("""
    SELECT *
    FROM user
    WHERE id=?
    """,[id_int])
    conn.commit()
    ls = cur.fetchone()
    conn.close()
    return ls

def clear_account():
    conn = sqlite3.connect(db_part)
    cur=conn.cursor()
    cur.execute("""
    DELETE FROM user
    """)
    conn.commit()
    conn.close()

def delete_account_by_id(id_int):## for admin
    conn = sqlite3.connect(db_part)
    cur=conn.cursor()
    cur.execute("""
    DELETE FROM user
    WHERE id=?
    """,[id_int])
    conn.commit()
    conn.close()

def delete_acount(username,password):## for user
    if auth(username,password) == False:
        print("username or password incorrect cannot delete")
        return False
    password = md5(password)
    conn = sqlite3.connect(db_part)
    cur=conn.cursor()
    cur.execute("""
    DELETE FROM user
    WHERE username=? AND password=?
    """,[username , password ])
    conn.commit()
    conn.close()
    return True

def duplicate_username(username):
    conn = sqlite3.connect(db_part)
    cur = conn.cursor()
    cur.execute("""
    SELECT username
    FROM user
    WHERE username=?
    """,[username])
    conn.commit()
    found = False
    if cur.fetchone() != None:
        found = True
    conn.close()
    return found

if __name__=="__main__":
    print("test db controller")
    #create_table()## first time run this to create database and table
    #create_account("admin","admin")
    #print(auth('admin', 'admin'))## true คือ login ได้
    #print(auth("spa-cdti","fake_password"))
    #print(get_account_by_id(1))## ถ้ามีมันจะเอาออกมา
    #print(get_account_by_id(9999))## ถ้ามีมันจะเอาออกมา
    #clear_account()
    #delete_acount("123","123")
    print(get_all())