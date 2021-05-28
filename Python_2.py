#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Задание 1
word = 'testing'

if len(word) % 2 == 0:
    word_smb = len(word) // 2
    print(word[word_smb -1 : word_smb + 1])
else: 
    word_smb = len(word)// 2 + 1
    print(word[-word_smb])


# In[4]:


#Задание 2
numb = int(input('Введите число:'))
numb_sum = 0

while numb:
    numb_sum += numb
    numb = int(input('Введите число:'))
print(numb_sum)


# In[3]:


#Задание 3
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print('Внимание, кто-то может остаться без пары!')
else:
    result = zip(sorted(boys), sorted(girls))
for couple in result:
    print(couple[0], 'и', couple[1]) 


# In[9]:


#Задание 4
countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print('Средняя температура в странах')

for avg_temp in countries_temperature:
    print(avg_temp[0], '-', round((sum(avg_temp[1]) / len(avg_temp[1]) - 32) *5 / 9, 1), 'C')

