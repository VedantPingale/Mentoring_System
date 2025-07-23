from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import Certification
from .forms import CertificationForm

# Student Upload View (accessible to all authenticated users)
@login_required
def upload_certification(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.student = request.user
            certification.save()
            return redirect('user_certification_list')  # Redirect to user's certifications
    else:
        form = CertificationForm()
    return render(request, 'Certifications/upload_certification.html', {'form': form})

# Admin View: List Certifications (restricted to staff members)
@staff_member_required
def admin_certification_list(request):
    certifications = Certification.objects.all()
    return render(request, 'Certifications/admin_certification_list.html', {'certifications': certifications})

# User View: List of their own uploaded certifications
@login_required
def user_certification_list(request):
    certifications = Certification.objects.filter(student=request.user)
    return render(request, 'Certifications/user_certification_list.html', {'certifications': certifications})

# User View: Delete a certification
@login_required
def delete_certification(request, cert_id):
    certification = get_object_or_404(Certification, id=cert_id, student=request.user)
    if request.method == 'POST':
        certification.delete()
        return redirect('user_certification_list')
    return render(request, 'Certifications/confirm_delete.html', {'certification': certification})
