from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name="members.html"),name='member-home' ),
]
