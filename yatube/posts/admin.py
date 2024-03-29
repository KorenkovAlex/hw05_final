from django.contrib import admin

from .models import Post, Group, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'text',
                    'pub_date',
                    'author',
                    'group',
                    'image',)
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    search_fields = ('text', 'group',)
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'text',
        'post',
        'created',
    )
    search_fields = (
        'text',
        'author',
        'post',
    )
    list_filter = (
        'created',
        'author',
    )


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'user',
    )
    search_fields = (
        'author',
        'user',
    )
    list_filter = (
        'author',
        'user',
    )


admin.site.register(Post, PostAdmin)

admin.site.register(Group, GroupAdmin)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Follow, FollowAdmin)
