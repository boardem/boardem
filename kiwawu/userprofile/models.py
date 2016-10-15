from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import post
from django.contrib.auth.models import User
from post.models import textpost
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

def upload_location(instance, filename):
    return "%s/%s%s" %(instance.user, instance.slug, filename)

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
#    all_post = models.ForeignKey(textpost, on_delete=models.CASCADE)

    # photo = models.FileField(verbose_name=("Profile Picture"),
    #                   upload_to=upload_to("main.UserProfile.photo", "profiles"),
    #                   format="Image", max_length=255, null=True, blank=True)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)
    work = models.CharField(max_length=100, default='', blank=True)
    def save(self, *args, **kwargs):
        for field_name in ['country','city','organiaztion' ]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
            super(Profile, self).save(*args, **kwargs)

    def __unicode__(self):
       return self.user.first_name + " " + self.user.last_name

class Work(models.Model):
    user = models.OneToOneField(User,related_name='work', on_delete=models.CASCADE)
    Business_Name = models.CharField(max_length=100, default='', blank=True)
    Address = models.CharField(max_length=100, default='', blank=True)
    Job_Title = models.CharField(max_length=100, default='', blank=True)
    def save(self, *args, **kwargs):
        for field_name in ['businessname','jobtitle' ]:
                val = getattr(self, field_name, False)
                if val:
                    setattr(self, field_name, val.capitalize())
                super(Work, self).save(*args, **kwargs)
    def __unicode__(self):
       return self.Business_Name + " & " + self.Address

class BusinessProfile(models.Model):
    user = models.OneToOneField(User,related_name='businessprofile', on_delete=models.CASCADE)
    work = models.ForeignKey(Work,related_name='businessprofile', on_delete=models.CASCADE)
    Business_Name = models.CharField(max_length=100, default='', blank=True, unique=True)
    Address = models.CharField(max_length=100, default='', blank=True)
    def save(self, *args, **kwargs):
        for field_name in ['businessname']:
                val = getattr(self, field_name, False)
                if val:
                    setattr(self, field_name, val.capitalize())
                super(BusinessProfile, self).save(*args, **kwargs)


class ProfilePictures(models.Model):
    user = models.ForeignKey(User,related_name='profilepictures',on_delete=models.CASCADE)
    pictures = models.ImageField(upload_to=upload_location, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=100, blank=True, null=True)
    width_field = models.IntegerField(default=100, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True,unique=True)
    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name
    def get_absolute_url(self):
        return self.slug


@receiver(pre_save, sender=ProfilePictures)
def pre_save_post_receiver(sender, instance, *args, **kargs):
    if not instance.slug:
        instance.slug=create_slug(instance)

def create_slug(instance, new_slug=None):
    
    slug = slugify(instance.pictures)
    if new_slug is not None:
        slug=new_slug
    qs = ProfilePictures.objects.filter(slug=slug).order_by("-id")
    exists=qs.exists()
    if exists:
        new_slug ="%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
