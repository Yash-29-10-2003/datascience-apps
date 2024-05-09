import streamlit as st   #to build easy data science related webpages
import yfinance as yf   #yahoo finance , helps download stock market data
import pandas as pd    

#Adding content to the streamlit webpage. This is basic markup language (# acts as headline)
#https://www.markdownguide.org/cheat-sheet/
st.write("""
# Stock App

In this application you can study various informational and historical data about any stock of your choice in a concise manner !
""")

tickerSymbol = "GOOGL"
user_input = st.text_input("Add ticker here (GOOGL , AAPL , etc.) : ")

st.write("***")
#https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
tickerSymbol = user_input
tickerData = yf.Ticker(tickerSymbol)

#basic info regarding the stock
info = tickerData.info
st.markdown("""
    ## Company Profile
    * **Name:** {}
    * **Sector:** {}
    * **Industry:** {}
    * **Website:** [{}]({})
    * **Country:** {}
    * **Market Cap:** ${:,}
""".format(info['longName'], info['sector'], info['industry'], info['website'], info['website'], info['country'], info['marketCap']))

st.write("***")
#history function tells us about the historical data
#period: the frequency at which to gather the data;
#start: the date to start gathering the data.
#end: the date to end gathering the data
tickerDf = tickerData.history(period='1d', start='2014-4-30', end='2024-4-30')
# Open: the stock price at the beginning of that day/month/year
# Close: the stock price at the end of that day/month/year
# High: the highest price the stock achieved that day/month/year
# Low: the lowest price the stock achieved that day/month/year
# Volume: How many shares were traded that day/month/year
# Dividents , Stock Splits

#We can use the closing price to get a stock price chart
st.write("""
         ## Stock Price
         """)
st.line_chart(tickerDf.Close)
st.write("***")

#Volume traded
st.write("""
         ## Volume Traded
         """)
st.line_chart(tickerDf.Volume)
st.write("***")

#Balance Sheet
balance_sheet = tickerData.balance_sheet
st.write("""
    ## Balance Sheet
""")
st.dataframe(balance_sheet)
st.write("***")

#Income Statement
income_statement = tickerData.financials
st.write("""
    ## Income Statement
""")
st.dataframe(income_statement)
st.write("***")

#Cash Flow Statement
cash_flow_statement = tickerData.cashflow
st.write("""
    ## Cash Flow Statement
""")
st.dataframe(cash_flow_statement)
st.write("***")

#Dividends if available
dividends = tickerData.dividends
st.write("""
    ## Dividend History
""")
if not dividends.empty:
    st.write(dividends)
else:
    st.write("No dividend data available.")
st.write("***")

#Options if available
options = tickerData.options
st.write("""
    ## Option Chain Data
""")
if options:
    st.write(options)
else:
    st.write("No options data available.")
st.write("***")

#Upcoming Earnings
earnings_calendar = tickerData.calendar
earnings_df = pd.DataFrame(earnings_calendar)
st.write("""
    ## Upcoming Earnings Calendar
""")
st.write(earnings_df)
st.write("***")

#Recommendations
recommendations = tickerData.recommendations
st.write("""
    ## Recommendatios
""")
st.write(recommendations)