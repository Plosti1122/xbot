token = "875904630:AAHXnN72BwRplv5p08mglpxujzUmu42vO50"
import sqlite3
import _pickle as pickle
import requests


def new_user(id):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE id =:a1", {"a1":id})
    results = cursor.fetchall()
    conn.close()
    if len(results)>0:
        return(False)
    else:
        return(True)


def add_new_user(id,username):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("insert into user values (:a1,:a2,:a3,:a4,:a5) ", {"a1":id,"a2":'',"a3":'',"a4":username,"a5":0})
    conn.commit()
    conn.close()


def get_user_stage(id):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT stage FROM user WHERE id =:a1", {"a1":id})
    results = cursor.fetchall()
    conn.close()
    return(results[0][0])

def set_user_stage(id,stage):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET stage =:a1 WHERE id =:id", {"a1":stage,"id":id})
    conn.commit()
    conn.close()



def extract_unique_code(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[1] if len(text.split()) > 1 else None



def referal(id,text):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET ref =:a1 WHERE id =:id", {"a1": text, "id": id})
    conn.commit()
    conn.close()


def add_new_user_by_ref(id,urnme,nick):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("insert into user values (:a1,:a2,:a3,:a4,:a5) ", {"a1":id,"a2":'',"a3":urnme,"a4":nick,"a5":0})
    conn.commit()
    conn.close()


def get_ref(id):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ref FROM user WHERE id =:a1", {"a1": id})
    results = cursor.fetchall()
    conn.close()
    return (results[0][0])

def set_refS(id,stage):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    abc = stage+1
    cursor.execute("UPDATE user SET kolvo =:a1 WHERE id =:id", {"a1":abc,"id":id})
    conn.commit()
    conn.close()

def get_refS(id):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT kolvo FROM user WHERE id =:a1", {"a1": id})
    results = cursor.fetchall()
    conn.close()
    return (results[0][0])


def get_nick(id):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM user WHERE id =:a1", {"a1": id})
    results = cursor.fetchall()
    conn.close()
    return (results[0][0])

def set_ssd(id,res1):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    res1 = pickle.dumps(res1)
    cursor.execute("UPDATE SSD SET infa =:a1 WHERE id =:id", {"a1":res1,"id":id})
    conn.commit()
    conn.close()

def get_ssd(id):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT infa FROM SSD WHERE id =:a1", {"a1": id})

    results = cursor.fetchall()
    res = pickle.loads(results[0][0])
    conn.close()
    return (res)


def new_admin(id):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin WHERE id =:a1", {"a1":id})
    results = cursor.fetchall()
    conn.close()
    if len(results)>0:
        return(False)
    else:
        return(True)


def add_new_superadmin(id):
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("insert into admin values (:a1,:a2,:a3) ", {"a1":id,"a2":'',"a3":1})
    conn.commit()
    conn.close()

def get_user_list_id():
    conn = sqlite3.connect('rbasa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM user WHERE kolvo >=:a1",{"a1":0})
    results = cursor.fetchall()
    conn.close()
    res=[]
    for i in range(0,len(results)):
        res.append(results[i][0])
    return(res)