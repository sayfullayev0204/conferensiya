from django.shortcuts import render
from django.views.generic import TemplateView, View, GenericViewError, ListView
from articles.models import Article

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

# class ErrorPageView(TemplateView):
#     template_name = 'error.html'

# class ErrorPageView(View, GenericViewError):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'error.html', status=404

