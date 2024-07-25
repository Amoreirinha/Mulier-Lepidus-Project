from django.contrib import admin
from .models import Products, Blog, Categoria
admin.site.register(Products)
admin.site.register(Categoria)
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    # form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['mini_image', 'blo_title']
    search_fields = ['blo_title']
# Register your models here.
