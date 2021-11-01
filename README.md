# Nialls Pattern Stock Screener
#### Video Demo:  <URL HERE>
#### Description: My final project for CS50 was a web based application using python,
#### flask and HTML similar to that of finance. I use TA-lib a library 
####for technical analysis, which contains the patterns and is able to identify what stocks from the s&p 500 correspond to a particular pattern by using the data in a csv file

## app.py
### This file parses through the s&p500.csv getting the open high low and close of each stock.
### It then uses TA-lib to analysis the info of each stock and see what pattern corresponds to the stock.
###

## patterns.py
### this file is a dictionary containing the names and symbols of all patterns

## index.html
### contains a for loop to iterate and display each stock that corresponds to the selected pattern
### used a img tag with a link to finviz that uses the stock in the url to show a graph of the stock a feature I was proud of

## styles.css
### used to add style to html page 