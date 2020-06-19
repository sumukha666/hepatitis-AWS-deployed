from flask import Flask, redirect, url_for, request, render_template
from sklearn.externals import joblib
import json

app = Flask(__name__)

filename = './liver_SVM.joblib.pkl'

svc_load = joblib.load(filename)

@app.route('/',methods=["GET"])
def home_func():
	return render_template("homepage.html")
	


@app.route('/liver',methods=["POST"])
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

		res = svc_load.predict([X])
   		if res[0]:
				return "you're liver is Damaged"
		else:
				return "you're liver is functioning well"

if __name__ == '__main__':
   app.run()
