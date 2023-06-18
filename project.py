import pandas as pd
import requests
from bs4 import BeautifulSoup
import html5lib
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Question-01: Use yfinance to extract TESLA stock data
ticker_symbol = "TSLA"
tesla_data = yf.download(ticker_symbol)
tesla_data = tesla_data.reset_index()
print(tesla_data.head())

#Question 2: Use Webscraping to extract Tesla Revenue data

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2022-01-01"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html5lib')
tesla_revenue = pd.read_html(html_data, match="Tesla Quarterly Revenue")[0]
tesla_revenue.rename(columns={"Tesla Quarterly Revenue(Millions of US $)": "Date", "Tesla Quarterly Revenue(Millions of US $).1": "Revenue"}, inplace=True)
tesla_revenue.rename(columns={tesla_revenue.columns[1]: "Revenue"}, inplace=True)
tesla_revenue.rename(columns={tesla_revenue.columns[0]: "Date"}, inplace=True)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(',|\$', "", regex=True)
tesla_revenue["Date"] = tesla_revenue["Date"].str.replace(',|\$', "", regex=True)
print(tesla_revenue.tail())

#Question 3: Use yfinance to extract GME stock data
ticker_symbol = "GME"
gme_data = yf.download(ticker_symbol)
gme_data = gme_data.reset_index()
print(gme_data.head())

#Question 4: Use Webscraping to extract GME Revenue data
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2022-01-01"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html5lib')
gme_revenue = pd.read_html(html_data, match="GameStop Quarterly Revenue")[0]
gme_revenue.rename(columns={"GameStop Quarterly Revenue(Millions of US $)": "Date", "GameStop Quarterly Revenue(Millions of US $).1": "Revenue"}, inplace=True)
gme_revenue.rename(columns={gme_revenue.columns[1]: "Revenue"}, inplace=True)
gme_revenue.rename(columns={gme_revenue.columns[0]: "Date"}, inplace=True)
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(',|\$', "", regex=True)
gme_revenue["Date"] = gme_revenue["Date"].str.replace(',|\$', "", regex=True)
print(gme_revenue.tail())

#Question 5 & 6: Plot Tesla & GME Stock Graph
def make_graph(stock_data, revenue_data, stock_name):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"))

    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data['Date']), y=revenue_data['Revenue'].astype("float"), name="Revenue"), row=2, col=1)

    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US billions)", row=2, col=1)

    fig.update_layout(showlegend=False, height=600)
    fig.update_layout(title_text=stock_name + " Stock Graph")

    fig.show()

make_graph(tesla_data, tesla_revenue, 'Tesla')
make_graph(gme_data, gme_revenue, 'GameStop')