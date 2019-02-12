# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Article(models.Model):
    sumbitter = models.ForeignKey(User)
    submitted_date = models.DateTimeField(default=now, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
