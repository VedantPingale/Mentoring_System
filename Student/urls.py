from django.urls import path
from .views import student_profile, user_list, user_detail

urlpatterns = [
    path("profile/", student_profile, name="student_profile"),
    path("profile/<int:user_id>/", student_profile, name="student_profile_admin"),
    
    path("dashboard/users/", user_list, name="user_list"),
    path("dashboard/users/<int:user_id>/", user_detail, name="user_detail"),
]
