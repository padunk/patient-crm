from django.shortcuts import render
from core.models import Patient
from django.contrib.auth.decorators import login_required
from core.forms import SearchForm
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.http import require_GET

# Create your views here.


@login_required
def index(request):
    patients = Patient.objects.all()
    context = {
        'form': SearchForm(),
        'patients': patients,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {})


@require_GET
def search_view(request):
    form = SearchForm(request.GET)
    patients = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        patients = Patient.objects.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(address__icontains=search_query)
        )

        html = render(request, 'partials/search-results.html',
                      {'patients': patients}).content.decode('utf-8')
        return HttpResponse(html)
