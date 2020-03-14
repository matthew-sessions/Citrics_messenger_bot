from flask import Flask, request, jsonify, send_file, make_response
import requests
import json
import traceback
import random
from decouple import config
from flask_pymongo import PyMongo
from apps.get_city import *
from apps.post_types import *
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from apps.pred_models import *

def create_app():
    app = Flask(__name__, static_url_path='/apps/static')



    

    citydata = get_city_json()
    verify_token = config('verify_token')
    token = config('token')
    app.config['MONGO_URI'] = config('MONGO_URI')
    mongo = PyMongo(app)
    url = 'https://605eecb8.ngrok.io'
    app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    page_id = config('page_id')
    tfidf = joblib.load('apps/data/models/tfidf_model.joblib')
    tfidf_data = joblib.load('apps/data/models/tfidf_data.joblib')



    class PSIDDATA4(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        USID = db.Column(db.BIGINT)
        Type = db.Column(db.String(100))
        CityOne = db.Column(db.Integer)
        CityTwo = db.Column(db.Integer)
    
  
    

    @app.route(f"/population_overview/<city_format>/pic.png")
    def allcitydata(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = populationgrowthchart(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route(f"/population_age/<city_format>/pic.png")
    def populationage(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = plot_popbreakdown(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route(f"/education/<city_format>/pic.png")
    def edu(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = educationplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route(f"/schoolenrollment/<city_format>/pic.png")
    def schoolenrollment(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = schoolenrollplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route(f"/householdincome/<city_format>/pic.png")
    def householdincome_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = householdincomeplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route(f"/percapita/<city_format>/pic.png")
    def percapita_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = capitaincomeplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route(f"/occupation/<city_format>/pic.png")
    def occupaiton_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = occupationplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')    

    @app.route(f"/workerclass/<city_format>/pic.png")
    def workerclass_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = workerplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')


    @app.route(f"/commute/<city_format>/pic.png")
    def commute_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = commuteplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')        

    @app.route(f"/vehicles/<city_format>/pic.png")
    def vehicles_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = vehiclesplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png') 

    @app.route(f"/homevalues/<city_format>/pic.png")
    def homeval_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = homevalchart(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route(f"/unitsinstructure/<city_format>/pic.png")
    def unitsinstructure_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = unitsinstructureplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route(f"/yearbuilt/<city_format>/pic.png")
    def yearbuilt_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = yearbuiltplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route(f"/rent/<city_format>/pic.png")
    def rental_ep(city_format):

        data = format_data(city_format)
        datali = []
        for i in data:
            datali.append(mongo.db.alldata.find_one({'_id':i}))
        name = rentplot(datali)
        return send_file(name, attachment_filename='plot.png', mimetype='image/png')

    @app.route('/webhook', methods=['GET', 'POST'])
    def webhook_verify():
        if request.method == 'POST':
            try:
                data = json.loads(request.data)
                sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID

                if 'postback' in data['entry'][0]['messaging'][0].keys():
                    postback = data['entry'][0]['messaging'][0]['postback']['payload'].split('_')
                    baseword = postback[0]
                    
                    if '+' in postback[1]:
                        spl = postback[1].split('+')
                        
                        cityids = [int(i) for i in spl]
                        
                    else:
                        cityids = [int(postback[1])]
                    
                    citydata_list = [mongo.db.alldata.find_one({'_id': i}) for i in cityids]             

                    response = logicmapper(baseword, citydata_list)
                    
                    for i in response:
                        payload = {
                            "recipient":{
                                "id":sender
                            },
                            'message':
                            i
                            }
                                          
                        r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload)
                       
                elif 'text' in data['entry'][0]['messaging'][0]['message'].keys() and int(sender) != int(page_id):
                 
                    user = PSIDDATA4.query.filter_by(USID=int(sender)).first()
                    
                    if user is None:                       
                        db.session.add(PSIDDATA4(USID=int(sender), Type=None, CityOne=None, CityTwo=None))
                        db.session.commit()
                        text = data['entry'][0]['messaging'][0]['message']['text'].lower()
                        tfidf_trans = tfidf.transform([text])
                        res = understand(tfidf_data, tfidf_trans)
                        if res == 11:
                            pass #add compare function
                        elif res is False:
                            city_pointer_single = city_name_mapper(text, citydata)
                            if city_pointer_single is not None:
                                user = PSIDDATA4.query.filter_by(USID=int(sender)).first()
                                mongodata = mongo_getter_single(mongo, city_pointer_single)
                                user.Type = 'single'
                                user.CityOne = int(mongodata['_id'])
                                db.session.commit()                                
                                response = logicmapper('NewSelection',[mongodata])

                                for i in response:
                                    payload = {
                                        "recipient":{
                                            "id":sender
                                        },
                                        'message':
                                        i
                                        }
                                                    
                                    r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload)
                            else:
                                pass #add generic "I did not understand message!"
                              
                    else:
                        text = data['entry'][0]['messaging'][0]['message']['text'].lower()
                        tfidf_trans = tfidf.transform([text])
                        res = understand(tfidf_data, tfidf_trans)
                        if res is not False:

                            if res == 11:
                                pass

                            elif user.Type is not None:
                                pass
                            else:
                                print('itishere')
                        
                        print(res)

                        response = forcebutton()
                        payload = {
                            "recipient":{
                                "id":sender
                            },
                            'message':
                            response
                            }    
                        r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload)
                        print(data)

                else:
                    pass

            except Exception as e:
                pass

        elif request.method == 'GET': # For the initial verification
            if request.args.get('hub.verify_token') == verify_token:
                return request.args.get('hub.challenge')
                return "Wrong Verify Token"
        return "Hello World"

    return app