import csv
from flask import Flask, render_template, request
import os
import pandas as pd
import yfinance as yfin
from momentums import momentums
import talib

app = Flask(__name__)


@app.route("/")
def index():
    momentum= request.args.get('momentum', None)
    stocks = {}

    with open('data/s&p500.csv') as file:
        for row in csv.reader(file):
            stocks[row[0]] = {'company': row[1]}
    if momentum:
        data_files = os.listdir('data\daily')
        for data in data_files:
            df = pd.read_csv(f'data/daily/{data}')
            momentum_function = getattr(talib, momentum)
            symbol = file.split('.')[0]
            try:
                result = momentum_function(df['Open'], df['High'], df['Low'], df['Close'])
                last = result.tail(1).values[0]
                #print(last)
                if last > 0:
                    stocks[symbol][momentum] = 'Has momentum'
                elif last < 0:
                    stocks[symbol][momentum] = 'Does not have momentum'
                else:
                    stocks[symbol][momentum] = None
            except:
                pass
    return render_template('index.html', momentums=momentums, stocks=stocks)


@app.route('/capture')
def capture():
    with open('data/s&p500.csv') as f:
        symbols = f.read().splitlines()
        for symbol in symbols:
            ticker = symbol.split(',')[0]
            df = yfin.download(ticker, start="2021-01-01", end="2021-10-19")
            df.to_csv('data/daily/{}.csv'.format(ticker))

    return {
        'code': 'success'
    }
