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

from .models import Data, Reduction, Entry

class IndexView(TemplateView):
    template_name = "index.html"

class DataListView(ListView):
    model = Data
    fields = '__all__'

def create_data_ajax(request):
    '''
    Deals with the ajax request
    '''
    data = request.POST['table_content']
    data = json.loads(data)
    try:
        for row in data:
            if all(x for x in row): # All not None!
                entry = Data.objects.create_entry(row[0],row[1],row[2])
        return HttpResponse("Updated")
    except Exception, e:
        return HttpResponse("Error: %s"%e)

class DataFormView(ModelFormSetView):
    '''
    Deals with the formset request
    '''
    model = Data
    template_name = 'formset.html'
    prefix = "table"
    can_delete = True
    success_url = reverse_lazy('app1:list')

    # The functions below are just for debug!
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

#
# For inline formsets
# Reduction has many Entries
#

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet

class ReductionInline(InlineFormSet):
    model = Entry
    prefix = "table"

class CreateReductionView(CreateWithInlinesView):
    model = Reduction
    inlines = [ReductionInline]
    template_name = 'reduction_formset.html'

    def get_context_data(self, **kwargs):
        ctx = super(CreateReductionView, self).get_context_data(**kwargs)
        pprint(ctx)
        return ctx
    # The functions below are just for debug!
    def post(self, request, *args, **kwargs):
        od = collections.OrderedDict(sorted(dict(self.request.POST).items()))
        pprint(dict(od))
        return super(CreateReductionView, self).post(request, *args, **kwargs)

    def forms_valid(self,  form, inlines):
        print "FORMs VALID"
        return super(CreateReductionView, self).forms_valid(form, inlines)

    def forms_invalid(self,  form, inlines):
        print "FORMs INNNNNVALID"
        pprint(form.errors)
        for formset in inlines:
            pprint(formset.errors)
        return super(CreateReductionView, self).forms_invalid(form, inlines)

class UpdateReductionView(UpdateWithInlinesView):
    model = Reduction
    inlines = [ReductionInline]
    template_name = 'reduction_formset.html'
