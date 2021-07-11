#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Задание 5. Работа с файловой системой
#1

import os
for file in os.listdir('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Файлы к ДЗ Файловая система/Downloads'):
    print(file)


# In[5]:


import json


# In[6]:


purchases = {}
with open('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Файлы к ДЗ Файловая система/Downloads/purchase_log.txt', 'r', encoding = 'utf-8') as f :
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        key = dict_['user_id']
        value = dict_['category']
        if key!= 'user_id':
            purchases.setdefault(key,value)


# In[ ]:


#Задание 5. Работа с файловой системой
#2
import json
purchases_2 = []
with open('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Файлы к ДЗ Файловая система/Downloads/purchase_log.txt', 'r', encoding = 'utf-8') as f_1 :
    for line in f_1:
        dict_ = json.loads(line)
        purchases_2.append(dict_)
def products(name):
    for d in purchases_2:
        if (d['user_id'] == name):
            return d['category']
    return None
with open('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Файлы к ДЗ Файловая система/Downloads/visit_log.csv', 'r') as f:
    with open('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Файлы к ДЗ Файловая система/Downloads/funnel4.csv', 'w') as funnel:
        for line in f:
            user_id =line.strip().split(',')[0]
            category = products(user_id)
            if category:
                line_out = line.rstrip() + ', ' + str(category) + '\r'
                funnel.write(line_out)

