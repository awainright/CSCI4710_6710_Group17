from flask import Flask, render_template
import util
from flask_sqlalchemy import SQLAlchemy
import os
import csv
import json
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

    def toList(self):
        return [self.index, self.country, self.age, self.gender, self.fearFactor, self.anxiousFactor, self.angerFactor,
                self.happyFactor, self.sadFactor, self.emotionFactor, self.whyFactor, self.meaningFactor, self.job]


db.drop_all()
db.create_all()
with open('data/t.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for line in reader:
        response = Survey(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9],
                          line[10], line[11], line[12])
        db.session.add(response)
        db.session.commit()

column_names = ["index", "What country do you live in?", "How old are you?", "What is your gender?",
                "To what extent do you feel FEAR due to the coronavirus?",
                "To what extent do you feel ANXIOUS due to the coronavirus?",
                "To what extent do you feel ANGRY due to the coronavirus?",
                "To what extent do you feel HAPPY due to the coronavirus?",
                "To what extent do you feel SAD due to the coronavirus?",
                "Which emotion is having the biggest impact on you?", "What makes you feel that way?",
                "What brings you the most meaning during the coronavirus outbreak?", "What is your occupation?"]

query0 = db.session.query(Survey).all()
query1 = db.session.query(Survey).filter(Survey.gender == "Male").filter(Survey.age <= 35).all()
query2 = db.session.query(Survey).filter(Survey.age >= 36, Survey.gender == "Male").all()
query3 = db.session.query(Survey).filter(Survey.age <= 35, Survey.gender == "Female").all()
query4 = db.session.query(Survey).filter(Survey.age >= 36, Survey.gender == "Female").all()

query1_1 = db.session.query(Survey).filter(Survey.country == "USA", Survey.gender == "Male", Survey.age <= 35).all()
query1_2 = db.session.query(Survey).filter(Survey.country == "Romania", Survey.gender == "Male", Survey.age <= 35).all()
query1_3 = db.session.query(Survey).filter(Survey.country == "UK", Survey.gender == "Male", Survey.age <= 35).all()
query1_4 = db.session.query(Survey).filter(Survey.country == "Canada", Survey.gender == "Male", Survey.age <= 35).all()
query1_5 = db.session.query(Survey).filter(Survey.country == "Switzerland", Survey.gender == "Male",
                                           Survey.age <= 35).all()
query1_6 = db.session.query(Survey).filter(Survey.country == "Rwanda", Survey.gender == "Male", Survey.age <= 35).all()
query1_7 = db.session.query(Survey).filter(Survey.country == "Ireland l", Survey.gender == "Male",
                                           Survey.age <= 35).all()
query1_8 = db.session.query(Survey).filter(Survey.country == "Germany", Survey.gender == "Male", Survey.age <= 35).all()
query1_9 = db.session.query(Survey).filter(Survey.country == "Israel", Survey.gender == "Male", Survey.age <= 35).all()

query2_1 = db.session.query(Survey).filter(Survey.country == "USA", Survey.gender == "Male", Survey.age > 35).all()
query2_2 = db.session.query(Survey).filter(Survey.country == "Romania", Survey.gender == "Male", Survey.age > 35).all()
query2_3 = db.session.query(Survey).filter(Survey.country == "UK", Survey.gender == "Male", Survey.age > 35).all()
query2_4 = db.session.query(Survey).filter(Survey.country == "Canada", Survey.gender == "Male", Survey.age > 35).all()
query2_5 = db.session.query(Survey).filter(Survey.country == "Switzerland", Survey.gender == "Male",
                                           Survey.age > 35).all()
query2_6 = db.session.query(Survey).filter(Survey.country == "Rwanda", Survey.gender == "Male", Survey.age > 35).all()
query2_7 = db.session.query(Survey).filter(Survey.country == "France", Survey.gender == "Male", Survey.age > 35).all()
query2_8 = db.session.query(Survey).filter(Survey.country == "Germany", Survey.gender == "Male", Survey.age > 35).all()
query2_9 = db.session.query(Survey).filter(Survey.country == "New Zealand", Survey.gender == "Male",
                                           Survey.age > 35).all()
query2_10 = db.session.query(Survey).filter(Survey.country == "spain", Survey.gender == "Male", Survey.age > 35).all()
# Not sure whats wrong with query2_11
query2_11 = db.session.query(Survey).filter(Survey.country == "Palestine", Survey.gender == "Male",
                                            Survey.age > 35).all()

query3_1 = db.session.query(Survey).filter(Survey.country == "USA", Survey.gender == "Female", Survey.age <= 35).all()
query3_2 = db.session.query(Survey).filter(Survey.country == "Romania", Survey.gender == "Female",
                                           Survey.age <= 35).all()
query3_3 = db.session.query(Survey).filter(Survey.country == "UK", Survey.gender == "Female", Survey.age <= 35).all()
query3_4 = db.session.query(Survey).filter(Survey.country == "Canada", Survey.gender == "Female",
                                           Survey.age <= 35).all()
query3_5 = db.session.query(Survey).filter(Survey.country == "Switzerland", Survey.gender == "Female",
                                           Survey.age <= 35).all()
query3_6 = db.session.query(Survey).filter(Survey.country == "Rwanda", Survey.gender == "Female",
                                           Survey.age <= 35).all()
# should contain 1
query3_7 = db.session.query(Survey).filter(Survey.country == "China", Survey.gender == "Female", Survey.age <= 35).all()
query3_8 = db.session.query(Survey).filter(Survey.country == "Germany", Survey.gender == "Female",
                                           Survey.age <= 35).all()
query3_9 = db.session.query(Survey).filter(Survey.country == "Australia", Survey.gender == "Female",
                                           Survey.age <= 35).all()
query3_10 = db.session.query(Survey).filter(Survey.country == "Portugal", Survey.gender == "Female",
                                            Survey.age <= 35).all()
query3_11 = db.session.query(Survey).filter(Survey.country == "Colombia", Survey.gender == "Female",
                                            Survey.age <= 35).all()
query3_12 = db.session.query(Survey).filter(Survey.country == "Cyprus", Survey.gender == "Female",
                                            Survey.age <= 35).all()

query4_1 = db.session.query(Survey).filter(Survey.country == "USA", Survey.gender == "Female", Survey.age > 35).all()
query4_2 = db.session.query(Survey).filter(Survey.country == "Romania", Survey.gender == "Female",
                                           Survey.age > 35).all()
query4_3 = db.session.query(Survey).filter(Survey.country == "UK", Survey.gender == "Female", Survey.age > 35).all()
query4_4 = db.session.query(Survey).filter(Survey.country == "Canada", Survey.gender == "Female", Survey.age > 35).all()
query4_5 = db.session.query(Survey).filter(Survey.country == "Switzerland", Survey.gender == "Female",
                                           Survey.age > 35).all()
# should contain 1
query4_6 = db.session.query(Survey).filter(Survey.country == "Australia", Survey.gender == "Female",
                                           Survey.age > 35).all()
query4_7 = db.session.query(Survey).filter(Survey.country == "Portugal", Survey.gender == "Female",
                                           Survey.age > 35).all()
query4_8 = db.session.query(Survey).filter(Survey.country == "Germany", Survey.gender == "Female",
                                           Survey.age > 35).all()
usaQuery = db.session.query(Survey).filter(Survey.country == "USA").all()
canQuery = db.session.query(Survey).filter(Survey.country == "Canada").all()
ukQuery = db.session.query(Survey).filter(Survey.country == "UK").all()


# this is the code connected to d3_map
@app.route('/api/query_survey_results/<country>', methods=['GET'])
def query_survey_results(country=''):
    if country == "United States of America":
        country = "USA"
    if country == "United Kingdom":
        country = "UK"

    flag = False
    for row in query0:
        if country == row.country:
            flag = True
            break

    if flag:
        temp_query = db.session.query(Survey).filter(Survey.country == country).all()
        print(temp_query)
        survey_query_data = {'user_data': []}
        for surveys in temp_query:
            survey_query_data['user_data'].append(surveys.toList())
    else:
        survey_query_data = {'user_data': [country + " does not have any survey data"]}

    return json.dumps(survey_query_data)



@app.route('/')
def index():
    return render_template('d3_map.html')


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
