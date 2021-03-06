import os, csv
import talib
import yfinance as yf
import pandas
from flask import Flask, request, render_template
from patterns import candlestick_patterns

app = Flask(__name__)


@app.route('/capture')
def capture():
    with open('data/s&p500.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            data = yf.download(symbol, start="2020-01-01", end="2020-08-01")
            data.to_csv('data/daily/{}.csv'.format(symbol))

    return {
        "code":"compiled"
    }


@app.route('/')
def index():
    pattern = request.args.get('pattern', False)
    stocks = {}

    with open('data/s&p500.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}

    if pattern:
        for FILE in os.listdir('data/daily'):
            df = pandas.read_csv(f'data/daily/{FILE}')
            pattern_function = getattr(talib, pattern)
            ticker = FILE.split('.')[0]

            try:
                results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                company_check = results.tail(1).values[0]

                if company_check > 0:
                    stocks[ticker][pattern] = 'bullish'
                elif company_check < 0:
                    stocks[ticker][pattern] = 'bearish'
                else:
                    stocks[ticker][pattern] = None
            except Exception as e:
                print(f'Pattern failed on :{FILE} no pattern found in this file')


    return render_template('index.html', candlestick_patterns=candlestick_patterns, stocks=stocks, pattern=pattern)
