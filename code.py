import numpy as np
import pandas as pd

covid_data = pd.read_csv("covid_confirmed_usafacts.csv")
idx = covid_data.index[covid_data['State']=='NY']
pre = idx[0]
post = idx[-1]
col_pre = covid_data.columns.get_loc("3/12/20")
col_post = covid_data.columns.get_loc("4/30/20")
NY_covid = covid_data.iloc[pre:post+1, col_pre:col_post+1].sum()
NY_covid.columns = ['date', 'number of confirmed cases']
NY_covid.to_csv('NY_covid.csv')


date1 = '2020-03-12'
date2 = '2020-04-30'
mydates = pd.date_range(start=date1, end=date2).strftime('%Y-%m-%d').tolist()
tweets = np.zeros(len(mydates))
cnt = 0
for d in mydates:
	file_name = 'tweets/{} Coronavirus Tweets.CSV'.format(d)
	ts = pd.read_csv(file_name)
	tweets[cnt] = ts.shape[0]
	cnt +=1

tweets = {'date' : pd.Series(mydates), 'number of tweets with Covid': pd.Series(tweets)}
tweets = pd.DataFrame(tweets)
tweets.to_csv('tweets.csv')


