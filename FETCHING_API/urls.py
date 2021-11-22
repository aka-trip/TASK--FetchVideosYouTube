#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""FETCHING_API URL Configuration

The `urlpatterns` list routes URLs to views. 
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# In[ ]:


from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/',views.fetch_new_posts),                    # /new of localhost - This endpoint is responsible for fetching all videos
    path('',views.VideoList.as_view()),                    # homepage of localhost- This endpoint is responsible for showing all videos
]


# In[ ]:




