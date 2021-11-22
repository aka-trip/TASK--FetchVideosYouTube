#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ASGI exposes the ASGI callable as a module-level variable named ``application``


# In[ ]:


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fetch_api.settings')

application = get_asgi_application()

