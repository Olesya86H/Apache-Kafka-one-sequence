#!/usr/bin/env python
# coding: utf-8

# In[1]:


from kafka import KafkaConsumer
from json import loads


# In[2]:


consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')),
     api_version=(0, 10, 1),
     security_protocol='PLAINTEXT')


# In[ ]:


for message in consumer:
    message = message.value
    print('{} added'.format(message))


# In[ ]:




