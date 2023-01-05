from django.contrib import admin
from .models import Post_vero, Like_vero, tag_piaciuti

# Register your models here.
admin.site.register(Post_vero)
admin.site.register(Like_vero)
admin.site.register(tag_piaciuti)