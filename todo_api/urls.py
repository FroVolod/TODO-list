from django.conf.urls import url

from todo_api.views import TaskView


urlpatterns = [
    url(r'^tasks/(?P<id>[0-9]+)?/?$', TaskView.as_view()),
]
