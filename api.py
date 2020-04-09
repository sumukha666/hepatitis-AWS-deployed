from flask import Flask, redirect, url_for, request
from sklearn.externals import joblib
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

filename = './liver_SVM.joblib.pkl'

svc_load = joblib.load(filename)
@app.route('/liver',methods=["POST"])
def sendLiverDetails():
	if request.method=="POST":
		liverDetails = (request.get_json(force=True));
		#print liverDetails
	
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
	
		print X
		
		res = svc_load.predict([X])
		print res
   	return "good"

if __name__ == '__main__':
   app.run()