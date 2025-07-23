from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Assignment, Submission
from .forms import AssignmentForm, SubmissionForm

def is_staff(user):
    return user.is_authenticated and user.is_staff

@login_required
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})

@login_required
@user_passes_test(is_staff)
def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.mentor = request.user
            assignment.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'assignments/assignment_form.html', {'form': form})

@login_required
@user_passes_test(is_staff)
def assignment_delete(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    assignment.delete()
    return redirect('assignment_list')

@login_required
def assignment_submit(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.student = request.user
            submission.assignment = assignment
            submission.save()
            return redirect('assignment_list')
    else:
        form = SubmissionForm()
    return render(request, 'assignments/assignment_submit.html', {'form': form, 'assignment': assignment})
