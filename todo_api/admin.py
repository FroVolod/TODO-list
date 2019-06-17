from django.contrib import admin

from todo_api.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_creation', 'flag_due', 'order')


admin.site.register(Task, TaskAdmin)
