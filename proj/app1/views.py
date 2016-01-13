# app1/views.py
from django.views.generic import TemplateView,  ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms import modelformset_factory
from extra_views import FormSetView, ModelFormSetView
from django.core.urlresolvers import reverse_lazy
from pprint import pprint
import collections

import json

from .models import Data

class IndexView(TemplateView):
    template_name = "index.html"

class DataListView(ListView):
    model = Data
    fields = '__all__'

class DataFormView(ModelFormSetView):
    #form_class = modelformset_factory(Data, fields='__all__', extra=5)
    model = Data
    template_name = 'formset.html'
    prefix = "table"
    can_delete = True
    success_url = reverse_lazy('app1:list')

    def post(self, request, *args, **kwargs):
        od = collections.OrderedDict(sorted(dict(self.request.POST).items()))
        pprint(dict(od))
        return super(DataFormView, self).post(request, *args, **kwargs)

    def formset_valid(self, formset):
        print "FORM VALID"
        return super(DataFormView, self).formset_valid(formset)

    def formset_invalid(self, formset):
        print "FORM INNNNNVALID"
        pprint(formset.errors)
        return super(DataFormView, self).formset_invalid(formset)


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
