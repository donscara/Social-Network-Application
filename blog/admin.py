from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'published_date', )
    list_filter = ('created_date', 'published_date', 'author')
    search_fields = ('body',)
    prepopulated_fields = {'body': ('body',)}
    # removes combobox, creates search text input field
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ('published_date',)

