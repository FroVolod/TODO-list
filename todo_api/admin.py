from django.contrib import admin

from todo_api.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_creation', 'date_due', 'flag_due')


admin.site.register(Task, TaskAdmin)
