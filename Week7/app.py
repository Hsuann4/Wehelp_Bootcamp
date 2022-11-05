from datetime import datetime
from hashlib import new
from pickle import TRUE
from sqlite3 import Cursor
from flask import Flask, redirect
from flask import request
from flask import render_template
from flask import session
from flask import jsonify
import mysql.connector
import json 

conn = mysql.connector.connect(
    user='root', password='Dennis860404_', database='website'
)

app = Flask(__name__, )

app.secret_key = "Don't tell others"




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods={"POST"})
def signup():
    new_name = str(request.form["rig_username"])
    new_account = str(request.form["rig_account"])
    new_password = str(request.form["rig_password"])

    cursor = conn.cursor(buffered = True)
   
    query = "SELECT 'username' FROM member WHERE username = %s;"
    tumple = (new_account,)
    cursor.execute(query,tumple)
    check = cursor.fetchone()
    if check:
        return redirect("/error?message=invalid_token")
    else:
        add_member = ("INSERT INTO member"
                      "(name, username, password)"
                      "VALUES (%s, %s, %s)")
        data_member = (new_name, new_account, new_password)
        cursor.execute(add_member, data_member)
        conn.commit()

        return redirect("/")


@app.route("/signin", methods=["POST"])
def signin():

    account = str(request.form["account"]) 
    password = str(request.form["password"])

    cursor = conn.cursor(buffered = True)
    query = "SELECT id, name, username, password FROM member WHERE username = %s AND password = %s;"
    tumple = (account, password)
    cursor.execute(query, tumple)
    member = cursor.fetchone()
    if member:
        session['id'], session['name'], session['username'], session['password'] = member
        return redirect("/member")
    else:
        return redirect("/error?message=wronginput")
 
    


@app.route('/api/member', methods = ["GET"])
def getdata ():
    getvalue = request.args #接收前端寄來的json
  
    input = getvalue['username'] #看看前端Json 格式
    
    cursor = conn.cursor(buffered = True)
    query = "SELECT 'username' FROM member WHERE username = %s;"
    tuple_ = (input,)
    cursor.execute(query,tuple_)
    conn.commit()
    check = cursor.fetchone()

    if check: 
        cursor = conn.cursor(buffered=True)
        query = "SELECT id, name, username FROM member WHERE username = %s ;"
        tuple_ = (input,)
        cursor.execute(query, tuple_)
        search_result = cursor.fetchone()
        inner = {'id': search_result[0], 'name': search_result[1], 'username':search_result[2]  }
        
        return jsonify({"data": inner}) 
    else: 
        inner = None

        return jsonify({"data": inner}) 


@app.route("/api/member", methods =["PATCH"])
def updated():
    

    updatedinput = request.get_json()
    updatedinputvalue = updatedinput["name"]
    current_user = session["username"]

    cursor = conn.cursor(buffered = True)
    queryforupdate = "UPDATE member SET name = %s WHERE username = %s;"
    tuple_ = (updatedinputvalue, current_user)
    cursor.execute(queryforupdate, tuple_)
    query = "SELECT name FROM member WHERE username = %s; "
    tuple_for_check = (current_user,)
    cursor.execute(query,tuple_for_check)
    username = cursor.fetchone()[0]
    conn.commit()
    if username == updatedinputvalue:
        return jsonify({"ok":True})
    else: 
        return jsonify({"error":True})  


    
@app.route("/member", methods=["GET","POST"])
def Successful():
   
    if session.get("username") != None: 

        return render_template('ok.html',
           
           name_from_sql = session.get("name")
            )
    else: 
        return redirect('/')
    
    
   
@app.route("/error", methods=["GET"])
def Failed_1():
    data = request.args.get("message")
    if  data == str("wronginput"):
        return render_template("failed_2.html")
    elif data == str("invalid_token"):
        return render_template("failed_3.html")


@app.route("/signout", methods=["GET"])
def Signout():
    session.pop('id', None)
    session.pop('name', None)
    session.pop('username', None)
    session.pop('password', None)

    return redirect("/")


app.run(port="3000", debug= True)
