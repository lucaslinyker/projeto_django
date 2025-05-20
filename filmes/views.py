from django.shortcuts import render
from filmes.models import Filme

# Create your views here.
def filme_view(request):
    # filmes = Filme .objects.all()
    search = request.GET.get('search')
    if search:
        filmes = Filme.objects.filter(nome__contains=search)

    return render(request, 'filmes.html', {'filmes': filmes})
