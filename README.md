# Introduction

This is a collection of data science web apps created using streamlit/dash etc.
All streamlit apps are compatible with either mobile or PC view.
View Themes can be changed by going into settings by clicking on the verticle ellipses on the top right corner of the webapp.

## Stock Application
Basic stock application that shows the company profile , stock price , volume , balance sheet , income statements , cash flow statements . divident history , option chain , upcoming earning events and recommendations for the stock ticker given by the user.
![image](https://github.com/Yash-29-10-2003/streamlit-apps/assets/89728102/4a86b314-0918-4b4a-98ed-135acfaf10ce)


## Basketball EDA
A Basketball Stat explorer that shows all the stats for nba players from seasons (1950-2023). Web scrapes this data from the basketball reference website and allows for precise filtering based on teams , positions. Allows downloading the filtered data [https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806] and shows top 10 players of the season based on different statistics (PPG, 3P%, and FG%). Also has data visualization options like scatter plots and intercorrelation heatmaps. 
![image](https://github.com/Yash-29-10-2003/streamlit-apps/assets/89728102/07b7aa27-b1f9-4de8-bc56-f97ed13a1f5e)
Inspiration : JxmyHighroller (YT)

## CryptoCurrency EDA
A crypto EDA that scrapes data from https://coinmarketcap.com [Web scraper adapted from the Medium article *[Web Scraping Crypto Prices With Python](https://towardsdatascience.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)* written by [Bryan Feng](https://medium.com/@bryanf)]. Allows users to see the price data and %change in price for the top 100 coins on the website. Users can filter their choice/number of cryptocurrency to be shown and bar plotted as well as the percentage change time frame values (7 Days , 1 Day , 1 Hour). Users can also download this filtered data as a csv. Has adaptive data visualization for %change using a bar graph which updates based on selected time frame.
![image](https://github.com/Yash-29-10-2003/streamlit-apps/assets/89728102/fae387bc-7d83-4b4e-8c3c-8b2836e067e8)

## Sales Dashboard
This task/project was done to acquire the Quantium Software Enginnering Simulation Certification @ Forage. 

All problem Statements @ [https://www.theforage.com/career-path/software-engineering/firms/quantium/simulations/software-engineering-j6ci]

Certification of Completion @ [https://drive.google.com/file/d/1GKpYa8QMttSPqY8u-qn8NMbpC-4fWrxP/view?usp=drive_link]
- Developed an interactive Dash application that enabled the client to assess the impact of price changes on sales and profitability.
- Implemented a test suite to verify the Dash application is working and a bash script to automatically run the test suite.
- Developed an intuitive user interface to make the application enjoyable and engaging for the client to interact with.
![image](https://github.com/Yash-29-10-2003/datascience-apps/assets/89728102/f03c40a6-e71f-4bbd-b630-8ce5dddb4dc1)

## ML Multi Page app
This application has 2 different ML regression models incorporated in it.
- **Iris Prediction:** This model predicts the species of iris flowers based on sepal and petal measurements.
- **Penguin Prediction:** This model predicts the species of penguins based on various features like flipper length, bill length, etc.

In the iris prediction app we use the iris dataset via iris = datasets.load_iris()
Users can select the Sepal and Petal length and widths for predicting the iris type using the random forest classifier.
![image](https://github.com/Yash-29-10-2003/datascience-apps/assets/89728102/e7bec73b-e471-4a9f-b4e1-13cfdc6d9de4)

In the penguine prediction app we generated pickle file after training the model on the cleaned penguins csv using Random Forest Classifier. Users can either input a csv file with their input vars as a dataframe or choose the values in the sidebar for the classification.
![image](https://github.com/Yash-29-10-2003/datascience-apps/assets/89728102/716cfdb8-b84d-4ac8-9742-cfa823210649)

# Deployment
Ive deployed some of the aforementioned apps as a test on streamlits own hosting platform . Links to deployed apps :

Stock APP : https://stockinfo.streamlit.app/

Basketball EDA APP : https://edabasketball.streamlit.app/
