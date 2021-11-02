#!/usr/bin/env python
# coding: utf-8

# Задание 1. Загрузка данных

# In[7]:


import pandas as pd

hnames = ['surgery', 'Age', 'rectal_temperature', 'pulse', 'respiratory_rate', 'temperature_of_extremities', 'pain', 'outcome']
hnumber = [0, 1, 3, 4, 5, 6, 10, 22]
na_values = ['?']

horse_data = pd.read_csv('C:/Users/bev20/OneDrive/Desktop/Курс Phyton/3 часть/1/практика_и_дз/horse_data.csv', usecols=hnumber, sep=',', na_values = na_values, header=None, names=hnames, engine='python')
horse_data.head()
horse_data.info()


# Задание 2. Первичное изучение данных

# Анализ значений по столбцам

# In[9]:


horse_data.describe()
horse_data.describe(include = 'all')


# Базовые статистики/выбросы

# Мода, Медиана, СКО, Дисперсия

# In[11]:


print('\n Медиана')
for j in horse_data.columns:
    print( j,':',horse_data[j].median())
print('\n Мода')
for j in horse_data.columns:
    print(j,':',horse_data[j].mode())
print('\n СКО')
for j in horse_data.columns:
    print(j,':',horse_data[j].std())
print('\n Дисперсия')
for j in horse_data.columns:
    print(j,':',horse_data[j].var())


# Выбросы (межквартильный размах)

# In[15]:


for j in horse_data.columns:
    horse_data[j].describe()
    q1 = horse_data[j].quantile(0.25)
    q3 = horse_data[j].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5)*iqr
    upper_bound = q3 + (1.5)*iqr
    remove_outliers= horse_data[~horse_data[j].between(lower_bound, upper_bound, inclusive=True)].sort_values(j)
    print(remove_outliers)


# Задание 3. Работа с пропусками

# In[33]:


import seaborn as sns
horse_data.info()
# Заполняем пропуски в surgery, outcome, rectal_temperature, pulse, respiratory_rate, temperature_of_extremities, pain
# Анализ проведено на основании распределения

#surgery_plot= sns.countplot(x = 'surgery', data = horse_data.sort_values('surgery'))
# surgery заполняем 1 (чаще встречается, 1 пропуск, оправдано)

#outcome_plot= sns.countplot(x = 'outcome', data = horse_data.sort_values('outcome'))
# outcome заполняем 1 (чаще встречается, 1 пропуск, оправдано)

#rectal_temp_plot= sns.histplot(x = 'rectal_temperature', data = horse_data)
# Нормальное распределение. Заменяем средним значением

#pulse_plot= sns.histplot(x = 'pulse', data = horse_data)
# Исходя из распределения (скошено влево) можно заменить медианой. Либо средним значением по группировке по возрасту (кажется интуитивно верным)

#respiratory_rate_plot= sns.histplot(x = 'respiratory_rate', data = horse_data)
# Исходя из распределения (скошено влево) можно заменить медианой. Либо средним значением по группировке по возрасту (кажется интуитивно верным)

#temperature_of_ext_plot= sns.countplot(x = 'temperature_of_extremities', data = horse_data.sort_values('temperature_of_extremities'))
# Заполняем 3 (чаще встречается)

#pain_plot= sns.countplot(x = 'pain', data = horse_data.sort_values('pain'))
# Заполняем 3 (чаще встречается)


# Формируем новый дата-фрейм с заменой пропусков

# In[35]:


horse_data_final = horse_data
horse_data_final['surgery'].fillna(1, inplace = True)
horse_data_final['outcome'].fillna(1, inplace = True)
horse_data_final['rectal_temperature'] = horse_data_final['rectal_temperature'].fillna(horse_data['rectal_temperature'].mean())
horse_data_final['pulse'] = horse_data_final['pulse'].fillna(horse_data.groupby('Age')['pulse'].transform('mean'))
horse_data_final['respiratory_rate'] = horse_data_final['respiratory_rate'].fillna(horse_data.groupby('Age')['respiratory_rate'].transform('mean'))
horse_data_final['temperature_of_extremities'].fillna(3, inplace = True)
horse_data_final['pain'].fillna(3, inplace = True)


# In[38]:


horse_data_final.info()


# In[ ]:




