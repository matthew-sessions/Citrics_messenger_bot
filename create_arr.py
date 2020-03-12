import json
import numpy as np
with open('apps/data/cities/city_mapper.json', 'r') as file:
    data = file.read()
    cities = json.loads(data)
    
words = ''

for i in list(cities.keys()):
    words = words + ' ' + i
    
word_list = []
for i in words.split():
    if i not in word_list:
        word_list.append(i)
print('word list')



z = dict(zip(word_list, [0 for i in word_list]))
cite_cos = []

for i in list(cities.keys())[20000:]:
    di = z.copy()
    for a in i.split():
        try:
            di[a] += 1
        except:
            print('pass')
    cite_cos.append(list(di.values()))
print('done array')

sv = np.array(cite_cos)

from numpy import asarray
from numpy import save

save('data2.npy', sv)
print('save array')