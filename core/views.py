from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"مرحباً {username} 🍰")
            return redirect("home")
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة")
    return render(request, "core/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "❌ اسم المستخدم مستخدم مسبقاً")
            return redirect("register")
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "🎉 تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
        return redirect("login")
    return render(request, "core/register.html")

def contact(request):
    return render(request, "core/contact.html")
