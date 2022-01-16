<!-- ABOUT THE PROJECT -->
## About The Project
This project parses data from a stock news website, "https://finviz.com/" using BeautifulSoup. It then performs sentiment analysis on news headlines regarding stocks for 'TSLA', 'AAPL', 'FB', using nltk.vader and visualizing the data with matplotlib and pandas. This data is then plotted against stock prices retrieved from yfinance, and compares whether news headlines had a impact on the ticker price of the analyzed stocks. <br /> <br /> Inspiration from [Youtube](https://www.youtube.com/watch?v=o-zM8onpQZY&ab_channel=TheCodex)

### Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
* [Matplotlib](https://matplotlib.org/)
* [yfinance](https://pypi.org/project/yfinance/)
* [nltk](https://www.nltk.org/)

### Example Output:
![Average Sentiment of Stock_Article](https://user-images.githubusercontent.com/62624592/149677356-8d450164-81b1-4d61-90b6-053a8cdc97ea.png)
![TSLA_Sentiment](https://user-images.githubusercontent.com/62624592/149677358-7b0942a3-3d92-4710-b26b-326c7cdc1ec8.png)
![FB_Sentiment](https://user-images.githubusercontent.com/62624592/149677361-e141faf8-6cff-4397-96ba-970a25360103.png)
![Appl_Sentiment](https://user-images.githubusercontent.com/62624592/149677365-91146af9-4723-4161-bd67-bd89212ae0b9.png)

