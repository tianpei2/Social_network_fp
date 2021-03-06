import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm
from sklearn.linear_model import LinearRegression
import glob

# ##################### Part 1: get the number of confirmed cases of covid-19 ####################
# covid_data = pd.read_csv("covid_confirmed_usafacts.csv")
# idx = covid_data.index[covid_data['State']=='NY']
# pre = idx[0]
# post = idx[-1]
# col_pre = covid_data.columns.get_loc("3/12/20")
# col_post = covid_data.columns.get_loc("4/30/20")
# NY_covid = covid_data.iloc[pre:post+1, col_pre:col_post+1].sum()
# NY_covid.columns = ['date', 'number of confirmed cases']
# NY_covid.to_csv('NY_covid.csv')

# #################### Part 2: get the number of confirmed cases of covid-19 for all states ####################
# states = pd.read_csv('states.csv')['Abbreviation'].to_numpy()
# covid = pd.DataFrame()
# print(covid)
# for s in states:
# 	covid_data = pd.read_csv("covid_confirmed_usafacts.csv")
# 	print(s)
# 	idx = covid_data.index[covid_data['State']==s]
# 	pre = idx[0]
# 	post = idx[-1]
# 	col_pre = covid_data.columns.get_loc("3/12/20")
# 	col_post = covid_data.columns.get_loc("4/30/20")
# 	covid[s] = covid_data.iloc[pre:post+1, col_pre:col_post+1].sum()
# covid.to_csv('covid.csv', header=True)

# ##################### Part 3: get the number of tweets about covid-19 ####################
# date1 = '2020-03-12'
# date2 = '2020-04-30'
# mydates = pd.date_range(start=date1, end=date2).strftime('%Y-%m-%d').tolist()
# tweets = np.zeros(len(mydates))
# cnt = 0
# for d in mydates:
# 	file_name = 'tweets/{} Coronavirus Tweets.CSV'.format(d)
# 	ts = pd.read_csv(file_name)
# 	tweets[cnt] = ts.shape[0]
# 	cnt +=1

# tweets = {'date' : pd.Series(mydates), 'number of tweets with Covid': pd.Series(tweets)}
# tweets = pd.DataFrame(tweets)
# tweets.to_csv('tweets.csv')

# ##################### Part 4: analyze the correlation ####################
# corr = pd.DataFrame()
# covid_data = pd.read_csv("covid.csv")

# tweets = pd.read_csv("tweets.csv")
# states = pd.read_csv('states.csv')['Abbreviation'].to_numpy()

# tweets = tweets['number of tweets with Covid'].to_numpy()
# tweets = (tweets[1:] - tweets[:-1]) / tweets[:-1]
# for s in states:
# 	covid = covid_data[s].values
# 	covid = (covid[1:] - covid[:-1] + 1) / (covid[:-1] + 1)
# 	cos_sim = dot(covid, tweets) /(norm(covid) * norm(tweets))
# 	corr[s] = [cos_sim]
# corr = corr.T
# corr.to_csv('correlation.csv', header=True)

# #################### Part 5: analyze in terms of linear regression ####################
# corr = pd.DataFrame()
# covid_data = pd.read_csv("covid.csv")

# tweets = pd.read_csv("tweets.csv")
# states = pd.read_csv('states.csv')['Abbreviation'].to_numpy()
# tweets = tweets['number of tweets with Covid'].to_numpy().reshape((-1, 1))

# for s in states:
# 	regressor = LinearRegression()
# 	covid = covid_data[s].values.reshape((-1, 1))
# 	regressor.fit(tweets, covid) #training the algorithm
# 	corr[s] = [regressor.coef_[0][0], regressor.intercept_[0]]

# corr = corr.T
# corr.to_csv('LinearRegression.csv', header=True)


# #################### Part 6: clean the weather data ####################
# input_path = 'weather' # use your path
# all_files = glob.glob(input_path + "/*.csv")
# output_path = 'cleaned_weather/'

# for filename in all_files:
# 	weather_data = pd.read_csv(filename)
# 	weather_data = weather_data[['DATE', "HourlyAltimeterSetting", "HourlyDewPointTemperature", "HourlyDryBulbTemperature", "HourlyRelativeHumidity", "HourlySeaLevelPressure", "HourlyStationPressure", "HourlyVisibility", "HourlyWetBulbTemperature", "HourlyWindDirection"]]
# 	weather_data['DATE'] = pd.to_datetime(weather_data['DATE']).dt.floor('d')

# 	for c in ["HourlyAltimeterSetting", "HourlyDewPointTemperature", "HourlyDryBulbTemperature", "HourlyRelativeHumidity", "HourlySeaLevelPressure", "HourlyStationPressure", "HourlyVisibility", "HourlyWetBulbTemperature", "HourlyWindDirection"]:
# 		weather_data[c] = weather_data[c].apply (pd.to_numeric, errors='coerce')
# 		weather_data[c] = weather_data[c].dropna()
# 	weather_data = weather_data.groupby('DATE').mean()
# 	out_file = output_path + filename.split('/')[-1]
# 	weather_data.to_csv(out_file)

# #################### Part 7: analyze correlation between weather and covid-19 ####################
input_path = 'cleaned_weather/' # use your path
all_files = glob.glob(input_path + "/*.csv")
counties = [f.split('/')[-1].split('.')[0] for f in all_files]

# covid_data = pd.read_csv("covid_confirmed_usafacts.csv")
# col_pre = covid_data.columns.get_loc("3/12/20")
# col_post = covid_data.columns.get_loc("4/30/20")
# covid = pd.DataFrame()

# for c in counties:
# 	co = covid_data[(covid_data['County Name'] == c) & (covid_data['State'] == 'NY')]
# 	covid = pd.concat([covid, co])

# covid = covid.iloc[:, col_pre:col_post+1]
# covid = covid.T
# covid.to_csv('county_covid.csv')


corr = pd.DataFrame(columns = ["humidity", "visibility", "temperature", "pressure"], index = ["Suffolk County", "Queens County", "New York County", "Westchester County"])
covid = pd.read_csv('county_covid.csv') 

for filename in all_files:
	c = filename.split('/')[-1].split('.')[0]
	covid19 = covid[c].values
	covid19 = (covid19[1:] - covid19[:-1] + 1)/ (covid19[:-1] + 1)
	weather_data = pd.read_csv(filename)

	h = weather_data["HourlyRelativeHumidity"].values
	h = (h[1:] - h[:-1]) / h[:-1]
	corr.at[c, "humidity"] = dot(covid19, h) /(norm(covid19) * norm(h))

	v = weather_data["HourlyVisibility"].values
	v = (v[1:] - v[:-1]) / v[:-1]
	corr.at[c, "visibility"] = dot(covid19, v) /(norm(covid19) * norm(v))


	t = weather_data["HourlyWetBulbTemperature"].values
	t = (t[1:] - t[:-1]) / t[:-1]
	corr.at[c, "temperature"] = dot(covid19, t) /(norm(covid19) * norm(t))

	p = weather_data["HourlyStationPressure"].values
	p = (p[1:] - p[:-1]) / p[:-1]
	corr.at[c, "pressure"] = dot(covid19, p) /(norm(covid19) * norm(p))

corr.to_csv('correlation of weather and covid19.csv')


