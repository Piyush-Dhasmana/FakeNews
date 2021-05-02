# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:21:05 2021

@author: PIYUSH
"""
import sys
print(sys.path)
import pickle
import requests
from flask import Flask, render_template, request
import nltk
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords
import numpy as np

ps = PorterStemmer()
nltk.download("wordnet")
nltk.download("stopwords")
nltk.download('punkt')

classifier = pickle.load(open( 'NBmodel.pkl', 'rb'))
tfidf =pickle.load(open( 'tfid.pickle', 'rb'))
app= Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def search():
    Title=[request.form["Title"]]
    Description=[request.form["News"]]
    
    a=["my name is piyush football"]
    b=["Hello How $ARe matrix"]
    data=a+b
    data
    " ".join(data)
    
    data= re.sub(r'[^a-zA-Z]', ' ',str(data))
    data= data.lower()
    data= data.split()
    data
    List=[]
    for word in data:
        if word not in stopwords.words('english'):
            a=ps.stem(word) 
            List.append(a)
    
    ab=[" ".join(List)]
    ab
    data1=tfidf.transform(ab).toarray()
    data1.shape
    tfidf.get_feature_names()
    fake_real=classifier.predict(data1)
    fake_real
    if fake_real==1:
        return render_template('index.html', prediction="It is the real news")
    else:
        return render_template('index.html', prediction="Don't believe in this")
    


# It is called terminated extension
if __name__ == "__main__":
    app.run(debug=True)
   
    
    
    
    
    
    
    
    