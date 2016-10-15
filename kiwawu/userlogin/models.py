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
