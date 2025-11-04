from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


# 🏠 Home / Landing Page
def home(request):
    return render(request, 'home.html')


# 📝 Register User
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')

        # ✅ Validation checks
        if not username or not email or not password1 or not password2 or not role:
            messages.error(request, "All fields are required.")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if role not in ['student', 'faculty']:
            messages.error(request, "Invalid role selection.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        # ✅ Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            role=role
        )
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'users/register.html')


# 🔐 Login User
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # 🔹 Redirect based on role
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'faculty':
                return redirect('faculty_dashboard')
            else:
                logout(request)
                messages.error(request, "Invalid role detected.")
                return redirect('login')

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'users/login.html')


# 🚪 Logout User
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')
