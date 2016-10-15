from django.contrib import admin
from .models import textpost
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import admin
from django.contrib.auth.models import User

from post.models import textpost, Images

#class create_post_admin(admin.ModelAdmin):
#    list_disply = ["__unicode__", "timestamp", "updated"]
#    form = create_post_form

class textpostusers(admin.StackedInline):
#    list_display = ["__unicode__","date_updated", "time_stamp", "id", "slug"]
#    list_filter = ["date_updated", "time_stamp"]
#    search_fields = ["text_post_title", "text_post_content", "id", "slug"]
    model = textpost
    can_delete = True
    verbose_name_plural = 'textpost'




class UserAdmin(BaseUserAdmin):
     inlines = (textpostusers, )


# Re-register UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#admin.site.register(textpost)
# admin.site.register(Images)

#admin.site.register(usermassdata)
