from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import NMForm
from .models import NModel

def index(request):
    nmodels = NModel.objects.all()
    return render(request, 'journal/index.html', {
        'nmodels': nmodels,
        'nmform': NMForm()
    })

def profile(request):
    if request.method == "POST":
        form = NMForm(request.POST)
        if form.is_valid():
            nmodel_id = form.cleaned_data['nmodel']
            nmodel = NModel.objects.get(id=nmodel_id)
            nmodel.state.profile = True
            nmodel.state.save()

    return HttpResponseRedirect(reverse('index'))

