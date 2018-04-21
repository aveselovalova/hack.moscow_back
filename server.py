import nltk
from nltk import word_tokenize, pos_tag, pos_tag_sents
from nltk.tree import Tree
from textblob import TextBlob
import json
import requests
import PIL
import datetime
import time
import random
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'index.html'

@socketio.on('firstConnect')
def handleMessage(msg):
    print ("# User Connected ...")
    
@socketio.on('getImage')
def message(msg):
    print("I GET A MESSAGE: " msg)
    imgUrl = "http://a57.foxnews.com/images.foxnews.com/content/fox-news/lifestyle/2018/03/08/corgi-got-fat-shamed-and-internet-could-not-handle-it/_jcr_content/par/featured_image/media-0.img.jpg/931/524/1520540975471.jpg?ve=1&tl=1&text=big-top-image"
    emit('imageResponse', {'data': imgUrl})

if __name__ == '__main__':
    socketio.run(app)