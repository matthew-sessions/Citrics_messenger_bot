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


def educationplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Educational Attainment'].values()))
        means_frank = list(data[0]['Educational Attainment'].values())
        means_guido = list(data[1]['Educational Attainment'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Educational Attainment'].keys())

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
        plt.xlabel('Level of Education Attained', fontsize=19)
        plt.title('Population Distribution by Education Completed', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Educational Attainment'].values())
        x = list(data[0]['Educational Attainment'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Totall Population by %', fontsize=19)
        plt.xlabel('Level of Education Attained', fontsize=19)
        plt.title('Population Distribution by Educational Completed', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)

def schoolenrollplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['School Enrollment'].values()))
        means_frank = list(data[0]['School Enrollment'].values())
        means_guido = list(data[1]['School Enrollment'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['School Enrollment'].keys())

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

        plt.ylabel('Currently enrolled in school by %', fontsize=19)
      
        plt.title('School enrollment distribution', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['School Enrollment'].values())
        x = list(data[0]['School Enrollment'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Currently enrolled in school by %', fontsize=19)
      
        plt.title('School enrollment distribution', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)    


def householdincomeplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Household Income'].values()))
        means_frank = list(data[0]['Household Income'].values())
        means_guido = list(data[1]['Household Income'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Household Income'].keys())

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

        plt.ylabel('Totall numper of households by %', fontsize=19)
        plt.xlabel('Household income bracket', fontsize=19)
        plt.title('Household income by income bracket', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Household Income'].values())
        x = list(data[0]['Household Income'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Totall numper of households by %', fontsize=19)
        plt.xlabel('Household income bracket', fontsize=19)
        plt.title('Household income by income bracket', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)    

def capitaincomeplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Per Capita by Gender'].values()))
        means_frank = list(data[0]['Per Capita by Gender'].values())
        means_guido = list(data[1]['Per Capita by Gender'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Per Capita by Gender'].keys())

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

        plt.ylabel('Income in USD', fontsize=19)
        plt.xlabel('Per-capita income by gender', fontsize=19)
        plt.title('Per-capita income grouped by gender', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()

    else:
        sns.set()
        labels = list(data[0]['Per Capita by Gender'].keys())
        fracs = list(data[0]['Per Capita by Gender'].values())    
        fig = plt.figure(figsize=(20, 10)) 

        ax1 = fig.add_axes([0, 0, .5, .5], aspect=1)
        ax1.pie(fracs, labels=labels, radius = 1.2, autopct=absolute_value, textprops={'fontsize': 20})  
        ax1.set_title('Title for ax1', y=1.08, fontsize=25)    


        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)     

def occupationplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Occupation'].values()))
        means_frank = list(data[0]['Occupation'].values())
        means_guido = list(data[1]['Occupation'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Occupation'].keys())

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

        plt.ylabel('Occupation by %', fontsize=19)
        plt.xlabel('Types of Occupations', fontsize=19)
        plt.title('Labor Force by type of occupation', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Occupation'].values())
        x = list(data[0]['Occupation'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Occupation by %', fontsize=19)
        plt.xlabel('Types of Occupations', fontsize=19)
        plt.title('Labor Force by type of occupation', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)   

def workerplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Class of Worker'].values()))
        means_frank = list(data[0]['Class of Worker'].values())
        means_guido = list(data[1]['Class of Worker'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Class of Worker'].keys())

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

        plt.ylabel('Class of Worker by %', fontsize=19)
        plt.xlabel('Type of work class', fontsize=19)
        plt.title('Labor Force by Class of Worker', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Class of Worker'].values())
        x = list(data[0]['Class of Worker'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Class of Worker by %', fontsize=19)
        plt.xlabel('Type of work class', fontsize=19)
        plt.title('Labor Force by Class of Worker', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)       

def commuteplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Commuting to Work'].values()))
        means_frank = list(data[0]['Commuting to Work'].values())
        means_guido = list(data[1]['Commuting to Work'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Commuting to Work'].keys())

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

        plt.ylabel('Labor Force by %', fontsize=19)
        plt.xlabel('Type of transport taken to work', fontsize=19)
        plt.title('Means of Work Commute', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Commuting to Work'].values())
        x = list(data[0]['Commuting to Work'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Labor Force by %', fontsize=19)
        plt.xlabel('Type of transport taken to work', fontsize=19)
        plt.title('Means of Work Commute', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image) 

def vehiclesplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Vehicles Available'].values()))
        means_frank = list(data[0]['Vehicles Available'].values())
        means_guido = list(data[1]['Vehicles Available'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Vehicles Available'].keys())

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

        plt.ylabel('Households by %', fontsize=19)
        plt.xlabel('Number of Vehicles Available', fontsize=19)
        plt.title('Vehicles Available by Household', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Vehicles Available'].values())
        x = list(data[0]['Vehicles Available'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Households by %', fontsize=19)
        plt.xlabel('Number of Vehicles Available', fontsize=19)
        plt.title('Vehicles Available by Household', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image) 

def homevalchart(data):
    sns.set()
    fig, ax = plt.subplots(figsize=(20, 10))

    for i in data:
        x = list(i['Historical Property Value Data']['Average Home Value'].keys())
        y = list(i['Historical Property Value Data']['Average Home Value'].values())
        name = i['name_with_com']
        ax.plot(x, y, label = name, linewidth = 5, linestyle = '--')

    ax.set(title='')
    ax.legend(fontsize=20)
    fig.suptitle('', fontsize=20)

    plt.ylabel('Avg Home Value in USD', fontsize=19)
    plt.xlabel('Home Value by Month', fontsize=19)
    ax.xaxis.set_major_locator(plt.MaxNLocator(15))
    ax.tick_params(axis='y', which='major', labelsize=17)
    plt.xticks(fontsize=17, rotation=30)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)

def unitsinstructureplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Units in Structure'].values()))
        means_frank = list(data[0]['Units in Structure'].values())
        means_guido = list(data[1]['Units in Structure'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Units in Structure'].keys())

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

        plt.ylabel('Households by %', fontsize=19)
        plt.xlabel('Number of Units in Structure', fontsize=19)
        plt.title('', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Units in Structure'].values())
        x = list(data[0]['Units in Structure'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Households by %', fontsize=19)
        plt.xlabel('Number of Units in Structure', fontsize=19)
        plt.title('', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)     

def yearbuiltplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Year Built'].values()))
        means_frank = list(data[0]['Year Built'].values())
        means_guido = list(data[1]['Year Built'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Year Built'].keys())

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

        plt.ylabel('Households by %', fontsize=19)
        plt.xlabel('Households by Year Built', fontsize=19)
        plt.title('Household structures by year built', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Year Built'].values())
        x = list(data[0]['Year Built'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Households by %', fontsize=19)
        plt.xlabel('Households by Year Built', fontsize=19)
        plt.title('Household structures by year built', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)      

def rentplot(data):
    sns.set()
    if len(data) > 1:
    # data to plot
        n_groups = len(list(data[1]['Rent'].values()))
        means_frank = list(data[0]['Rent'].values())
        means_guido = list(data[1]['Rent'].values())
        name1 = data[0]['name_with_com']
        name2 = data[1]['name_with_com']
        x = list(data[0]['Rent'].keys())

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

        plt.ylabel('Total Rental by %', fontsize=19)
        plt.xlabel('Cost of Rent', fontsize=19)
        plt.title('Rentals Grouped by Price', fontsize=30)
        plt.xticks(index + bar_width, x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
        plt.show()
    else:
        name1 = data[0]['name_with_com']
        bar_width = 0.7
        opacity = 0.8    
        fig, ax = plt.subplots(figsize=(20, 10))
        means_frank = list(data[0]['Rent'].values())
        x = list(data[0]['Rent'].keys())
        rects1 = plt.bar(x, means_frank, bar_width,
        alpha=opacity,
        color='b',
        label=name1)
        plt.ylabel('Total Rental by %', fontsize=19)
        plt.xlabel('Cost of Rent', fontsize=19)
        plt.title('Rentals Grouped by Price', fontsize=30)
        plt.xticks(x,fontsize=17, rotation=20)

        ax.legend(fontsize=20)

        plt.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return(bytes_image)      