from django.contrib import admin

# Register your models here.
from .models import Post, Category

from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    pass
    summernote_fields = ('body',)


class CategoryAdmin(admin.ModelAdmin):

    pass


admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)
