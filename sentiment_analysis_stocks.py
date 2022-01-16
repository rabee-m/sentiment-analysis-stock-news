from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn import preprocessing
from datetime import datetime

#general url without the ticker
article_url = 'https://finviz.com/quote.ashx?t='

tickers = ['TSLA', 'AAPL', 'FB'] #tickers we will analyze

news_tables = {} #stores news headlines

#loops through each of our tickers and retrieves the html file containing
#all the news headlines and adds it to news_tables
for ticker in tickers:
    url = article_url + ticker
    
    req = (Request(url=url, headers={'user-agent': 'my-app'}))
    response = urlopen(req)
    
    html = BeautifulSoup(response, 'html')
    news_tables[ticker] = html.find(id='news-table') #add news headlines
    
#parse through the raw data, and extract relevant information about the title and time,
#storing it in parsed_data
parsed_data = []

for ticker, news_table in news_tables.items():
    
    for row in news_table.findAll('tr'):
        
        title = row.a.get_text()
        date_data = row.td.text.split()
        
        if len(date_data) == 1:
            #we only have data on time, not date
            time = date_data[0]
        else:
            #we have data on time, and date
            date = date_data[0]
            time = date_data[1]
        
        parsed_data.append([ticker, date, time, title])


#using pandas to store our parsed_data as a dataframe object
df = pd.DataFrame(parsed_data, columns=['ticker','date','time','title'])

#applying sentiment analysis using vader to create a new column in our dataframe, that has a
# score corresponding to the sentiment of the title
vader = SentimentIntensityAnalyzer()
df['compound'] = df['title'].apply(lambda title: vader.polarity_scores(title)['compound'])

df['date'] = pd.to_datetime(df.date).dt.date #converts date from string type to date type

#visualization of sentiment analysis
plt.figure(figsize=(10, 8))

#generate a new data frame that has average sentiment of articles for each ticker on each date
mean_df = df.groupby(['ticker', 'date']).mean()
mean_df = mean_df.unstack()
mean_df = mean_df.xs('compound', axis='columns').transpose()


#settings for the mean_df chart
avg_bar = mean_df.plot(kind='bar', color=['salmon','magenta','cyan'])
avg_bar.set_xlabel('Date')
avg_bar.set_ylabel('Average Sentiment of News Articles')
avg_bar.set_title('Average Sentiment of Stock Article (Jan 2021)')
avg_bar.grid('on')


#now we will plot the stock price of each stock ticker against the average sentiment price
for ticker in tickers:
    
    #pull stock data, and format it
    start_date = df['date'].min()
    end_date = df['date'].max()
    stock_data = pd.DataFrame(yf.download(ticker, start_date, end_date), columns=['Close'])
    stock_data = stock_data.round(2)
    d = preprocessing.normalize(stock_data, axis=0)
    scaled_stock_data = pd.DataFrame(d, columns=['Close Price'])
    #filter mean_df sentiment dataframe, so it only has relevent ticker we are currently analyzing
    ticker_df = mean_df[[ticker]].copy()
    
    ax = scaled_stock_data.plot(color='cyan')
    ticker_df.plot(kind='bar', ax=ax, color='salmon')
    ax.set_title(ticker+ ' price vs Average Sentiment Analysis of News Articles')
    ax.grid('on')
    
    
    
    #ax[1].plot(stock_data[])
    #stock_data.plot(kind='bar')
    #mean_df.plot(kind='bar')

plt.show()
    

