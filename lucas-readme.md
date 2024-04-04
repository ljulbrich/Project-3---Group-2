# Project-3---Group-2

Our proposal is written here:
https://docs.google.com/document/d/1966Fck0Z57jaAnJw_osNfomzqi6nW-hzQI0lGnqi5c8/edit?usp=sharing

### Long term view and sentiment analysis

The `long-term-price.html` page takes an input in the form of a stock ticker at the end of the URL. This then uses the flask `app.py` to run two python scripts.
The data from those python scripts are stored in the webpage and then passed to the two javascript files which create the graphs.

This file holds most of the relevant html and css aside from the navbar which is stored in `navbar.html`

#### `live_view.py` and `liveView.js`

`live_view.py` uses the python yfinance library to grab stock data from the last 10 years. The data is then saved as a JSON object and passed to the html file.

`liveView.js` takes the JSON object saved to the html and then converts the unix timestamp to a standard date fomat. It then graphs the JSON object using plotly.

#### `webscraper.py` and `wordCloud.js`

`webscraper.py` uses the python library selenium to grab the relevant news articles from yahoo finance stock tickers. It saves the title, blurb, and link in a list.
The blurb is then passed through a huggingface sentiment analysis transformer which returns the sentiment (either positive or negative) and the confidence score. These are both added to the list which is converted to a JSON object and stored in the html file.

`wordCloud.js` takes the json object from the html file and creates a wordcloud graph which shows the user which articles may have a positive or negative sentiment at a glance.

#### `eventListener.js`

This is copying Shawns first function in the main folder which listens to when the input is entered into the long term view search pannel.

#### Ethics

This web app uses publicly available data, however it is limited in scope as most of the financial data has been taken from yahoo finance.
The wordcloud sentiment analysis may not be accurate as the transformer hasn't been tuned to perform sentiment analysis on financial news data.
This being said, this application is a great resource for those who want to get a good overview of stock data and news.