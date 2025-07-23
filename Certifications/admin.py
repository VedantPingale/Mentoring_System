from django.contrib import admin
from .models import Certification

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'uploaded_at')
    search_fields = ('title', 'student__username')
    list_filter = ('uploaded_at',)
