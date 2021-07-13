#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Задание 1
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
lst = ids.values()
new_lst = []
for i in lst:
    for j in i:
        new_lst.append(j)
print(set(new_lst))


# In[5]:


#Задание 2
queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]

storage = {}

for i in queries:
    cnt_word = i.split()

    if len(cnt_word) in storage.keys():
        storage[len(cnt_word)] += 1
    else:
        storage.update({
            len(cnt_word): 1
        })

for key, value in storage.items():
    prc = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов, содержащих {key} слов(а): {prc}%')


# In[7]:


#Задание 3
results = {
'vk': {'revenue': 103, 'cost': 98},
'yandex': {'revenue': 179, 'cost': 153},
'facebook': {'revenue': 103, 'cost': 110},
'adwords': {'revenue': 35, 'cost': 34},
'twitter': {'revenue': 11, 'cost': 24},
}

for key, value in results.items():
    value['ROI'] = round(((value['revenue'] / value['cost']) - 1)*100 , 2)
    print(key, value)


# In[3]:


#Задание 4
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
max_stat = 0
res = str()
for key, vl in stats.items():
    if (vl > max_stat):
        max_stat = vl
        res = key
print(f'Максимальный объем продаж на рекламном канале:', res)

