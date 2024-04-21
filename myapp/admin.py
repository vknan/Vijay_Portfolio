from django.contrib import admin
from .models import Category,Post, Comment, Contact, Course
# # Unregister your User model
# admin.site.unregister(User)
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login')
    

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

admin.site.register(Course, CourseAdmin) 
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)

#------------------------------------------------------------------------------------------------

# from .models import ProductCategory, Product, Customer, OrderItem, Review

# class OrderItemInline(admin.TabularInline):
#     model = OrderItem

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'product_category', 'price_actual', 'discounted_price', 'avg_rating']
#     list_editable = ['price_actual', 'discounted_price']
#     list_filter = ['product_category']

#     inlines = [OrderItemInline]

# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ['product', 'customer', 'ordered', 'date_added']
#     list_editable = ['ordered']
#     list_filter = ['date_added']

# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'product', 'rating', 'comment']
#     list_filter = ['customer', 'product']

# admin.site.register(ProductCategory)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Customer)
# admin.site.register(OrderItem, OrderItemAdmin)
# admin.site.register(Review, ReviewAdmin)
# admin.site.register(FilesAdmin)