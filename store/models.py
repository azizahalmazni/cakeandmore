from django.db import models

class تصنيف(models.Model):
    اسم_التصنيف = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    وصف = models.TextField(blank=True, null=True, verbose_name="الوصف")

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.اسم_التصنيف


class منتج(models.Model):
    التصنيف = models.ForeignKey(تصنيف, on_delete=models.CASCADE, related_name="المنتجات", verbose_name="التصنيف")
    اسم_المنتج = models.CharField(max_length=200, verbose_name="اسم المنتج")
    الوصف = models.TextField(verbose_name="الوصف")
    السعر = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="السعر")
    الصورة = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="صورة المنتج")
    متوفر = models.BooleanField(default=True, verbose_name="متوفر؟")
    تاريخ_الإضافة = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.اسم_المنتج
