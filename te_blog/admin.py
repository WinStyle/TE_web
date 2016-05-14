from django.contrib import admin
from te_blog import models
# Register your models here.
class TE_BLOG_admin(admin.ModelAdmin):
    list_display = ('title','summary','author','signature','view_count','created_at')
    list_filter = ('created_at',)
    search_fields = ('title','author__user__username')

    def signature(self,obj):
        return obj.author.signature

class TE_user_admin(admin.ModelAdmin):
    list_display = ('user','signature','ext','mobile')

admin.site.register(models.TE_BLOG,TE_BLOG_admin)
admin.site.register(models.Category)
admin.site.register(models.TE_user,TE_user_admin)