from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("الاسم", "البريد_الإلكتروني", "الموضوع", "تاريخ_الإرسال")
    search_fields = ("الاسم", "البريد_الإلكتروني", "الموضوع")
    list_filter = ("تاريخ_الإرسال",)

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"
