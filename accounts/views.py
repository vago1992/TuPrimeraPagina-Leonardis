from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, ProfileEditForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("pages_list")
        return render(request, "accounts/login.html", {"error": "Credenciales inválidas"})
    return render(request, "accounts/login.html")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("pages_list")

@login_required
def profile_view(request):
    return render(request, "accounts/profile.html", {"profile": request.user.profile})

@login_required
def profile_edit(request):
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)

    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    return render(request, "accounts/profile_edit.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })