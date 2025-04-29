from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def filme_view(request):
    html = """
    <html>
        <head>
            <title>Filmes</title>
        </head>
        <body>
            <h1>Filmes</h1>
            <ul>
                <li><a href="/filmes/filme1">Filme 1</a></li>
                <li><a href="/filmes/filme2">Filme 2</a></li>
                <li><a href="/filmes/filme3">Filme 3</a></li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html)
