from django.contrib import admin
from .models import رسالة_تواصل

@admin.register(رسالة_تواصل)
class رسالة_تواصلAdmin(admin.ModelAdmin):
    list_display = ("الاسم", "البريد_الإلكتروني", "الموضوع", "تاريخ_الإرسال")
    search_fields = ("الاسم", "البريد_الإلكتروني", "الموضوع")
    list_filter = ("تاريخ_الإرسال",)
