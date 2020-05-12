import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm

# # get the number of confirmed cases of covid-19
# covid_data = pd.read_csv("covid_confirmed_usafacts.csv")
# idx = covid_data.index[covid_data['State']=='NY']
# pre = idx[0]
# post = idx[-1]
# col_pre = covid_data.columns.get_loc("3/12/20")
# col_post = covid_data.columns.get_loc("4/30/20")
# NY_covid = covid_data.iloc[pre:post+1, col_pre:col_post+1].sum()
# NY_covid.columns = ['date', 'number of confirmed cases']
# NY_covid.to_csv('NY_covid.csv')

# get the number of confirmed cases of covid-19
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

# # get the number of tweets about covid-19
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

# analyze the correlation 
corr = pd.DataFrame()
covid_data = pd.read_csv("covid.csv")

tweets = pd.read_csv("tweets.csv")
states = pd.read_csv('states.csv')['Abbreviation'].to_numpy()

tweets = tweets['number of tweets with Covid'].to_numpy()
tweets = (tweets[1:] - tweets[:-1]) / tweets[:-1]
for s in states:
	covid = covid_data[s].values
	covid = (covid[1:] - covid[:-1] + 1) / (covid[:-1] + 1)
	cos_sim = dot(covid, tweets) /(norm(covid) * norm(tweets))
	corr[s] = [cos_sim]
corr = corr.T
corr.to_csv('correlation.csv', header=True)

