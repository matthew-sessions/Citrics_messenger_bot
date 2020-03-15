from flask import Flask, request, jsonify, send_file, make_response
from decouple import config
from flask_pymongo import PyMongo
from apps.get_city import *


def create_app():
    app = Flask(__name__, static_url_path='/apps/static')

    app.config['MONGO_URI'] = config('MONGO_URI')
    mongo = PyMongo(app)

  
    @app.route(f"/")
    def home():


        return jsonify('home')  
    

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

    return app