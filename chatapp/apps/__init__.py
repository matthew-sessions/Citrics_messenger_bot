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
from apps.fault_response import *

def create_app():
    app = Flask(__name__, static_url_path='/apps/static')



    

    citydata = get_city_json()
    verify_token = config('verify_token')
    token = config('token')
    app.config['MONGO_URI'] = config('MONGO_URI')
    mongo = PyMongo(app)
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

    class ChatHistoryLogs(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        USID = db.Column(db.BIGINT)
        Content = db.Column(db.String(1000))
        Pred = db.Column(db.Integer)

  
    @app.route(f"/")
    def home():


        return jsonify('home')  
    @app.route('/<here>')
    def home2(here):
        db.session.add(PSIDDATA4(USID=45454, Type=here, CityOne=None, CityTwo=None))
        db.session.commit()      
        return('hello')  

    @app.route('/webhook', methods=['GET', 'POST'])
    def webhook_verify():
        if request.method == 'POST':
            try:
                data = json.loads(request.data)
                sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID

                if 'postback' in data['entry'][0]['messaging'][0].keys():
                    if data['entry'][0]['messaging'][0]['postback']['payload'] == 'GetStarted':

                        GetStarted(sender, token)
                    
                    else:
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
                        if res == False:
                            intoit = 777
                        else:
                            intoit = res
                        db.session.add(ChatHistoryLogs(USID=int(sender), Content=text, Pred=intoit))
                        db.session.commit()  
                                
                        if res == 11:
                            city_pointer_compare = compare_getter(text, citydata)
                            if city_pointer_compare is False:
                                compare_not_understood(sender, token)
                            elif city_pointer_compare == 'MissingCity':
                                compare_city_missing(sender, token)
                            else:
                                user = PSIDDATA4.query.filter_by(USID=int(sender)).first()
                                mongodata = mongo_getter_double(mongo, city_pointer_compare)
                                user.Type = 'compare'
                                user.CityOne = int(mongodata[0]['_id'])
                                user.CityTwo = int(mongodata[1]['_id'])
                                db.session.commit()                              
                                response = logicmapper('NewSelection',mongodata) 
                                for i in response:
                                    payload = {
                                        "recipient":{
                                            "id":sender
                                        },
                                        'message':
                                        i
                                        }
                                                    
                                    r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload)                                                               
                        elif res is False:
                            
                            db.session.add(ChatHistoryLogs(USID=int(sender), Content=text, Pred=777))
                            db.session.commit()                             
                            city_pointer_single = city_name_mapper(text, citydata)
                            if city_pointer_single is not None:
                                user = PSIDDATA4.query.filter_by(USID=int(sender)).first()
                                mongodata = mongo_getter_single(mongo, city_pointer_single)
                                user.Type = 'single'
                                user.CityOne = int(mongodata['_id'])
                                user.CityTwo = None
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
                                generic_no_understand(sender, token)
                              
                    else:
                        text = data['entry'][0]['messaging'][0]['message']['text'].lower()
                        tfidf_trans = tfidf.transform([text])
                        res = understand(tfidf_data, tfidf_trans)
                        if 'housing' in text:
                            res = 10    
                        if res == False:
                            intoit = 777
                        else:
                            intoit = res
                        db.session.add(ChatHistoryLogs(USID=int(sender), Content=text, Pred=intoit))
                        db.session.commit()                                                   
                        if res is not False:

                            if res == 11:
                                city_pointer_compare = compare_getter(text, citydata)
                                if city_pointer_compare is False:
                                    compare_not_understood(sender, token)
                                elif city_pointer_compare == 'MissingCity':
                                    compare_city_missing(sender, token)
                                else:
                                    user = PSIDDATA4.query.filter_by(USID=int(sender)).first()
                                    mongodata = mongo_getter_double(mongo, city_pointer_compare)
                                    user.Type = 'compare'
                                    user.CityOne = int(mongodata[0]['_id'])
                                    user.CityTwo = int(mongodata[1]['_id'])
                                    db.session.commit()                              
                                    response = logicmapper('NewSelection',mongodata) 
                                    for i in response:
                                        payload = {
                                            "recipient":{
                                                "id":sender
                                            },
                                            'message':
                                            i
                                            }
                                                        
                                        r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload)

                            elif user.Type is None:
                                need_city_data(sender, token)
                            else:
                                if user.Type == 'compare':
                                    cityid1 = user.CityOne
                                    cityid2 = user.CityTwo
                                    mongodata = mongo_getter_double(mongo, [cityid1, cityid2])
                                    
                                else:
                                    cityid = user.CityOne
                                    mongodata = [mongo_getter_single(mongo, cityid)]
                                function_name = function_id_to_name(res)
                                response = logicmapper(function_name,mongodata) 
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
                            city_pointer_single = city_name_mapper(text, citydata)
                            if city_pointer_single is not None:
                                user = PSIDDATA4.query.filter_by(USID=int(sender)).first()
                                mongodata = mongo_getter_single(mongo, city_pointer_single)
                                user.Type = 'single'
                                user.CityOne = int(mongodata['_id'])
                                user.CityTwo = None
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
                                generic_no_understand(sender, token)


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