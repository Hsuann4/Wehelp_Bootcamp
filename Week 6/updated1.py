


from datetime import datetime
from hashlib import new
from pickle import TRUE
from sqlite3 import Cursor
from flask import Flask, redirect
from flask import request
from flask import render_template
from flask import session


import datetime
import mysql.connector

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

    cursor = conn.cursor()
   
    query = (f'SELECT username FROM member WHERE username = "{new_account}";')
    cursor.execute(query)
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

    cursor = conn.cursor()
    query = (f"SELECT id, name, username, password FROM member where username = '{account}' and password = '{password}';")
    cursor.execute(query)
    member = cursor.fetchone()
    if member:
        session['id'], session['name'], session['username'], session['password'] = member
        return redirect("/member")
    else:
        return redirect("/error?message=wronginput")
 
       
@app.route("/member", methods=["GET"])
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


app.run(port="3000")
