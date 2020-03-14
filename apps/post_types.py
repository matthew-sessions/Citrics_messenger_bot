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
                    "payload":"EducationData_"+cities,
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

    text = ''
    for i in citydata:
        cityname = i['name_with_com']
        
        medianage = i['Median Age']
        under18 = i['Population under 18']
        over16 = i['Population over 16']
            
        format_text = f"👨‍👩‍👧‍👧 {cityname} has a Median Age of {medianage} \n{under18}% of the total population are under the age of 18 and {over16}% are over the age of 16.\n\n"
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
                    "payload":"EducationData_"+cities,
                    "title":"Education Data"
                },
                {
                    "type":"postback",
                    "payload":"IncomeData_"+cities,
                    "title":"Income Data"
                },                
                ]
            }
            }
        }        
    return([message_pic, message])


def EducationData(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/education/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }

    message_pic2 = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/schoolenrollment/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }       

    text = ''
    for i in citydata:
        cityname = i['name_with_com']
        
        bailang = i['Two or more Languages']
        englishonly = i['Language']['English Only']
        other = i['Language']['Language other than English']
        noenglish = i['Language']['Cannot Speak English']

        format_text = f"🏫 {bailang}% of people in {cityname} can speak more than one language. {englishonly}% can only speak English, {other}% of people natively speak a language other than English, and {noenglish}% of people cannont speak English. \n\n"
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
                    "payload":"IncomeData_"+cities,
                    "title":"Income Data"
                },       
                {
                    "type":"postback",
                    "payload":"RealEstate_"+cities,
                    "title":"Home Data"
                },     
                {
                    "type":"postback",
                    "payload":"PopulationOverview_"+cities,
                    "title":"Population Stats"
                },                                      
                ]
            }
            }
        }        
    return([message_pic, message_pic2, message])

def IncomeData(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/householdincome/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }

    text = ''
    for i in citydata:
        cityname = i['name_with_com']
        
        meanincome = i['Mean Household Income']
        medianicome = i['Median Household Income']

            
        format_text = f"💰 {cityname} has a median household income of ${medianicome} and a mean household income of ${meanincome}. \n\n"
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
                    "payload":"PercapitaIncome_"+cities,
                    "title":"Income Per Capita"
                },
                {
                    "type":"postback",
                    "payload":"LaborStats_"+cities,
                    "title":"Labor Stats"
                },                
                ]
            }
            }
        }        
    return([message_pic, message])

def PercapitaIncome(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/percapita/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }

    text = ''
    for i in citydata:
        cityname = i['name_with_com']
        
        insurance = i['Health Insurance']
        poverty = i['Below Poverty Level']
        medianicome = i['Median Per Capita Income']
        unemployment = i['Unemployment Rate']        
            
        format_text = f"💰 {cityname} has a median per-capita income of ${medianicome}. The Unemployment Rate is {unemployment}%, {poverty}% of the total population lives below the poverty line, and {insurance}% have health insurance. \n\n"
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
                    "payload":"LaborStats_"+cities,
                    "title":"Labor Stats"
                },  
                {
                    "type":"postback",
                    "payload":"RealEstate_"+cities,
                    "title":"Real Estate Data"
                },                              
                ]
            }
            }
        }        
    return([message_pic, message])


def LaborStats(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/occupation/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }
    message_pic2 = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/workerclass/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }
    text = ''
    for i in citydata:
        cityname = i['name_with_com']
        
        male = round(i['Sex of Labor Force']['Male'],1)
        female = round(i['Sex of Labor Force']['Female'],1)   
            
        format_text = f"The Labor Force in {cityname} is {male}% Male and {female}% Female. \n\n"
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
                    "payload":"Commute_"+cities,
                    "title":"Daily Commute Data"
                },  
                {
                    "type":"postback",
                    "payload":"RealEstate_"+cities,
                    "title":"Real Estate Data"
                },                              
                ]
            }
            }
        }        
    return([message_pic, message_pic2, message])


def Commute(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/commute/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }

    text = ''
    for i in citydata:
        cityname = i['name_with_com']
        
        commutetime = i['Mean Travel Time']            
        format_text = f"The average worker in {cityname} has a daily commute time of {commutetime} minutes. \n\n"
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
                    "payload":"VehicleAvailable_"+cities,
                    "title":"Vehicle Data"
                },  
                {
                    "type":"postback",
                    "payload":"RealEstate_"+cities,
                    "title":"Real Estate Data"
                },                              
                ]
            }
            }
        }        
    return([message_pic, message])

def VehicleAvailable(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/vehicles/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }

    text = 'Click below to view more stats'

    
    message = {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text":text,
                "buttons":[
                {
                    "type":"postback",
                    "payload":"UnitsInStructure_"+cities,
                    "title":"Units in Structure"
                },                       
                {
                    "type":"postback",
                    "payload":"Rent_"+cities,
                    "title":"Rent Data"
                }
                           
                ]
            }
            }
        }        
    return([message_pic, message])

def UnitsInStructure(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/unitsinstructure/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }
    message_pic2 = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/yearbuilt/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }
    text = ''
    for i in citydata:
        cityname = i['name_with_com']

        vaccancyrate = i['Vacancy Rate']['Homeowner vacancy rate']  
        totalunits = i['Total Housing Units']            
        format_text = f"{cityname} has {totalunits} housing units with a vacancy rate of {vaccancyrate}% \n\n"
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
                    "payload":"Rent_"+cities,
                    "title":"Rent Data"
                },
                {
                    "type":"postback",
                    "payload":"RealEstate_"+cities,
                    "title":"Property Values"
                }                          
                ]
            }
            }
        }        
    return([message_pic, message_pic2, message])

def RealEstate(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/homevalues/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }

    text = ''
    for i in citydata:
        cityname = i['name_with_com']

        vaccancyrate = i['Vacancy Rate']['Homeowner vacancy rate']  
        totalunits = i['Total Housing Units']            
        format_text = f"{cityname} has {totalunits} housing units with a vacancy rate of {vaccancyrate}% \n\n"
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
                    "payload":"UnitsInStructure_"+cities,
                    "title":"Housing Unit Data"
                },                       
                {
                    "type":"postback",
                    "payload":"Rent_"+cities,
                    "title":"Rent Data"
                }
                           
                ]
            }
            }
        }        
    return([message_pic, message])

def Rent(citydata):
    if len(citydata) == 2:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
    else:
        cities = str(citydata[0]['_id'])
    message_pic = {
            "attachment":{
            "type":"image", 
            "payload":{
                "url":site + f'/rent/{cities}/pic.png', 
                "is_reusable":True
            }
            }
        }

    text = ''
    for i in citydata:
        cityname = i['name_with_com']

        medianrent = i['Median Rent']
           
        format_text = f"{cityname} has a median rent price of ${medianrent} \n\n"
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
                    "payload":"UnitsInStructure_"+cities,
                    "title":"Housing Unit Data"
                },                       
                {
                    "type":"postback",
                    "payload":"RealEstate_"+cities,
                    "title":"Home Values"
                }
                           
                ]
            }
            }
        }        
    return([message_pic, message])

def logicmapper(baseword, citydata):
    function = eval(baseword)
    res = function(citydata)
    return(res)


def NewSelection(citydata):
    if len(citydata) > 1:
        cities = f"{citydata[0]['_id']}+{citydata[1]['_id']}"
        name = f"{citydata[0]['name_with_com']} and {citydata[1]['name_with_com']} "
    else:
        cities = str(citydata[0]['_id'])
        name = f"{citydata[0]['name_with_com']}"

    text = f'What would you like to learn about {name}?\n\nClick a category below to start learning or type something like: "Show me data for home prices".'
    message = {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text":text,
                "buttons":[
                {
                    "type":"postback",
                    "payload":"PopulationOverview_"+cities,
                    "title":"General Population Stats"
                },                       
                {
                    "type":"postback",
                    "payload":"EducationData_"+cities,
                    "title":"Education & Schools"
                },
                {
                    "type":"postback",
                    "payload":"IncomeData_"+cities,
                    "title":"Income & Worklife"
                } 
                ]
            }
            }
        }        
    return([message])    

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
                "payload": "PopulationOverview_18525+1375",
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