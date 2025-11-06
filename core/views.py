from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# 🏠 الصفحة الرئيسية
def home(request):
    return render(request, 'home.html')


# 🔐 تسجيل الدخول
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

    # تأكد أن القالب موجود في هذا المسار:
    # C:\Users\maks\cakeandmore\templates\core\login.html
    return render(request, "core/login.html")


# 🧁 إنشاء حساب جديد
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "❌ اسم المستخدم مستخدم مسبقاً")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "🎉 تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
        return redirect("login")

    # تأكد أن القالب موجود في هذا المسار:
    # C:\Users\maks\cakeandmore\templates\core\register.html
    return render(request, "core/register.html")


# ✉️ صفحة التواصل
def contact(request):
    # تأكد أن القالب موجود في هذا المسار:
    # C:\Users\maks\cakeandmore\templates\core\contact.html
    return render(request, "core/contact.html")
