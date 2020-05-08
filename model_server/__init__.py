
from flask import Flask,render_template,request,json,render_template_string,redirect,jsonify
import json

from .EIML.EIML import EIML


def create_app():
    app_name = 'mlapp'
    print('app_name = {}'.format(app_name))

    # create app
    mlapp = Flask(__name__, instance_relative_config=True)


    @mlapp.route("/api/Attributes",methods=["GET"])
    def get_Attributes():
        try:
            with open('model_server/EIML/X_names.json') as f:
                file_data = f.read()
        except:
            file_data = "could not read file"
        return jsonify(file_data)

    @mlapp.route("/api/Jobs",methods=["GET"])
    def get_Jobs():
        try:
            with open('model_server/EIML/y_names.json') as f:
                file_data = f.read()
        except:
            file_data = "could not read file"
        return jsonify(file_data)

    @mlapp.route("/api/predict",methods=["POST"])
    def predict():	
        # if request.method=='GET':
        #     data=request.form.values()
        #     attr=list(data)
        #     #print(attr)
        #     #res=req.post("http://localhost:5000/ml/api/predict",json={'labels':attr})
        #     #res=res.json()['res']
        #     model=EIML()
        #     res=model.predict(attr)
        #     print("\n\n\n**",res,"**\n\n")
        #     return render_template("jobs.html",jobs=res)
        


        if request.method=="POST":
            #print('DOING ML\n\n')
            data=request.get_json()['labels']
            #print("Check\ndata=",data,"\n\n")
            attr=list(data)
            #print("\n\n\nLabels = ",attr)
            model=EIML()
            res=model.predict(attr)
            #print("CHECK@==>",res)
            return jsonify({'status': 200,'message': 'OK',"res":json.dumps(res,default=model.convert)}) #render_template("jobs.html",jobs=res)


    return mlapp