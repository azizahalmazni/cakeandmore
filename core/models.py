from django.db import models

class ContactMessage(models.Model):
    الاسم = models.CharField(max_length=100, verbose_name="اسم المرسل")
    البريد_الإلكتروني = models.EmailField(verbose_name="البريد الإلكتروني")
    الموضوع = models.CharField(max_length=200, verbose_name="الموضوع")
    الرسالة = models.TextField(verbose_name="نص الرسالة")
    تاريخ_الإرسال = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"

    def __str__(self):
        return f"{self.الاسم} - {self.الموضوع}"
