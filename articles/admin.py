from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [CommentInLine]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'approved', 'date')
    list_filter = ('approved', 'date')
    actions = ['approve_articles']  # Admin uchun tasdiqlash uchun action

    def approve_articles(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
