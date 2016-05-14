from django.db import models
from test.test_imageop import MAX_LEN
from django.contrib.auth.models import User
# Create your models here.

class TE_BLOG(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    author = models.ForeignKey('TE_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('TE_user')

class TE_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128,default='This guy is too lazy to leave anything here.')
    photo = models.ImageField(upload_to="/statics/upload_imgs/",default="/statics/upload_imgs/back_001.jpg")
    ext = models.CharField(max_length=10)
    mobile = models.CharField(max_length=14)
    def __unicode__(self):
        return self.user.username


