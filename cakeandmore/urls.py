"""
📍 إعداد روابط المشروع الرئيسي - Cake & More 🍰
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🧁 لوحة التحكم
    path('admin/', admin.site.urls),

    # 🏠 التطبيق الأساسي (الصفحات العامة)
    path('', include('core.urls')),

    # 🛒 تطبيق المنتجات
    path('store/', include('store.urls')),

    # 💳 تطبيق الطلبات والدفع
    path('orders/', include('orders.urls')),
]

# 🖼️ دعم عرض الصور أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
