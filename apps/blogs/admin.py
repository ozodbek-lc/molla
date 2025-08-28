from django.contrib import admin
from apps.blogs.models import *

admin.site.register(CategoryModel)
admin.site.register(PostModel)
admin.site.register(TagModel)
admin.site.register(AuthorModel)
