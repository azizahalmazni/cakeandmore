from django.contrib import admin
from .models import التصنيف, المنتج

@admin.register(التصنيف)
class تصنيفAdmin(admin.ModelAdmin):
    list_display = ("اسم_التصنيف",)
    search_fields = ("اسم_التصنيف",)
    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"


@admin.register(المنتج)
class منتجAdmin(admin.ModelAdmin):
    list_display = ("اسم_المنتج", "السعر", "التصنيف", "متوفر", "تاريخ_الإضافة")
    list_filter = ("التصنيف", "متوفر")
    search_fields = ("اسم_المنتج", "الوصف")
    list_editable = ("السعر", "متوفر")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
