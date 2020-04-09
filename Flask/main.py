from flask import Flask,render_template,request,json,render_template_string,redirect
import json

import requests as req


app=Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def landing():
	return  redirect("/home")

@app.route("/signup")
def admin():
	import json
	return render_template('signup.html',status='status')


@app.route("/backend/create_user",methods=['POST'])
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


@app.route("/login",methods=["GET","POST"])
def login_view():

	if request.method == "GET":
		return render_template("login.html")

	if request.method == "POST":
		username=request.form["username"]
		password=request.form["password"]
		#write code to verify user is already registered and validate login
		#possibly add a cookie to persisten login session
		return redirect("/home")

@app.route("/home",methods=["GET","POST"])
def home_view():	
	if request.method=="GET":
		
		return render_template("home_page.html",data=X_names.values())
	
	if request.method=="POST":
		data=request.form.values()
		attr=list(data)
		res=req.post("http://localhost:9090/api/predict",json={'labels':attr})
		res=res.json()['res']
		
		return render_template("jobs.html",jobs=json.loads(res))
	




if __name__ == '__main__':
	X_names=json.load(open("X_names.json"))
	app.run(host='127.0.0.1',port=8080,debug=False)
