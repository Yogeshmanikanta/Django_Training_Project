from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST['role']

        # ✅ Validation checks
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

        # ✅ Create user safely
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


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # 🔹 Redirect based on role
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'faculty':
                return redirect('faculty_dashboard')
            else:
                messages.error(request, "Invalid role detected.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'users/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
