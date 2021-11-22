#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Creating a model for fetching videos from YouTube using APIs.


# In[ ]:


from django.db import models

# Create OUR models here.
class Videos(models.Model):
    title = models.CharField(null=True,blank=True,max_length=500)                               # Title Of the Video
    description = models.CharField(null=True, blank=True, max_length=6000)                      # Description Of the Video
    publishingDateTime = models.DateTimeField()                                                 # Publish date/time Of the Video
    thumbnailsUrls = models.URLField()                                                          # URL Of the Thumbnail
    channelTitle = models.CharField(null=True,blank=True,max_length=500)                        # Title/Name Of the Channel

