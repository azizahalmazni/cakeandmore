from django.contrib import admin
from .models import تصنيف, منتج

@admin.register(تصنيف)
class تصنيفAdmin(admin.ModelAdmin):
    list_display = ("اسم_التصنيف",)
    search_fields = ("اسم_التصنيف",)


@admin.register(منتج)
class منتجAdmin(admin.ModelAdmin):
    list_display = ("اسم_المنتج", "السعر", "التصنيف", "متوفر", "تاريخ_الإضافة")
    list_filter = ("التصنيف", "متوفر")
    search_fields = ("اسم_المنتج", "الوصف")
    list_editable = ("السعر", "متوفر")
