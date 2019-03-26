from django.db import models

# Create your models here.
from django.db.models import ForeignKey

class Topic(models.Model):
    '''主题'''
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text

class Entry(models.Model):
    '''上边某个主题的具体内容'''
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)
    class Meta:  #储存用于模型管理的额外信息
        verbose_name_plural = 'entries'
    def __str__(self):
        return self.text
