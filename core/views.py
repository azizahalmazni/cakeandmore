from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from store.models import Product


# 🏠 الصفحة الرئيسية (تظهر آخر 4 منتجات)
def home(request):
    latest_products = Product.objects.all()[:4]  # جلب آخر 4 منتجات فقط
    return render(request, 'core/home.html', {'latest_products': latest_products})


# 🔑 تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"مرحباً {username} 🍰")
            return redirect("home")
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة")
            return redirect("login")

    return render(request, "core/login.html")


# 📝 تسجيل مستخدم جديد
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # التحقق من أن اسم المستخدم غير مستخدم مسبقاً
        if User.objects.filter(username=username).exists():
            messages.error(request, "❌ اسم المستخدم مستخدم مسبقاً")
            return redirect("register")

        # إنشاء المستخدم الجديد
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "🎉 تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
        return redirect("login")

    return render(request, "core/register.html")


# 📞 صفحة التواصل معنا
def contact(request):
    return render(request, "core/contact.html")
