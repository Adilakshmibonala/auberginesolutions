from django.contrib import admin

# Register your models here.
from posts.models import User, BlogPost, Comments

admin.site.register(User)
admin.site.register(BlogPost)
admin.site.register(Comments)
