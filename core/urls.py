from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from filmes.views import FilmesListView, NovoFilmeCreateView, FilmeDetailView
from filmes.views import FilmesListView, FilmeDeleteView
from usuarios.views import usuario_view, login_view, logout_view

urlpatterns = [
    path('', FilmesListView.as_view(), name='filmes_list'),
    path('users/', usuario_view, name='usuarios'),
    path('admin/', admin.site.urls),
    path('filmes/', FilmesListView.as_view(), name='filmes_list'),
    path('novo_filme/', NovoFilmeCreateView.as_view(), name='novo_filme'),
    path('filme/<int:pk/>', FilmeDetailView.as_view(), name='filme_detail'),
    path('filme/<int:pk>/', FilmeDetailView.as_view(), name='filme_detail'),
    path('filme/delete/<int:pk>/', FilmeDeleteView.as_view(), name='filme_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
] + static(settings.MIDIA_URL, document_root=settings.MIDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
