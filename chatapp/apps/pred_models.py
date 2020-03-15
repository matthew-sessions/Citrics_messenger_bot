from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd 
import difflib

def understand(tfidf, tfidf_trans):

    dist_matrix  = cosine_similarity(tfidf.todense(), tfidf_trans.todense())
    results = pd.DataFrame(dist_matrix)
    res = int(results[0].sort_values(ascending=False)[0:1].index[0])
    val = float(results[0].sort_values(ascending=False)[0:1].values[0])
    if val >= 0.01:
        return res
    else:
        return False


def city_name_mapper(word, data):
    word = word.replace(',','').replace('.','')
    res = difflib.get_close_matches(word.lower(), list(data.keys()), n=1)
    if res ==[]:
        return(None)
    return data[res[0]]['ID']

def mongo_getter_single(mongo, id):
    data = mongo.db.alldata.find_one({'_id':id})
    return(data)

def mongo_getter_double(mongo, id):
    data1 = mongo.db.alldata.find_one({'_id':id[0]})
    data2 = mongo.db.alldata.find_one({'_id':id[1]})
    return([data1,data2])    


def compare_getter(text, data):
    text = text.lower()
    if 'compare' in text:
        content = text.split('compare')[1]
        if ' and ' in content:
            citytext = content.split(' and ')
            cities = [city_name_mapper(i, data) for i in citytext]
            if None not in cities:
                return(cities)
            else:
                return('MissingCity')
        else:
            return(False)
    else:
        return(False)

def function_id_to_name(id):
    data = {0: 'PopulationOverview',
            1: 'PopulationAge',
            2: 'EducationData',
            3: 'IncomeData',
            4: 'PercapitaIncome',
            5: 'LaborStats',
            6: 'Commute',
            7: 'VehicleAvailable',
            8: 'UnitsInStructure',
            9: 'Rent',
            10: 'RealEstate',
            11: 'RealEstate',
            12: 'GPS'}
    return(data[id])