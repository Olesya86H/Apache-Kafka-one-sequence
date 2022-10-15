#!/usr/bin/env python
# coding: utf-8

# In[1]:


from time import sleep
from json import dumps
from kafka import KafkaProducer


# In[2]:


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'),
                         api_version=(0, 10, 1),
                         security_protocol='PLAINTEXT')


# In[3]:


for e in range(10):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(1)


# In[ ]:




