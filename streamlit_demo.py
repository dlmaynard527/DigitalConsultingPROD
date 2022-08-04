# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 13:40:05 2022

@author: dlmaynard
"""

import yfinance as yf
import streamlit as st
#import pandas as pd

st.write()

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

st.line_chart(tickerDF.Close)

st.line_chart(tickerDF.Volume)

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


import yfinance as yf
from PIL import Image,ImageDraw 
import datetime as dt
import pandas as pd

# ticker to input
ticker = 'ATEX'

# initiate ticker
ticker_value = yf.Ticker(ticker)

market_cap = ticker_value.info['marketCap']

pop = 334805269 * 6

value = market_cap /pop

# create dateframe of last hour of stock prices
df= ticker_value.history(period='7d',interval='1m')

# reset index
df = df.reset_index()

df.tail(1)

# locate most recent minute's closing price
close_price = round(df.iloc[-1,4],2)

# locate most recent date and time
date_time = dt.datetime.strftime(df.iloc[-1,0], '%A %b %d, %Y %r ET')

# create blank image
import numpy as np

width = 1400
height = 1000

array = np.zeros([height, width, 3], dtype=np.uint8)

array[:,:] = [0, 0, 0]

# array to image
img = Image.fromarray(array)

# create font
#font = ImageFont.truetype("arial.ttf", 80)
#font2 = ImageFont.truetype("arial.ttf", 40)

# draw on image and show
d1 = ImageDraw.Draw(img)
d1.text((400, 300), str(date_time), fill=(255, 255, 255))
d1.text((600, 400), ticker, fill=(255, 255, 255))
d1.text((250, 500), "Implied Evaluation: $"+str(round(value,4)), fill=(255, 255, 255))
st.image(img)