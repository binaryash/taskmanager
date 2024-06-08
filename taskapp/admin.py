from django.contrib import admin
from .models import ScrapingJob

@admin.register(ScrapingJob)
class ScrapingJobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'created_at', 'get_status')
    search_fields = ('job_id',) 

    def get_status(self, obj):
        return 'Completed' if obj.completed else 'Pending'

    get_status.short_description = 'Status'
