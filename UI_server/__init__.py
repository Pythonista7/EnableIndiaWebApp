from flask import Flask, request
from flask import render_template,json,render_template_string,redirect
import json

import requests as req

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

        print("All data from the form ",data) # check console log
        
        #retrive and validate password and confirm_password if both dont match redo form
        # 
        #use a sqlite or other DB to store data entered in the form
        #
        # need destination template to render success(Log In form) and failure of signup (Redo the same signup form)

        return redirect("/login")


    @uiapp.route("/login",methods=["GET","POST"])
    def login_view():

        if request.method == "GET":
            return render_template("login.html")

        if request.method == "POST":
            username=request.form["username"]
            password=request.form["password"]
            #write code to verify user is already registered and validate login
            #possibly add a cookie to persisten login session
            return redirect("/home")

    @uiapp.route("/home",methods=["GET","POST"])
    def home_view():	
        if request.method=="GET":
            return render_template("home_page.html",data=X_names.values())
        
        if request.method=="POST":
            print("\n\n POSTED \n\n ")
            data=request.form.values()
            attr=list(data)
            print(attr)
            res=req.post("https://eiapp.herokuapp.com/ml/api/predict",json={'labels':attr})
            res=res.json()['res']
            
            return render_template("jobs.html",jobs=json.loads(res))
        


    return uiapp