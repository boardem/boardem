from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import datetime
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class postmanager(models.Manager):
    def all(self, *args, **kwargs):
        return super(postmanager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
    return "%s%s" %(instance.slug, filename)


class textpost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text_post_title = models.CharField(max_length=500, blank=False)
    text_post_content = models.CharField(max_length=9999999, blank=False)
    comments_select = models.BooleanField(default=True)
    comments_text = models.CharField(max_length=500, blank=False)
    time_stamp = models.DateTimeField(auto_now_add=False, auto_now=True)

    date_updated = models.DateTimeField(auto_now=True)
    pictureupload = models.ImageField(upload_to=upload_location, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=100, blank=True, null=True)
    width_field = models.IntegerField(default=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now_add=False, auto_now=False)

    objects= postmanager()
    def save(self, *args, **kwargs):
       for field_name in ['text_post_title','text_post_content']:
           val = getattr(self, field_name, False)
           if val:
               setattr(self, field_name, val.capitalize())
           super(Profile, self).save(*args, **kwargs)

    def __unicode__(self):
       return self.text_post_title



    def get_absolute_url(self):
        return reverse ("post:postdetail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-time_stamp","-date_updated"]



def get_image_filename(instance, filename):
    title = instance.post.text_post_title
    slug = slugify(title)
    return "%s%s" % (slug, filename)

class Images(models.Model):
    post = models.ForeignKey(textpost, default=None)
    image = models.ImageField(upload_to=get_image_filename,verbose_name='Image', null= True,blank=True)

def create_slug(instance, new_slug=None):
    slug = slugify(instance.text_post_title)
    if new_slug is not None:
        slug=new_slug
    qs = textpost.objects.filter(slug=slug).order_by("-id")
    exists=qs.exists()
    if exists:
        new_slug ="%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kargs):
    if not instance.slug:
        instance.slug=create_slug(instance)






pre_save.connect(pre_save_post_receiver, sender=textpost)
