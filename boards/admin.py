from django.contrib import admin
from boards.models import *


class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_time']

class BoardUsersAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'board', 'is_owner', 'is_reader']
    search_fields = ['user']

class BoardColumnsAdmin(admin.ModelAdmin):
    list_display = ['id', 'board', 'title', 'create_time', 'sort_index']
    search_fields = ['title']

class BoardCardsAdmin(admin.ModelAdmin):
    list_display = ['id', 'board', 'title', 'create_time', 'sort_index', 'column', 'description']
    search_fields = ['column']

class BoardCardCommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'card', 'comment', 'create_time']
    search_fields = ['card']

class BoardUserExecutorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'card']

admin.site.register(BoardUserExecutors, BoardUserExecutorsAdmin)
admin.site.register(BoardCardComments, BoardCardCommentsAdmin)
admin.site.register(BoardCards,BoardCardsAdmin)
admin.site.register(BoardColumns, BoardColumnsAdmin)
admin.site.register(BoardUsers, BoardUsersAdmin)
admin.site.register(Board, BoardAdmin)

