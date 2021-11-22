#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from django.contrib import admin


# In[ ]:


from .models import Videos
# Will Register our models here. 
# After writing model in MODELS.py register the model here and make migrations

admin.site.register(Videos)
  


# In[ ]:


from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

