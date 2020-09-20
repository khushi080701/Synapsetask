#!/usr/bin/env python
# coding: utf-8

# In[675]:


import pandas as pd
import numpy as np
import random
import json
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize


# In[676]:


#to display all rows
#pd.set_option("display.max_rows",None)


# In[725]:


#store the data of json file
with open("data1.json") as f :
    data1 = json.load(f)


# In[726]:


#store the data as list of dictionaries
data2 = data1['data']
#convert data to DataFrame
df = pd.DataFrame(data2)


# In[727]:


#fill all nan with 0
df = df.fillna(0)
#adding the location as columns by dropping and joining columns of location
location=pd.json_normalize(df.location)
df=pd.DataFrame.join(df,location)
df=df.drop(["location"],axis=1)


# In[728]:


df


# In[729]:


#constraints
#category should be sports or enivronment
df = df[(df["category"] == 'Sports')|(df["category"]=='Environment')]
#Only the people who are interested in funding the project
df = df[df["event_name"]=="Fund Project"]
#the funding amount should be greater than 20
df = df[df["amount"] > 20]
df


# In[730]:


#replacing the age with respect to the range given 
#replacing marital_status,device,category,event_name,gender
df1 = df.copy()
df1["age"]=df1["age"].replace({'18-24':22,'25-34':30, '35-44':40,'45-54':50,'55+':60})
df1["marital_status"]=df1["marital_status"].replace({"single":1,"married":2})
df1["device"] = df1["device"].replace({"android":1,"iOS":2})
df1["gender"] = df1["gender"].replace({"M":1,"F":2,"U":3})
df1["event_name"] = df1["event_name"].replace({"View Project":1,"Fund Project":2})
df1["category"] = df1["category"].replace({"Sports":1,"Environment":2})


# In[731]:


df1


# In[732]:


df


# In[733]:


#to see the maximum and minimum correlation 
import seaborn as sb
plt.figure(figsize=(10,10))
corr=df1.corr()
heatmap=sb.heatmap(corr)
plt.show()


# In[734]:


#dropping the unneccessary columns
df.drop(["client_time","event_name"],axis="columns")
df


# In[735]:


#sorting the values of category i.e 1 for Sports and 2 for Environment
df = df.sort_values(["category"])
df


# In[736]:


#drop the duplicates
df = df.drop_duplicates(["session_id","category"])
df


# In[737]:


#reset the index
df.reset_index(inplace=True, drop=True)
df


# In[738]:


gen=df.groupby(['gender']).size().to_frame(name='count').reset_index()
print(gen)


# In[739]:


plt.figure(figsize=(16,10))
# plot chart
ax1 = plt.subplot(121, aspect='equal')
gen.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%', 
 startangle=90, shadow=False, labels=gen['gender'], legend = False, fontsize=12)
# plot table
ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, gen, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
plt.show()


# In[740]:


age=df.groupby(['age']).size().to_frame(name='count').reset_index()
print(age)


# In[741]:


plt.figure(figsize=(16,10))
# plot chart
ax1 = plt.subplot(121, aspect='equal')
age.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%', 
 startangle=90, shadow=False, labels=age['age'], legend = False, fontsize=12)
# plot table
ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, age, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
plt.show()


# In[742]:


marital=df.groupby(['marital_status']).size().to_frame(name='count').reset_index()
print(marital)


# In[743]:


plt.figure(figsize=(16,10))
# plot chart
ax1 = plt.subplot(121, aspect='equal')
marital.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%', 
 startangle=90, shadow=False, labels=marital['marital_status'], legend = False, fontsize=12)
# plot table
ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, marital, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
plt.show()


# In[744]:


dev=df.groupby(['device']).size().to_frame(name='count').reset_index()
print(dev)


# In[745]:


plt.figure(figsize=(16,10))
# plot chart
ax1 = plt.subplot(121, aspect='equal')
dev.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%', 
 startangle=90, shadow=False, labels=dev['device'], legend = False, fontsize=12)
# plot table
ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, dev, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
plt.show()


# In[746]:


df2=pd.DataFrame(columns=["class","count"])
for name,group in grouped:
    df3=pd.DataFrame(data=[[name,group.shape[0]]],columns=["class","count"])
    df2 = pd.concat([df2,df3], axis=0)
df2.reset_index(inplace=True,drop=True)
df2


# In[747]:


plt.figure(figsize=(16,10))
# plot chart
ax1 = plt.subplot(121, aspect='equal')
df2.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%', 
 startangle=90, shadow=False, labels=df2['class'], legend = False, fontsize=7)
# plot table
ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, df2, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
plt.show()


# In[748]:


'''
c a g m d
size, color
'''
groupByLi = []
li = []
length = 1
for i in ['category','age','gender','marital_status','device']:
    groupByLi.append(i) 
    li1=[]
    length *= len(cga.groupby(i))
    #print(len(cga.groupby(i)))
    for j in range(length):
        value = df.groupby(groupByLi).size()[j]
        li1.append(value)
        #print(li1)
    li.append(li1)
#print(li)
#-->[[3025, 3058], [1547, 366, 368, 375, 369], [714, 698, 135], [460, 254], [113, 347]]
    
colors = [['#294736', '#79b593'], ['#b9eef0', '#79d8db', '#3cc5c9', '#189fa3', '#29878a'], ['#ae56d6', '#8223ad', '#65357a'], ['#db429e', '#a30f68'], ['#dbac5a', '#8a5f13']]

plt.pie(li[4], colors=colors[4],radius=1.50, startangle=90)
plt.pie(li[3], colors=colors[3],radius=1.20, startangle=90)
plt.pie(li[2], colors=colors[2],radius=1.00, startangle=90)
plt.pie(li[1], colors=colors[1],radius=0.50, startangle=90)
plt.pie(li[0], colors=colors[0],radius=0.30, startangle=90)


centre_circle = plt.Circle((0,0),0.10,color='black', fc='white',linewidth=0)
fig.gca().add_artist(centre_circle)
fig = plt.gcf()

plt.axis('equal')
plt.tight_layout()
plt.show()


# In[749]:


location1


# In[760]:


import plotly.express as px

fig = px.scatter_mapbox(location, lat="latitude", lon="longitude", hover_name="city", hover_data=["state", "zip_code"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_layout(
        title = 'Locations in which people are interested in funding and viewing this project',
        geo_scope='usa',
    )
fig.show()


# In[759]:


import plotly.express as px

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="city", hover_data=["state", "zip_code"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_layout(
        title = 'Locations in which people are interested in funding the project',
        geo_scope='usa',
    )
fig.show()


# In[ ]:


#indicator
#shadow effect 3d


# In[779]:


loc=df.groupby(['city']).reset_index()
loc


# In[ ]:




