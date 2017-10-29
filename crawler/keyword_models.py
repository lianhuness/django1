# coding=utf-8
# author= YQZHU


from django.db import models


class Keyword(models.Model):
    words = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.words
