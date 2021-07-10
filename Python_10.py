#!/usr/bin/env python
# coding: utf-8

# In[26]:





# In[17]:


#Задание 1
import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip_code']
users = pd.read_table('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Data Pandas/ml-1m/users.dat', sep='::', header=None, names=unames, engine='python')
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Data Pandas/ml-1m/ratings.dat', sep='::', header=None, names=rnames, engine='python')
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Data Pandas/ml-1m/movies.dat', sep='::', header=None, names=mnames, engine='python')

#movies[:5]
#ratings[:5]
#users[:5]

data = pd.merge(pd.merge(ratings, users), movies)
dt_rating = data.filter(items = ['movie_id', 'rating'])
dt_rating[dt_rating['rating']==5.0].sort_values(by='movie_id').value_counts().head(1)


# In[24]:


#Задание 2
data_power = pd.read_csv('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Data Pandas/power.csv')
countries = data_power[(data_power['country']=='Estonia') | (data_power['country']=='Lithuania') | (data_power['country']=='Latvia') ]
countries_1=countries[(countries['category']==4) | (countries['category']==12) | (countries['category']==21) & (countries['year']<2010) & (countries['year']>2005) & (countries['quantity']>0.0) ]
countries_1['quantity'].sum()


# In[25]:


#Задание 3
data=pd.read_html('https://fortrader.org/quotes')[1]
data.head()

