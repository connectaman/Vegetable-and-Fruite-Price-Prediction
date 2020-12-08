#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:21:51 2020

@author: amanulla
"""

from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import joblib
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=["GET","POST"])
def predicts():
    if request.method == "POST":
        # Getting the Data via POST Request
        print(request.form)
        item = request.form.get('item')
        df = pd.read_csv('data/Predict_vegetable_2020_price.csv')
        price = float(df[df['Item Name'] == item]['price'])
        price = "Price of %s is ₹ %.2f"%(item,price)
        return render_template('index.html',data = str(price))
    
    

if __name__ == '__main__':
    app.run()