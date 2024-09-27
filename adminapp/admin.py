from django.contrib import admin
from .models import ArticleComments, Articles, UserBlocks

class ArticleCommentsAdmin(admin.ModelAdmin):
    search_fields = ['content', '=authorid']

class ArticlesAdmin(admin.ModelAdmin):
    search_fields = ['=authorid', 'content']

class UserBlocksAdmin(admin.ModelAdmin):
    search_fields = ['=userid']

admin.site.register(ArticleComments, ArticleCommentsAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(UserBlocks, UserBlocksAdmin)
