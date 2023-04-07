from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Cplus_plus_Message(models.Model):

    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.author.username
 
    def last_10_msgs():
        return Cplus_plus_Message.objects.order_by('-date_posted').all()[:15]
 
class Python_Message(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.author.username
 
    def last_10_msgs():
        return Python_Message.objects.order_by('-date_posted').all()[:15]
 
class Java_Message(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.author.username
 
    def last_10_msgs():
        return Java_Message.objects.order_by('-date_posted').all()[:15]
 
class Javascript_Message(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.author.username
 
    def last_10_msgs():
        return Javascript_Message.objects.order_by('-date_posted').all()[:15]
 
class Css_Message(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.author.username
 
    def last_10_msgs():
        return Css_Message.objects.order_by('-date_posted').all()[:15]
 
class Html_Message(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.author.username
 
    def last_10_msgs():
        return Html_Message.objects.order_by('-date_posted').all()[:15]







