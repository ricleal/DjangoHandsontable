# app1/views.py
from django.views.generic import TemplateView,  ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.http import JsonResponse

import json

from .models import Data

class IndexView(TemplateView):
    template_name = "index.html"

class DataListView(ListView):
    model = Data
    fields = '__all__'

def create_data_ajax(request):
    data = request.POST['table_content']
    data = json.loads(data)
    try:
        for row in data:
            if all(x for x in row): # All not None!
                entry = Data.objects.create_entry(row[0],row[1],row[2])
        return HttpResponse("Updated")
    except Exception, e:
        return HttpResponse("Error: %s"%e)
