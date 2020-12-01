#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json


# In[42]:


with open('result.json') as json_file:
    data = json.loads(json_file.read())


# In[48]:


for row in data.keys():
    for i in data[row].keys():
        if i == 'monthly_data':
            for m in data[row][i].keys():
                   data[row][i][m]["month"] = str(m)     #["month"] = m
        


# In[51]:


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


# In[ ]:




