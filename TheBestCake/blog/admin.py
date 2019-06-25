from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','published')
    ordering=('published',)
    search_fields=('title','published')

admin.site.register(Post,PostAdmin)