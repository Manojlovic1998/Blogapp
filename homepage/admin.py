from django.contrib import admin
from .models import BlogPost, Tag, Category, PostCategory, PostTag


class PostCategoryAdmin(admin.TabularInline):
    model = PostCategory
    readonly_fields = ['post', 'category']


class PostTagAdmin(admin.TabularInline):
    model = PostTag
    readonly_fields = ['post', 'tag']


class TagAdmin(admin.ModelAdmin):
    ordering = ['title']


class CategoryAdmin(admin.ModelAdmin):
    ordering = ['title']


class BlogPostAdmin(admin.ModelAdmin):
    inlines = (PostCategoryAdmin, PostTagAdmin)
    ordering = ['published_at']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
