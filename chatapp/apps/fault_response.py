import requests

def compare_not_understood(sender, token):
    payload = {
        "recipient":{
            "id":sender
        },
        'message':{
            'text':'Sorry, I did not understand that! If you want to compare two Cities follow the format below 👇\n\n\nCompare Seattle WA and Tacoma WA'
        }
        }
                        
    r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload)

def compare_city_missing(sender, token):
    payload = {
        "recipient":{
            "id":sender
        },
        'message':{
            'text':'Sorry, I could not find data for one or both the Cities you provided! Please check the spelling and try again.\n\nNote: make sure to follow the format below 👇\n\n\nCompare Seattle WA and Tacoma WA'
        }
        }
                        
    r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload)

def generic_no_understand(sender, token):
    payload = {
        "recipient":{
            "id":sender
        },
        'message':{
            'text':"Sorry, I'm still learning and did not understand that! Try to rephrase your question.\n\nNote: if you want to compare two new Cities, follow the format below 👇\n\n👉 Compare Seattle WA and Tacoma WA\n\n\nOr for a single City..\n\n\n👉 Seattle Washington"
        }
        }
                        
    r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload) 

def GetStarted(sender, token):
    payload = {
        "recipient":{
            "id":sender
        },
        'message':{
            'text':"Welcome to Citrics! We have data on every City/Town in the US and we are eager to share!\n\nTo get started just let us know the City you are intrested in or tell use to compare two cities. Just follow the format below 👇\n\n👉 Compare Seattle WA and Tacoma WA\n\n\nOr for a single City..\n\n\n👉 Seattle Washington"
        }
        }
                        
    r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload) 

def need_city_data(sender, token):
    payload = {
        "recipient":{
            "id":sender
        },
        'message':{
            'text':"We need to know what Cities you are intrested in before we show you stats! Let us know what City you are intrested in or which Cities you want to compare\n\nFollow the format below 👇\n\n👉 Compare Seattle WA and Tacoma WA\n\n\nOr for a single City..\n\n\n👉 Seattle Washington"
        }
        }
                        
    r = requests.post('https://graph.facebook.com/v6.0/me/messages/?access_token=' + token, json=payload)        