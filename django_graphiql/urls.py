from django.conf.urls import url

from .views import GraphiQL

urlpatterns = [
    url(r'^', GraphiQL.as_view()),
]
