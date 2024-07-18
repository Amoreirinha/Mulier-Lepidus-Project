from django.urls import path

#import das views index e contato criadas no core/views
from core.views import index, contato, sobre, lojinha

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('lojinha', lojinha),
    path('sobre', sobre)
]

# acima o "path('', index)" indica que quando acessar a raiz do site será chamado a view index
# o "path('contato', contato)" indica que quando acessar a rota contato será chamado a view contato