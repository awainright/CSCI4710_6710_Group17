from flask import Flask, render_template
import util
from flask_sqlalchemy import SQLAlchemy
import os
import csv
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.orm import deferred
from sqlalchemy.orm import defer, undefer

# get current app directory
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = dir_path + '/data/'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir_path, 'survey.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Survey(db.Model):
    __tablename__ = 'data-survey'
    index = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.Text())
    age = db.Column(db.Integer)
    gender = db.Column(db.Text())
    fearFactor = db.Column(db.Integer)
    anxiousFactor = db.Column(db.Integer)
    angerFactor = db.Column(db.Integer)
    happyFactor = db.Column(db.Integer)
    sadFactor = db.Column(db.Integer)
    emotionFactor = db.Column(db.Text())
    whyFactor = db.Column(db.Text())
    meaningFactor = db.Column(db.Text())
    job = db.Column(db.Text())

    def __init__(self, index, country, age, gender, fearFactor, anxiousFactor, angerFactor, happyFactor, sadFactor,
                 emotionFactor, whyFactor, meaningFactor, job):
        self.index = index
        self.country = country
        self.age = age
        self.gender = gender
        self.fearFactor = fearFactor
        self.anxiousFactor = anxiousFactor
        self.angerFactor = angerFactor
        self.happyFactor = happyFactor
        self.sadFactor = sadFactor
        self.emotionFactor = emotionFactor
        self.whyFactor = whyFactor
        self.meaningFactor = meaningFactor
        self.job = job

    def __getitem__(self, this):
        return self.index, self.country, self.age, self.gender, self.fearFactor, self.anxiousFactor, self.angerFactor, self.happyFactor, self.sadFactor, self.emotionFactor, self.whyFactor, self.meaningFactor, self.job

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
        self.index, self.country, self.age, self.gender, self.fearFactor, self.anxiousFactor, self.angerFactor,
        self.happyFactor, self.sadFactor, self.emotionFactor, self.whyFactor, self.meaningFactor, self.job)

    def __iter__(self):
        return iter(
            [self.index, self.country, self.age, self.gender, self.fearFactor, self.anxiousFactor, self.angerFactor,
             self.happyFactor, self.sadFactor, self.emotionFactor, self.whyFactor, self.meaningFactor, self.job])


db.drop_all()
db.create_all()
with open('data/t.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    # print(df)
    for line in reader:
        # print(line[0])
        response = Survey(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9],
                          line[10], line[11], line[12])
        db.session.add(response)
        db.session.commit()

query0 = db.session.query(Survey).all()
print(query0)


@app.route('/')
def index():
    return render_template('basic_map_datamaps.html')


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
