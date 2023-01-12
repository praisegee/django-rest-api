from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdamin(admin.ModelAdmin):
    list_display = ('title', 'is_complete', 'time')
    search_fields = ('title',)
    list_filter = ('is_complete',)


# admin.site.register(Task, TaskAdamin)
