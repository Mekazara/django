from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Blog)
admin.site.register(Post)

# admin.site.register([Blog, Post])  #doesn't matter