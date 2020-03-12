from flask import Flask, request, jsonify, send_file, make_response
import requests
import json
import traceback
import random
from decouple import config
from flask_pymongo import PyMongo
from apps.get_city import *
from apps.post_types import *


def create_app():
    app = Flask(__name__, static_url_path='/apps/static')





    citydata = get_city_json()
    verify_token = config('verify_token')
    token = config('token')
    app.config['MONGO_URI'] = config('MONGO_URI')
    mongo = PyMongo(app)
    url = 'https://605eecb8.ngrok.io'
    
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
                        print(r.text)
                elif 'text' in data['entry'][0]['messaging'][0]['message'].keys():
                 
                    print(data)
                    response = forcebutton()
                    payload = {
                        "recipient":{
                            "id":sender
                        },
                        'message':
                        response
                        }    
                    r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload)
                    print(r.text)

                else:
                    print('else')

            except Exception as e:
                pass
                #print('next') # something went wrong
        elif request.method == 'GET': # For the initial verification
            if request.args.get('hub.verify_token') == verify_token:
                return request.args.get('hub.challenge')
                return "Wrong Verify Token"
        return "Hello World"

    return app