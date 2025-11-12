from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import CartItem

# 🛒 إضافة منتج إلى السلة
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # ✅ السلة تعتمد على الجلسة (حتى لو المستخدم غير مسجل)
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    # ✅ البحث أو إنشاء العنصر في السلة
    cart_item, created = CartItem.objects.get_or_create(
        session_key=session_key,
        product=product,
        defaults={'quantity': 1}
    )

    # ✅ إذا كان المنتج مضاف مسبقًا، نزيد الكمية فقط
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')


# 🧺 عرض محتويات السلة
def cart_view(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    # ✅ جلب كل عناصر السلة الخاصة بالجلسة الحالية
    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.total_price() for item in cart_items)

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })
