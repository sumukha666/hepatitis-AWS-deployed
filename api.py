from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/liver',methods=["POST"])
def sendLiverDetails():
	if request.method=="POST":
		liverDetails = (request.get_json(force=True));
		print(liverDetails)
   	return "worked"

if __name__ == '__main__':
   app.run()