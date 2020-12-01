#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
import sys
import json
import numpy as np
import matplotlib.pyplot as plt

data = "https://result-d7a54.firebaseio.com/.json"

data = json.loads(requests.get(data).text)

#print(data)



# In[ ]:





# In[ ]:





# In[75]:



def find(district,month_input):
        for i in data:
            d = i['district']
            if(d == district):
                month_data = i['monthly_data']
                for m in month_data:
                    if m != None:
                        if(month_input == m['month']):
                            return str(m)


# In[64]:


def plot(district):
    area_data = []
    for i in data:
            d = i['district']
            if(d == district):
                month_data = i['monthly_data']
                for m in month_data:
                    if m != None:
                            area_data.append(m)
    covid_data=[]
    unemploy_data = []
    for m2 in area_data:
        covid_data.append([float(m2['month']),float(m2['CovidIncreasingRate'])])
        unemploy_data.append([float(m2['month']),float(m2['UnemploymentRate'])])
    c_date = [i[0] for i in covid_data]
    c_value = [i[1] for i in covid_data]
    plt.figure(1)
    plt.plot(c_date, c_value, '-o', color="blue", markeredgecolor="black")
    plt.title('covid cases')
    plt.figure(2)
    u_date = [i[0] for i in unemploy_data]
    u_value = [i[1] for i in unemploy_data]
    plt.plot(u_date, u_value, '-o', color="blue", markeredgecolor="black")
    plt.title('unemployment rate recently')
    plt.show()

#plot('Cook,Illinois')
# In[66]:





# In[ ]:





# In[60]:





# In[ ]:




