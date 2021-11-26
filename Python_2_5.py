#!/usr/bin/env python
# coding: utf-8

# ### Задание 1

# Будем парсить страницу со свежеми новостям на habr.com/ru/all/.
# 
# Вам необходимо собирать только те статьи, в заголовках которых встречается хотя бы одно требуемое ключевое слово. Эти слова определяем в начале кода в переменной, например:
# 
# KEYWORDS = [‘python’, ‘парсинг’]
# 
# Поиск вести по всей доступной preview-информации (это информация, доступная непосредственно с текущей страницы).
# 
# В итоге должен формироваться датафрейм вида: <дата> - <заголовок> - <ссылка>

# In[115]:


import pandas as pd
import requests as req
import time
from bs4 import BeautifulSoup
import json


# In[86]:


KEYWORDS = ['python', 'парсинг', 'html']
URL = 'https://habr.com/ru/all/'


# In[90]:


def pars_habr(URL, KEYWORDS):
    res_h = req.get(URL)
    df = pd.DataFrame()

    soup = BeautifulSoup(res_h.text, 'html.parser')
    posts = soup.find_all('article', class_='tm-articles-list__item')

    for post in posts:
        texts = post.find_all('div', class_='tm-article-snippet')
        for text_ in texts:
            text_universal = text_.text.lower()
            if any([key in text_universal for key in KEYWORDS]):
                title_ = post.find('h2', class_='tm-article-snippet__title').text
                date_ = post.find('span', class_='tm-article-snippet__datetime-published').time.attrs['title']
                href_ = 'https://habr.com/ru/post/' + post.attrs['id']
                df = df.append({'Дата': date_, 'Заголовок': title_, 'Ссылка': href_}, ignore_index=True)
    display(df)


# In[91]:


pars_habr(URL, KEYWORDS)


# 

# 

# In[107]:





# In[116]:





# In[117]:





# ### Задание 2  

# Написать скрипт, который будет проверять список e-mail адресов на утечку при помощи сервиса Avast Hack Ckeck. Список email-ов задаем переменной в начале кода:
# EMAIL = [xxx@x.ru, yyy@y.com]
# 
# В итоге должен формироваться датафрейм со столбцами: <дата утечки> - <источник утечки> - <описание утечки>
# 
# Подсказка: сервис работает при помощи “скрытого” API. Внимательно изучите post-запросы.

# In[119]:


import json

email = ['xxx@x.ru', 'yyy@y.com', 'bev20@mail.ru']
js_email = json.dumps({'emailAddresses': email})


# In[120]:


link = 'https://identityprotection.avast.com/v1/web/query/site-breaches/unauthorized-data'
headers = {'Vaar-Version': '0',
           'Vaar-Header-App-Product-Name': 'hackcheck-web-avast',
           'Vaar-Header-App-Build-Version': '1.0.0'
          }

req = requests.post(link, data = js_email, headers = headers)


# In[121]:


dict_result = req.json()


# In[122]:


df = pd.DataFrame(columns = ('Дата утечки', 'Источник утечки', 'Описание утечки'))

for breach in dict_result['breaches'].values():
    df = df.append({'Дата утечки': breach['publishDate'],
                                      'Источник утечки': breach['site'],
                                      'Описание утечки': breach['description']
                                     }, ignore_index = True)
    
df


# In[ ]:





# In[ ]:





# 

# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




