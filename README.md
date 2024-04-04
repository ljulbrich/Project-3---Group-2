# Project-3---Group-2

Our proposal is written here:
https://docs.google.com/document/d/1966Fck0Z57jaAnJw_osNfomzqi6nW-hzQI0lGnqi5c8/edit?usp=sharing

# Webpage Backend

# 1.The blueprint of the whole project

* The idea of the project is to build a website thats similar to Yahoo Finance.
* yfinance is a python library that fuctions as an API to request data from Yahoo Finance.
* Python flask is the power engine thats used to build the website, 
  so that we can process data in the backend using python, and plotting graphs using pandas or matplotlib
* The data returned from yfinance can be passed to html paage and calling javascript function to further plotting those data.
* MongoDB is used to store data from user input on the website, and it also stores data from a csv file that has all the basic information from companies in Nasdaq.
* In summary, python flask is the backend to process the data, javascript is used to make the website interactive, and mongo DB is the database for this website.

# 2. The Earnings vs Revenues graph and Company details

* The start of the project is make a simple route ("/") in app.py, and run it on my local host.
* In my scrath jupyter notebook, I have tested different commands that do API requests.
![Screenshot of scratchbook](screenshots/scratch1.png)
* I have found the income statement to be particularly useful
![Screenshot of scratchbook](screenshots/scratch2.png)
* I use the earnings(income) and total revenues to plot a matplotlib 
* The above codes are collected and put into a python function in xiang.py as one of my methods
* The image data is transferred from python to javascript by using base64 class
![Screenshot of xiang.py](screenshots/er_plot1.png)
![Screenshot of xiang.py](screenshots/er_plot2.png)
* The image is dynamically generated and correctly displayed on the webpage
![Screenshot of xiang.py](screenshots/er_plot3.png)
* Since the image is displayed correctly, the next step is passing a json file that contains all the company details
![Screenshot of xiang.py](screenshots/details1.png)
* The function is called in app.py and passed down to html page to be handled by javascript
* The idea to handle this data is to dynamically generate a table in javascript that holds all of this data
![Screenshot of main.js](screenshots/details2.png)
* And the final table looks like this:
![Screenshot of webpage](screenshots/details3.png)
* The problem with this table is that not all stocks have the some data fields, for example some stocks dont have bid price, and some dont have revenues, etc.
* Data validation needs to be implemented for future improvements
* Since the table and the plt graph is processed successfully, it is time to apply some css to the page.
![Screenshot of main.html](screenshots/main_style.png)
* On the webpage is diaplayed like below (at the time, the news section wasnt added):
![Screenshot of webpage](screenshots/main_style2.png)

# 3. The news section

* Since the company details and the earnings graph only occupy 2/3 of the width of the page
* Another section I chose is the news, because when people check the stock, they would like to know some news about that company.
* The stock news is retrieved from yfinace as well, since it has a particular command for news.
![Screenshot of scratchbook](screenshots/news1.png)
* The difficulties here are to understand the data structure of the returned news.
![Screenshot of scratchbook](screenshots/news2.png)
* And how to handle the url when there is no image available for the particular stock.
* This final function is showing as down below:
![Screenshot of xiang.py](screenshots/news3.png)
* This function will be called in the app.py under the main route:
![Screenshot of xiang.py](screenshots/news4.png)
* How to handle the news data was quite a challenge in Javascript, because I want to make a dropdown menu to display the page number
* The page number will be furtherly used to slice the original news data to properly choose the range of the list
![Screenshot of xiang.py](screenshots/news5.png)
* I want the dropdown menu to be dynamically created, because the each stock has different number of news
* After the dropdown menu is created, it will do an initial call of the createNews function, so the news section shows first 3 news by default.
* And the createNews function takes in two arguments, page number and news data, because I need the page number to slice the news data
![Screenshot of xiang.py](screenshots/news6.png)
* The only problem here is when user select another page, how do we parse the selected value to re-call the function?
* The function is handled in Javascript
![Screenshot of main.js](screenshots/news7.png)
* But how to call the function is the thing I need to consider, and it is handled this way in the html:
![Screenshot of main.html](screenshots/news8.png)
* Eventually, the news section is displayed like this:
![Screenshot of webpage](screenshots/news9.png)

# 4. The index page and navigation bar

* The index page is designed to be like Google. The user will input the ticker of the stock he wants to search, and the the page will be directed to main page.
* And the there will be some quick access buttons under the search bar that can quickly direct to each group member's work.
![Screenshot of webpage](screenshots/index1.png)
* The input bar is designed to be like google, so when user press 'enter' key, the page should redirect.
* To do that, I add a key listener to this input box. And a safety check is also added to prevent the user doing an empty search.
![Screenshot of logic.js](screenshots/index2.png)
* And finally, I add some styles to the index page:
![Screenshot of index.html](screenshots/index3.png)
* After the index page, I designed a navigation bar and the same search bar in embeded in the navigation bar
* The navigation bar is saved in its own nav.html page, so we do need to copy paste the codes around.
![Screenshot of webpage](screenshots/nav1.png)
* The final navigation bar is like (the long term seach bar is added by another member):
![Screenshot of webpage](screenshots/nav2.png)

# 5. The trading simulator

* The trading simulator is designed to fuction as a broker application
* In this page, we would have a random company chosen from Nasdaq market, and its historic price (both high and low are displayed).
![Screenshot of webpage](screenshots/trade1.png)
* And there is a form to record the user's input, and the data would be stored in Mongo DB.
![Screenshot of webpage](screenshots/trade2.png)
* To discuss the technical details behind the page, the first thing I did was to seach for a dataset that has all of basic info of Nasdaq companies
* It is a csv file thats downloaded from Nasdaq official site, and inserted into the database by a one line code
* I use pymongo to extract the company data from the database
![Screenshot of webpage](screenshots/trade4.png)
![Screenshot of webpage](screenshots/trade3.png)
* The function is called in the app.py and data is passed to the javascript to plot the graph
![Screenshot of webpage](screenshots/trade5.png)
* A form is created to collect user's trading request
![Screenshot of webpage](screenshots/trade6.png)
* The user input data will be stored into Mongo DB after submission
![Screenshot of webpage](screenshots/trade7.png)
* And a thank you page with a go back will take the user back to the main page
![Screenshot of webpage](screenshots/trade8.png)


# Long term view and sentiment analysis

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

# Top 20 ASX Stocks

This page provides an overview of the top 20 ASX stocks with the largest market cap.
The dataset used to obtain the ASX code of all the listed shares are downloaded from Market Index (https://www.marketindex.com.au/data-downloads).
To obtain comprehensive information of all the ASX stocks, Yahoo Finance API is used. It provides a lot of information and data. To provide the users a quick and general view of the stock information, the following data/information are obtained from Yahoo Finance API: ASX code, name, industry, sector, market cap, employee count, revenue, price, volume, P/E ratio, earnings per share, and return on equity. A cleaned dataset is created and saved as a csv file for further analysis.
The csv file of all the ASX stocks is imported into MongoDB for storage. Python is used to retrieve data from MongoDB. All the table and charts are then created by sorting the top 20 largest market cap stocks.

# Footware stocks analysis

1. The blue graph shows the current price of footwear stocks in the US stock market. In the case, Deck is really at a high price. The current price helps the investors make decisions.
2. The PE Ratio is shown in the green graph. In the graph, On holding AG has a high PE ratio but is not overvalued while Weyco group is at a low PE ratio because of the insider's trading. They are different from what we learn in the textbook.
3. The 52 week change see the stock's long term performance. Deck has a high percentage because of its boosting business while Nike underrated the wholesales business which results in its low 52 week change

# The end

* The project is designed to simulate Yahoo Finance, and the final website is fully functional and provide the same function as Yahoo Finance
* However, there are some places need to be improved, especially the data validation part.
