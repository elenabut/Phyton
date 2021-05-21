#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задание 1
phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(phrase_1)<len(phrase_2): 
    print ('Фраза 2 длиннее фразы 1')
elif len(phrase_1)>len(phrase_2):
    print ('Фраза 1 длиннее фразы 2')
else:   
    print ('Фразы равной длины')


# In[1]:


#Задание 2
year=2019
d=year%4

if d==0:
    print ('Високосный год')
else: 
    print ('Обычный год')


# In[2]:


#Задание 3
month=input('Введите месяц')
day=int(input('Введите день'))

if month == 'Декабрь': 
      astro_sign = 'Ваш знак зодиака: Стрелец' if (day < 22) else 'Ваш знак зодиака: Козерог'
elif month == 'Январь':
      astro_sign = 'Ваш знак зодиака: Козерог' if (day < 20) else 'Ваш знак зодиака: Водолей'
elif month == 'Февраль': 
      astro_sign = 'Ваш знак зодиака: Водолей' if (day < 19) else 'Ваш знак зодиака: Рыбы'
elif month == 'Март': 
      astro_sign = 'Ваш знак зодиака: Рыбы' if (day < 21) else 'Ваш знак зодиака: Овен'
elif month == 'Апрель': 
      astro_sign = 'Ваш знак зодиака: Овен' if (day < 20) else 'Ваш знак зодиака: Телец'
elif month == 'Май': 
      astro_sign = 'Ваш знак зодиака: Телец' if (day < 21) else 'Ваш знак зодиака: Близнецы'
elif month == 'Июнь': 
      astro_sign = 'Ваш знак зодиака: Близнецы' if (day < 21) else 'Ваш знак зодиака: Рак'
elif month == 'Июль': 
      astro_sign = 'Ваш знак зодиака: Рак' if (day < 23) else 'Ваш знак зодиака: Лев'
elif month == 'Август': 
      astro_sign = 'Ваш знак зодиака: Лев' if (day < 23) else 'Ваш знак зодиака: Дева'
elif month == 'Сентябрь': 
      astro_sign = 'Ваш знак зодиака: Дева' if (day < 23) else 'Ваш знак зодиака: Весы'
elif month == 'Октябрь': 
      astro_sign = 'Ваш знак зодиака: Весы' if (day < 23) else 'Ваш знак зодиака: Скорпион'
elif month == 'Ноябрь': 
      astro_sign = 'Ваш знак зодиака: Скорпион' if (day < 22) else 'Ваш знак зодиака: Стрелец'
print(astro_sign) 


# In[4]:


#Задание 4
width = 10
length = 195
height = 5

if width<15 and length<15 and height<15:
    print ('Коробка №1')
elif (width>15 and width<50) or (length>15 and length<50) or (height>15 and height<50):
    print ('Коробка №2')
elif length>200:
    print ('Упаковка для лыж')
else:
    print ('Стандартная коробка №3')
    


# In[ ]:


#Задание 5
number = 122221
number_1 = (number//100000)*1.0
number_2 = ((number/100000 -number_1)*10)//1
number_3 = ((number/10000 -number //10000)*10)//1
number_4 = ((number/1000 -number //1000)*10)//1
number_5 = ((number/100 -number //100)*10)//1
number_6 = (number%10)*1.0

if (number_1+number_2+number_3)==(number_4+number_5+number_6):
    print ('Счастливый билет')
else:
    print ('Несчастливый билет')


# In[6]:


#Задание 6
fig=input('Введите тип фигуры')


# In[7]:


if fig=='Круг': param_1=input('Введите радиус круга:')
if fig=='Треугольник': param_2=int(input('Введите длину стороны A:'))  
if fig=='Треугольник': param_3=int(input('Введите длину стороны B:')) 
if fig=='Треугольник': param_4=int(input('Введите длину стороны C:')) 
if fig=='Прямоугольник': param_5=int(input('Введите длину стороны A:'))  
if fig=='Прямоугольник': param_6=int(input('Введите длину стороны B:'))


# In[8]:


from math import sqrt
if fig=='Круг': ans=3.14*param_1*param_1
if fig=='Треугольник': ans=sqrt((param_2 + param_3 + param_4)/2*((param_2 + param_3 + param_4)/2-param_2)*((param_2 + param_3 + param_4)/2-param_3)*((param_2 + param_3 + param_4)/2-param_4))
if fig=='Прямоугольник': ans= param_5*param_6  
print(ans) 

