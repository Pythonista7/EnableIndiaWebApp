from flask import Flask,render_template,request,json,render_template_string,redirect,jsonify
import json


"""
labels:['highest_education_S.S.L.C', 'disability_type_MR (Mental Retardation)', 'recommended_job_types_SEMI SKILLED MORE INTERACTION', 'disability_sub_type_PROFOUND (wheelchair+helper/other disability)']
"""

from EIML.EIML import EIML


mlapp=Flask(__name__)
mlapp.static_folder = 'static'


@mlapp.route("/api/Attributes",methods=["GET"])
def get_Attributes():
	try:
		with open('EIML/X_names.json') as f:
			file_data = f.read()
	except:
		file_data = "could not read file"
	return jsonify(file_data)

@mlapp.route("/api/Jobs",methods=["GET"])
def get_Jobs():
	try:
		with open('EIML/y_names.json') as f:
			file_data = f.read()
	except:
		file_data = "could not read file"
	return jsonify(file_data)

@mlapp.route("/api/predict",methods=["POST"])
def predict():	

	if request.method=="POST":
		data=request.get_json()['labels']
		print("Check\ndata=",data,"\n\n")
		attr=list(data)
		print("\n\n\nLabels = ",attr)
		model=EIML()
		res=model.predict(attr)
		#print("CHECK@==>",res)
		return jsonify({'status': 200,'message': 'OK',"res":json.dumps(res,default=model.convert)}) #render_template("jobs.html",jobs=res)





if __name__ == '__main__':
	mlapp.run(host='127.0.0.1',port=9090,debug=False)
