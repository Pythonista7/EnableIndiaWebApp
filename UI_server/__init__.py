from flask import Flask, request
from flask import render_template,json,render_template_string,redirect
import json

import requests as req

import sqlite3
#connect to the database


def create_app():
    app_name = 'uiapp'
    print('app_name = {}'.format(app_name))

    X_names=json.load(open("UI_server/X_names.json"))#Flask/X_names.json

    uiapp=Flask(__name__, instance_relative_config=True)
    uiapp.static_folder = 'static'

    @uiapp.route("/")
    def landing():
        return  redirect("/home")

    @uiapp.route("/signup")
    def admin():
        import json
        return render_template('register.html',status='status')


    @uiapp.route("/backend/create_user",methods=['POST'])
    def create_user():
        data=request.form 
        #use name tag html-attribute to reference form data, ex- to get username use request.form["Username"] 
        # reference admin.html for the form attributes 
        conn = sqlite3.connect('signupinfo.db')
        print("\n\nsuccessfully connected") #check console log
        c = conn.cursor()
        print("All data from the form ",data) # check console log
        name = request.form['name']
        email = request.form['email']
        phno = request.form['phone']
        username = request.form['username']
        password = request.form['password']
        cp = request.form['conf_password']
        #check if password and con_password match
        if cp == password:
            #use a sqlite or other DB to store data entered in the form
            #sql = "INSERT INTO RegisteredUsers(Name=?, Email=?, Phone=?, Username=?, Password=?"
            sql = "INSERT INTO RegisteredUsers(Name, Email, Phone, Username, Password) VALUES(?,?,?,?,?)"
            c.execute(sql, (name, email, phno, username, password))
            conn.commit()
        else:
            scope.error="Error" #copied this from signup.html
        # need destination template to render success(Log In form) and failure of signup (Redo the same signup form)

        return redirect("/login")

    """
CREATE TABLE "RegisteredUsers" ( "Name" TEXT, "Email" TEXT, "Phone" NUMERIC, "Username" TEXT, "Password" TEXT, PRIMARY KEY("Username","Email") )
    """
    @uiapp.route("/login",methods=["GET","POST"])
    def login_view():

        if request.method == "GET":
            return render_template("login.html")

        conn = sqlite3.connect('signupinfo.db')
        print("successfully connected") #check console log
        c = conn.cursor()
        if request.method == "POST":
            username=request.form["username"]
            password=request.form["password"]
            #write code to verify user is already registered and validate login
            validate='SELECT * FROM RegisteredUsers WHERE Username=? AND Password=?'
            c.execute(validate, (username, password))
            credentials=c.fetchall()
            if credentials != '\0':
                return redirect("/home") #login successful
            else:
                print('Invalid username or password') #idk what to do here, take input again
            #possibly add a cookie to persisten login session 

    @uiapp.route("/home",methods=["GET","POST"])
    def home_view():	
        if request.method=="GET":
            return render_template("input.html",data=X_names.values())
        
        if request.method=="POST":
            print("\n\n POSTED \n\n ")
            data=request.form.values()
            attr=list(data)
            print(attr) #https://eiapp.herokuapp.com/
            res=req.post("https://eiapp.herokuapp.com/ml/api/predict",json={'labels':attr})#("https://eiapp.herokuapp.com/ml/api/predict",json={'labels':attr})
            res=res.json()['res']
            
            return render_template("result.html",jobs=json.loads(res))
        


    return uiapp
