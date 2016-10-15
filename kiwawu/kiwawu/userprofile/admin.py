from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from userprofile.models import Profile, Work, BusinessProfile,ProfilePictures

class profile(admin.StackedInline):
#    list_display = ["__unicode__","date_updated", "time_stamp", "id", "slug"]
#    list_filter = ["date_updated", "time_stamp"]
#    search_fields = ["text_post_title", "text_post_content", "id", "slug"]
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class Work(admin.StackedInline):
    model = Work
    can_delete = False
    verbose_name_plural = 'Work'

class ProfilePictures(admin.StackedInline):
    model = ProfilePictures
    can_delete = True
    verbose_name_plural = 'ProfilePictures'



class UserAdmin(BaseUserAdmin):
    inlines = (profile,Work,ProfilePictures )


# class BusinessProfile(admin.ModelAdmin):
#     model = BusinessProfile
#     fields = ('Business_Name','Address',)

# Re-register UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(BusinessProfile)

admin.site.register(Profile)
