from django.urls import path
from .views import assignment_list, assignment_create, assignment_submit, assignment_delete

urlpatterns = [
    path('', assignment_list, name='assignment_list'),
    path('create/', assignment_create, name='assignment_create'),
    path('<int:assignment_id>/submit/', assignment_submit, name='assignment_submit'),
    path('<int:assignment_id>/delete/', assignment_delete, name='assignment_delete'),  # ✅ Added dele
]