# certifications/urls.py
from django.urls import path
from .views import upload_certification, admin_certification_list, user_certification_list, delete_certification

urlpatterns = [
    path('upload/', upload_certification, name='upload_certification'),
    path('admin-list/', admin_certification_list, name='admin_certification_list'),
    path('my-certifications/', user_certification_list, name='user_certification_list'),
    path('delete/<int:cert_id>/', delete_certification, name='delete_certification'),  # Ensure cert_id matches the view argument
]
