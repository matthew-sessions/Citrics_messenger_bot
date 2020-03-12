import json
import difflib
import requests
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
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
    
def save_pic(data):

    li = data
    sns.set()


    fig, ax = plt.subplots(figsize=(20, 10))

    for i in li:
        ax.plot(i[0], i[1], label = i[2], linewidth = 5, linestyle = '--')

    ax.set(xlabel=f'Property Value for {data[0][2]}', ylabel='Avg. Home Value in USD)',
        title='')
    ax.legend(fontsize=20)
    fig.suptitle('', fontsize=20)

    plt.ylabel(f'Property Value for {data[0][2]}', fontsize=16)
    ax.xaxis.set_major_locator(plt.MaxNLocator(15))
    ax.tick_params(axis='y', which='major', labelsize=17)
    plt.xticks(fontsize=17, rotation=30)
    ax.grid()
    name = ''

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)

def populationgrowthchart(data):
    sns.set()
    fig, ax = plt.subplots(figsize=(20, 10))

    for i in data:
        x = list(i['Population Growth'].keys())
        y = list(i['Population Growth'].values())
        name = i['name_with_com']
        ax.plot(x, y, label = name, linewidth = 5, linestyle = '--')

    ax.set(title='')
    ax.legend(fontsize=20)
    fig.suptitle('', fontsize=20)

    plt.ylabel('Totall Population', fontsize=19)
    plt.xlabel('Growth over eight years', fontsize=19)
    ax.xaxis.set_major_locator(plt.MaxNLocator(15))
    ax.tick_params(axis='y', which='major', labelsize=17)
    plt.xticks(fontsize=17, rotation=30)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)

def plot_popbreakdown(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Age Distribution'].values()))
        means_frank = list(data[0]['Age Distribution'].values())
        means_guido = list(data[1]['Age Distribution'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Age Distribution'].keys())

        # create plot
        fig, ax = plt.subplots(figsize=(20, 10))
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        rects1 = plt.bar(index, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)

        rects2 = plt.bar(index + bar_width, means_guido, bar_width,
        alpha=opacity,
        color='g',
        label=name2)

        plt.ylabel('Totall Population by %', fontsize=19)
        plt.xlabel('Age groups', fontsize=19)
        plt.title('Population Distribution by Age', fontsize=20)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Age Distribution'].values())
        x = list(data[0]['Age Distribution'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Totall Population by %', fontsize=19)
        plt.xlabel('Age groups', fontsize=19)
        plt.title('Population Distribution by Age', fontsize=20)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)
# # def payit(psid):
# #     data = {
# #     "recipient":{
# #         "id":psid
# #     },
# #     "messaging_type": "RESPONSE",
# #     "message":{
# #         "text": "Pick a color\nrgithe now:",
# #         "quick_replies":[
# #         {
# #             "content_type":"text",
# #             "title":"Red",
# #             "payload":"<POSTBACK_PAYLOAD>",
# #             "image_url":"http://example.com/img/red.png"
# #         },{
# #             "content_type":"text",
# #             "title":"Green",
# #             "payload":"<POSTBACK_PAYLOAD>",
# #             "image_url":"http://example.com/img/green.png"
# #         }
# #         ]
# #     }
# #     }
# #     return(data)

# def payit(psid):
#     data = {
#     "recipient":{
#         "id":psid
#     },
#     "message":{
#         "attachment":{
#         "type":"template",
#         "payload":{
#             "template_type":"generic",
#             "elements":[
#             {
#                 "title":"Welcome!",
#                 "image_url":"https://a34fecd8.ngrok.io/56/pic.png",
#                 "subtitle":"We have the right hat for everyone.",
#                 "default_action": {
#                 "type": "web_url",
#                 "url": "https://petersfancybrownhats.com/view?item=103",
#                 "webview_height_ratio": "tall",
#                 },
#                 "buttons":[
#                 {
#                     "type":"web_url",
#                     "url":"https://petersfancybrownhats.com",
#                     "title":"View Website"
#                 },{
#                     "type":"postback",
#                     "title":"Start Chatting",
#                     "payload":"DEVELOPER_DEFINED_PAYLOAD"
#                 }              
#                 ]      
#             }
#             ]
#         }
#         }
#     }}
#     return(data)
