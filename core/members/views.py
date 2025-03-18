from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class MemberPage(TemplateView):
    template_name = 'members.html'