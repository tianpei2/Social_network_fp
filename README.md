# Social_network_fp

## Date Source

Covid-19 data source: https://data.beta.nyc/pages/nyc-covid19  
Twiiter scraper source: https://www.kaggle.com/smid80/coronavirus-covid19-tweets

## Input

#### tweets

raw data of tweets

#### weather

raw data of weather for counties: New York, Queens, Suffolk, Westchester

#### covid_confirmed_usafacts.csv

covid-19 comfrimed cases dataset

#### states.csv

map from states name to Abbreviation

## Data cleaning (from 3/12 to 4/30 )

#### covid.csv

number of confrimed cases of Covid-19

#### tweets.csv

number of tweets with hashtags: #coronavirus, #coronavirusoutbreak, #coronavirusPandemic, #covid19, #covid_19

#### cleaned_weather

with attributes: humidity, visibility, temperature, pressure

## Output (correlation)

#### correlation.csv

correlation between increasing rate of number of confrimed cases and tweets w.r.t each state

#### LinearRegression.csv

linear relationship between total number of confrimed cases and tweets w.r.t each state

#### correlation_of_weather_and_covid19.csv

correlation between increasing rate of number of confrimed cases and tweets w.r.t certain county
