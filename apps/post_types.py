from decouple import config

import requests

token = config('token')
site = config('SITE')

def PopulationOverview(citydata):
    
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
        
    else:
        cities = str(citydata[0]['_id'])

    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/population_overview/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }
    
    text = ''
    for i in citydata:
        cityname = i['name_with_com']
        
        population = i['Total Population']
        male = i['Population Male & Female']['Male']
        female = male = i['Population Male & Female']['Female']
        
        pop2010 = i['Population Growth']['2010']
        growth = round(((population-pop2010)/pop2010) * 100, 2)
        if growth > 0:
            movement = 'increase 📈'
        else:
            movement = 'decrease 📉'
            
        format_text = f"{cityname} has a population of {int(population)} \nThis is {growth}% {movement} from 2010.\nThe gender breakdown is ♂️ {male}% male and ♀️ {female}% female.\n\n"
        text = text + format_text
    
    message = {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text":text,
                "buttons":[
                {
                    "type":"postback",
                    "payload":"PopulationAge_"+cities,
                    "title":"Population Data by Age"
                },
                {
                    "type":"postback",
                    "payload":"Education_"+cities,
                    "title":"Education Data"
                }
                ]
            }
            }
        }

    return([message_pic, message])

def PopulationAge(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/population_age/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }
    return([message_pic])


def logicmapper(baseword, citydata):
    function = eval(baseword)
    res = function(citydata)
    return(res)


def forcebutton():
    message = {
        "attachment":{
        "type":"template",
        "payload":{
            "template_type":"button",
            "text":"Population two",
            "buttons":[
            {
                "type":"postback",
                "payload": "PopulationOverview_20000",
                "title":"Population overview"
            },
            {
                "type":"postback",
                "payload": "PopulationTwo_2533",
                "title":"Population two"
            }            
            ]
        }
        }
    }  
    return(message)