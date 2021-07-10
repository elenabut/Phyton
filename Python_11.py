#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Задание 1
import pandas as pd
movies = pd.read_csv('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Data Func Pandas/movies.csv')
rating = pd.read_csv('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Data Func Pandas/ratings.csv')
rating.head()

def grp_movies(row):
    if row['rating'] <= 2.0:
        return 'низкий рейтинг'
    elif 2.0 < row['rating'] <= 4.0:
        return 'средний рейтинг'
    else:
        return 'высокий рейтинг'
rating['class'] = rating.apply(grp_movies, axis=1)
rating.head()


# In[15]:


#Задание 2
geo_data = {

'Центр':['москва', 'тула', 'ярославль'],

'Северо-Запад':['петербург', 'псков', 'мурманск'],

'Дальний Восток':['владивосток', 'сахалин', 'хабаровск'] 
}

keywords = pd.read_csv('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Data Func Pandas/keywords.csv')
keywords.head()

for i in range(0,10000):
    for key, val in geo_data.items():
        for city in val:
            if city in keywords['keyword'][i].split():
                print(city)


# In[17]:


def region(i):
    for key, val in geo_data.items():
        for city in val:
            if city in i['keyword'].split():
                return city
    return 'undefined'

keywords['region'] = keywords.apply(region, axis=1)
keywords[:50]

