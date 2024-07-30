from django.contrib import admin
from .models import Products, Blog, Categoria, Tecnology, CategoryTecnology
admin.site.register(Products)
admin.site.register(Categoria)
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ['mini_image', 'blo_title']
    search_fields = ['blo_title']
@admin.register(CategoryTecnology)
class CategoryTecnology(admin.ModelAdmin):
    list_display = ['cattec_name']
    search_fields = ['cattec_name']
@admin.register(Tecnology)
class Tecnology(admin.ModelAdmin):
    list_display = ['tec_name', 'mini_image']
    search_fields = ['tec_name']
