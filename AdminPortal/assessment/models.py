from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from .choices import *






class Assessment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    Profile = models.CharField(choices=PROFILE_CHOICES, max_length=50)
    Primary_category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    assessment_name = models.CharField(max_length=50)

class Question(models.Model):
    #assessment= models.ForeignKey(Assessment)
    qid=models.IntegerField( )
    qtype= models.CharField(max_length=50)
    text_question = models.TextField(null = True)
    ans_detail1 = models.TextField(null=True,)
    ans_detail2 = models.TextField(null=True)
    ans_detail3 = models.TextField(null=True)
    ans_detail4 = models.TextField(null=True)
    ans_detail5 = models.TextField(null=True)
    ans_detail6 = models.TextField(null=True)
