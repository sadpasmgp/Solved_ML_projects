from flask import Flask,render_template,url_for,request,jsonify

import pandas as pd
import numpy as np
import datetime
import pickle


model = pickle.load(open("rain_XGBnew_model.pkl", "rb"))
app = Flask(__name__, template_folder="template")

@app.route("/",methods=['GET'])

def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])

def predict():
	if request.method == "POST":
		# DATE
		date = request.form['date']
		day = float(pd.to_datetime(date, format="%Y-%m-%dT").day)
		month = float(pd.to_datetime(date, format="%Y-%m-%dT").month)
		# MinTemp
		minTemp = float(request.form['mintemp'])
		# MaxTemp
		maxTemp = float(request.form['maxtemp'])
		# Rainfall
		rainfall = float(request.form['rainfall'])
		# Evaporation
		evaporation = float(request.form['evaporation'])
		# Sunshine
		sunshine = float(request.form['sunshine'])
		# Wind Gust Speed
		windGustSpeed = float(request.form['windgustspeed'])
		# Wind Speed 9am
		windSpeed9am = float(request.form['windspeed9am'])
		# Wind Speed 3pm
		windSpeed3pm = float(request.form['windspeed3pm'])
		# Humidity 9am
		humidity9am = float(request.form['humidity9am'])
		# Humidity 3pm
		humidity3pm = float(request.form['humidity3pm'])
		# Pressure 9am
		pressure9am = float(request.form['pressure9am'])
		# Pressure 3pm
		pressure3pm = float(request.form['pressure3pm'])
		# Temperature 9am
		temp9am = float(request.form['temp9am'])
		# Temperature 3pm
		temp3pm = float(request.form['temp3pm'])
		# Cloud 9am
		cloud9am = float(request.form['cloud9am'])
		# Cloud 3pm
		cloud3pm = float(request.form['cloud3pm'])
		# Cloud 3pm
		location = float(request.form['location'])
		if(location == 'Portland'):
			location = 1
		elif(location == 'Cairns'):
			location = 2
		elif(location == 'Walpole'):
			location = 3
		elif(location == 'Dartmoor'):
			location = 4
		elif(location == 'MountGambier'):
			location = 5
		elif(location == 'NorfolkIsland'):
			location = 6
		elif(location == 'Albany'):
			location = 7
		elif(location == 'Witchcliffe'):
			location = 8
		elif(location == 'CoffsHarbour'):
			location = 9
		elif(location == 'Sydney'):
			location = 10
		elif(location == 'Darwin'):
			location = 11
		elif(location == 'MountGinini'):
			location = 12
		elif(location == 'NorahHead'):
			location = 13
		elif(location == 'Ballarat'):
			location = 14
		elif(location == 'GoldCoast'):
			location = 15
		elif(location == 'SydneyAirport'):
			location = 16
		# Wind Dir 9am
		winddDir9am = float(request.form['winddir9am'])
		if(winddDir9am == 'NMW'):
			winddDir9am == 0
		elif(winddDir9am== 'NW'):
			winddDir9am == 1
		elif(winddDir9am== 'WNW'):
			winddDir9am == 2
		elif(winddDir9am== 'N'):
			winddDir9am == 3
		# Wind Dir 3pm
		winddDir3pm = float(request.form['winddir3pm'])
		if(winddDir3pm== 'NW'):
			winddDir3pm == 0
		elif(winddDir3pm== 'NNW'):
			winddDir3pm == 1
		elif(winddDir3pm == 'N'):
			winddDir9am == 2
		elif(winddDir3pm== 'WNW'):
			winddDir3pm == 3
		# Wind Gust Dir
		windGustDir = float(request.form['windgustdir'])
		if(windGustDir== 'NNW'):
			windGustDir == 0
		elif(windGustDir == 'NW'):
			windGustDir == 1
		elif(windGustDir== 'WNW'):
			windGustDir == 2
		elif(windGustDir== 'N'):
			windGustDir == 3
		# Rain Today
		rainToday = float(request.form['raintoday'])
		if(rainToday== 'Yes'):
			rainToday== 1
		elif(rainToday== 'No'):
			rainToday== 0

		input_lst = [location , minTemp , maxTemp , rainfall , evaporation , sunshine ,
					 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
					 humidity9am , humidity3pm , pressure9am , pressure3pm , cloud9am , cloud3pm , temp9am , temp3pm ,
					 rainToday , month , day]
		pred = model.predict(input_lst)
		output = pred

	if output == 0:
		return render_template("after_sunny.html")
	else:
		return render_template("after_rainy.html")


if __name__=='__main__':
	app.run(debug=True)