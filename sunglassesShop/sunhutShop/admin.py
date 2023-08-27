from django.contrib import admin
from .models import Brand,Product
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

class ProductAdmin(admin.ModelAdmin):
    list_display = ["brand","model_code",]
    list_filter = ["category",]
    prepopulated_fields = {'slug': ('category',)}

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

    def has_view_permission(self, request, obj=None):
        return True

admin.site.register(Brand,BrandAdmin)
admin.site.register(Product,ProductAdmin)