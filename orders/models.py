from django.db import models
from store.models import Product


class طلب(models.Model):
    الاسم = models.CharField(max_length=100, verbose_name="اسم العميل")
    البريد_الإلكتروني = models.EmailField(verbose_name="البريد الإلكتروني")
    رقم_الهاتف = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    العنوان = models.TextField(verbose_name="عنوان التوصيل")
    تاريخ_الطلب = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    مكتمل = models.BooleanField(default=False, verbose_name="تم التنفيذ؟")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id} - {self.الاسم}"


class عنصر_طلب(models.Model):
    الطلب = models.ForeignKey(
        طلب,
        on_delete=models.CASCADE,
        related_name="عناصر_الطلب",
        verbose_name="الطلب"
    )
    المنتج = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="المنتج"
    )
    الكمية = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلبات"

    def __str__(self):
        return f"{self.الكمية} × {self.المنتج.name}"
