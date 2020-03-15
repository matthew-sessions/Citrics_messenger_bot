import json
import difflib
import requests
import numpy as np
import io

def get_city(word, data):
    res = difflib.get_close_matches(word.lower(), list(data.keys()), n=1)
    print(res)
    return data[res[0]]['ID']


def get_city_json():
    with open("apps/data/cities/city_mapper.json", "r") as myfile:
        data = myfile.read()
        obj = json.loads(data)
    return(obj)
       

def format_data(li):
    res = []

    if '+' in li:
        data = li.split('+')
        
        for i in data:
            res.append(int(i))
        return(res)
    else:
        res.append(int(li))
        return(res)
    