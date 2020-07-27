from flask import Flask, redirect, url_for, request, render_template
from sklearn.externals import joblib
import decimal
import json

app = Flask(__name__)

filename = './liver_svc_proba.joblib.pkl'

svc_load = joblib.load(open(filename,'rb'))

@app.route('/',methods=["GET"])
def home_func():
	return render_template("main.html")
	


@app.route('/liver',methods=["POST", "GET"])
def sendLiverDetails():
	if request.method=="POST":
		liverDetails = (request.get_json(force=True));
		#print liverDetails
		#print(liverDetails)
	
		X = []
		X.append(liverDetails['Age'])
		X.append(liverDetails['Gender'])
		X.append(liverDetails['Total_Bilirubin'])
		X.append(liverDetails['Direct_Bilirubin'])
		X.append(liverDetails['Alkaline_Phosphotase'])
		X.append(liverDetails['Alamine_Aminotransferase'])
		X.append(liverDetails['Aspartate_Aminotransferase'])
		X.append(liverDetails['Total_Protiens'])
		X.append(liverDetails['Albumin'])
		X.append(liverDetails['Albumin_and_Globulin_Ratio'])
		
		for i in liverDetails:
			if liverDetails[i] == "":
				return "Please enter " + i + " details"

		# res = svc_load.predict([X])
		res = svc_load.predict_proba([X])
		y= round(decimal.Decimal(res[0][0])*100,2)
		stng = "There are " + str(y) +  "%" +" chance of Liver Damage"
		return stng
   		# if res[0]==1:
		# 		return "your liver is Damaged"
		# else:
		# 		return "your liver is functioning well"
	if request.method == "GET":
		return render_template("liver.html")
			
# @app.route('/liver',methods=["GET"])
# def liver_page():
	

@app.route('/help',methods=["GET"])
def liver_page():
	return render_template("help.html")


if __name__ == '__main__':
   app.run()
