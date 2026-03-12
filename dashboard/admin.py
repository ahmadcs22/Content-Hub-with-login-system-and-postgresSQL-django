from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, VideoIdea, ResourceLink

# This tells Django to use the default User layout for your CustomUser
admin.site.register(CustomUser, UserAdmin)
admin.site.register(VideoIdea)
admin.site.register(ResourceLink)
