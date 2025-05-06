from django.shortcuts import render

# Create your views here.
def filme_view(request):
    return render(request, 'filmes.html', {'filme': filme})
