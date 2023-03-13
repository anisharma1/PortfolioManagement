
# Importing module
import mysql.connector
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456"
)

cursor = mydb.cursor()

# Opening database
cursor.execute("USE portfoliomanagement")



# Fetching information from table
# Converting into database
cursor.execute("select * from valuation_stocks")
df = pd.DataFrame(cursor.fetchall(), columns = ['stockId', 'date', 'open', 'high', 'low', 'close', 'adj_close', 'volume'])

# DMA calculations
DMA={}
temp=0
temp1=[]
n= int(input("Enter n-day DMA:"))
for i in range(0,len(df)-n):
  temp=0
  for j in range(n):
    temp+=df["close"][i+j]
  DMA[df["date"][i+n]]=(temp/n)


# DMA plot using matplotlib
temp1=[]
for i in DMA.keys():
  temp1.append(DMA[i])
ypoints = np.array(temp1)

plt.plot(ypoints, color = 'b')
plt.xlabel("Date")  # add X-axis label
plt.ylabel("Averages")  # add Y-axis label
plt.title("DMA")  # add title
plt.show()


# Plots for stock chart movement
ypoints1 = np.array(df["close"])
ypoints2 = np.array(df["open"])
plt.plot(ypoints1, color = 'b')
plt.plot(ypoints2, color = 'r', linestyle = 'dotted')

plt.xlabel("Date")  # add X-axis label
plt.ylabel("Price")  # add Y-axis label
plt.title("Stock Chart movement of stock prices with date")  # add title
plt.show()


# Fetching information from table
# Converting into database
cursor.execute("select * from quarterly_data")
quarterly_data = pd.DataFrame(cursor.fetchall(), columns = ['stockID', 'dateMonthYear', 'netIncome',"sharesOutsanding" ])


# Plot for outstanding shares
ypoints1 = np.array(quarterly_data["sharesOutsanding"])
plt.plot(ypoints1, color = 'b')

plt.xlabel("Date")  # add X-axis label
plt.ylabel("Number of Shares")  # add Y-axis label
plt.title("Outstanding Shares")  # add title
plt.show()



# For converting net income string ti integer
def convert(temp):
  temp1=""
  flag=0
  for j in temp:
    if (flag==0 and j=='$'):
      flag=1
    elif (flag==1):
      temp1+=j
  # print(temp,temp1, ind1)
  return int(temp1)


# EPS calculations
EPS={}
for ind1 in quarterly_data.index:
  temp= convert(quarterly_data.loc[ind1]["netIncome"])
  EPS[quarterly_data.loc[ind1]["dateMonthYear"]]= temp/quarterly_data.loc[ind1]["sharesOutsanding"]

print("EPS")
print(EPS)


# Fetching information from table
# Converting into database
cursor.execute("select * from yearly_data")
df = pd.DataFrame(cursor.fetchall(), columns = ['StockID', 'Year', 'average_stock_value', 'outstanding_share'])

# For Market Capitalization
MarketCap={}
for ind1 in df.index:
  MarketCap[df.loc[ind1]["Year"]]= df.loc[ind1]["average_stock_value"]*df.loc[ind1]["outstanding_share"]

print("Market Capitalization")
print(MarketCap)

