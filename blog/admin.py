from django.contrib import admin
from blog.models import post
# Register your models here.

class PostAdmin(admin.ModelAdmin) :
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopular_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']

admin.site.register(post,PostAdmin)
