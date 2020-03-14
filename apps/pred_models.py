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
    res = difflib.get_close_matches(word.lower(), list(data.keys()), n=1)
    if res ==[]:
        return(None)
    return data[res[0]]['ID']

def mongo_getter_single(mongo, id):
    data = mongo.db.alldata.find_one({'_id':id})
    return(data)