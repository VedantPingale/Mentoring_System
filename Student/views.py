from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Student
from .forms import StudentForm
from Certifications.models import Certification  # Importing Certification model

# Admin check function
def admin_required(user):
    return user.is_staff  # Allows only admin users

# Function to check if a user is an admin or themselves
def is_admin_or_self(user, profile_user):
    return user.is_staff or user == profile_user

# View for displaying the student profile (User can only see their own, Admins can see all)
@login_required
def student_profile(request, user_id=None):
    if user_id:
        student = get_object_or_404(Student, user__id=user_id)
        if not is_admin_or_self(request.user, student.user):
            return redirect('home')  # Redirect unauthorized users
    else:
        student, _ = Student.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.save()
            # Redirect based on whether user is admin or student
            if request.user.is_staff:
                return redirect('user_detail', user_id=student.user.id)
            return redirect('student_profile')
    else:
        form = StudentForm(instance=student)

    return render(request, "student/profile.html", {"form": form, "student": student})

# View for listing all non-admin users, sorted by admission number (Admins Only)
@user_passes_test(admin_required)
def user_list(request):
    students = Student.objects.filter(user__is_staff=False).order_by("Admission_No")
    return render(request, "admin/user_list.html", {"students": students})

# View for displaying a user's profile and their certifications (Admins Only)
@user_passes_test(admin_required)
def user_detail(request, user_id):
    student = get_object_or_404(Student, user__id=user_id)
    certifications = Certification.objects.filter(student=student.user)  # Fetch user's certifications
    return render(request, "admin/user_detail.html", {"student": student, "certifications": certifications})
