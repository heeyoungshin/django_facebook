from django.contrib import admin

# Register your models here.
from facebook.models import Article

admin.site.register(Article)

from django.contrib import admin
from facebook.models import Comment
admin.site.register(Comment)