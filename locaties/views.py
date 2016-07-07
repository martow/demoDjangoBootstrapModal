from django.core.urlresolvers import reverse

from locaties.models import Location
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy



# Create your views here.
def index(request):
    locations = Location.objects.all()
    template = loader.get_template('overview.html')
    context = RequestContext(request, {
        'locations': locations,
    })
    return HttpResponse(template.render(context))


class LocationCreateView(CreateView):
    model = Location
    fields = ['name', 'type']

    success_url = '/locaties'


class DetailLocation(DetailView):
    model = Location


class UpdateLocation(UpdateView):
    model = Location
    queryset = Location.objects.all()
    fields = ['name', 'type', 'notes']


class DeleteLocation(DeleteView):
    model = Location
    success_url = reverse_lazy('locations')

