

from flask import Flask, redirect
from flask import request
from flask import render_template
from flask import session


app=Flask(__name__, )
app.secret_key ="Don't tell others"




@app.route("/")
def index ():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():


    accounttypein = str(request.form["account"]) 
    passwordtypein = str(request.form["password"])
    
    if accounttypein == str("test") and passwordtypein == str("test"):
        Log_in_status = "Log_in"
        session["State"] = Log_in_status
       
        return redirect("/member")
    elif accounttypein == str("") or passwordtypein ==str(""):

        return redirect("/error?message=empty")
    else:
        return redirect("/error?message=wronginput")







@app.route("/member", methods =["GET"])
def ok():

        Log_in_status = session["State"]
        if Log_in_status != str("Log_in"):
            return redirect('/')

        return render_template('ok.html')


@app.route("/error", methods=["GET"])
def failed_1 ():
    data = request.args.get("message")
    if data == str("empty"):
        
        return render_template("failed_1.html")
    elif data == str("wronginput"):
        return render_template("failed_2.html")


@app.route("/signout", methods=["GET"])
def signout():
    Log_in_status = "Log_out"
    session['State'] = Log_in_status

    # return str(Log_in_status)
    return redirect("/")



app.run(port ="3000")