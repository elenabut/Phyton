#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


num_trial = 10000    # Кол-во попыток
result = 0       # Кол-во результатов
results_list = []

for i in range(num_trial):
    random_score = np.random.randint(0, 1000)    # Случайное число от 0 до 999
    if random_score == 999:
        results_list.append(100)
    elif random_score == 777:
        results_list.append(200)
    elif random_score == 555:
        results_list.append(50)
    elif random_score == 333:
        results_list.append(15)
    elif random_score == 111:
        results_list.append(10)
    elif random_score % 100 == 77:
        results_list.append(5)
    elif random_score % 10 == 7:
        results_list.append(3)    
    elif random_score % 100 == 0:
        results_list.append(2)
    elif random_score % 10 == 0:
        results_list.append(1)
    else:
        None
        result += 1

profit = sum(results_list) - num_trial
if profit > 0:
    print('Игра выгодна игроку. Выигрыш:', profit, ' Потрачено:', num_trial)
else:
    print('Игра не выгодна игроку. Проигрыш:', profit, ' Потрачено:', num_trial)

