#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Задание 5. Работа с файловой системой
#1

import os
for file in os.listdir('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Файлы к ДЗ Файловая система/Downloads'):
    print(file)


# In[35]:


import json


# In[40]:


#Вопрос: почему в open необходимо указать весь путь к файлу?Если он был считан на предыдущем шаге?#
with open('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Файлы к ДЗ Файловая система/Downloads/purchase_log.txt', 'r', encoding = 'utf-8') as f :
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        id_=dict_['user_id']
        value = dict_['category']
        purchases = {id_ : value}
        if id_!='user_id':
            print(purchases)


# In[79]:


#Задание 5. Работа с файловой системой
#2
# Не могу разобраться, в чем ошибка?

with open('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Файлы к ДЗ Файловая система/Downloads/visit_log.csv', 'r') as f, open('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/Файлы к ДЗ Файловая система/Downloads/funnel.csv', 'w') as funnel:
    for line in f:
        cat = line.strip().split(',')
        if cat[0] in purchases.keys(): 
            cat.append(purchases[cat[0]])
            add_line=','.join(cat)
        elif cat[0]=='user_id':
            cat.append('category')
            add_line=','.join(cat)
        else:
            add_line=','.join(cat)
        funnel.write(add_line+'\n')

