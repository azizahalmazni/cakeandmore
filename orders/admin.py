from django.contrib import admin
from .models import الطلب, عنصر_الطلب

class عنصر_الطلبInline(admin.TabularInline):
    model = عنصر_الطلب
    extra = 1

@admin.register(الطلب)
class طلبAdmin(admin.ModelAdmin):
    list_display = ("id", "الاسم", "البريد_الإلكتروني", "رقم_الهاتف", "تاريخ_الطلب", "مكتمل")
    list_filter = ("مكتمل", "تاريخ_الطلب")
    search_fields = ("الاسم", "البريد_الإلكتروني", "رقم_الهاتف")
    list_editable = ("مكتمل",)
    inlines = [عنصر_الطلبInline]

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"


@admin.register(عنصر_الطلب)
class عنصر_طلبAdmin(admin.ModelAdmin):
    list_display = ("الطلب", "المنتج", "الكمية")
    list_filter = ("الطلب",)
    search_fields = ("المنتج__اسم_المنتج",)

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلبات"
