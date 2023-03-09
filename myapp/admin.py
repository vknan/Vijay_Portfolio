from django.contrib import admin
from .models import Feature,Category,Post, Comment, Contact
 
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'posted_at')
    list_filter = ('is_published', 'posted_at')
    list_editable = ('is_published',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_resolved', 'commented_at')
    list_filter = ('is_resolved', 'commented_at')
    list_editable = ('is_resolved',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject', 'contacted_date','is_resolved')
    list_filter = ('contacted_date', 'is_resolved')
    list_editable = ('is_resolved',)

admin.site.register(Feature) 
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)