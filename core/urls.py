from django.urls import path
#import das views index e contato criadas no core/views
from core.views import index, contato, sobre, lojinha, produto_single, blogs, blog_single

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('sobre', sobre, name='sobre'),
    path('lojinha', lojinha, name='lojinha'),
    path('produto/<int:id>/', produto_single, name='produto_single'),
    path('blogs', blogs, name='blogs'),
    path('blog/<slug:slug>/', blog_single, name='blog_single'),
]

# acima o "path('', index)" indica que quando acessar a raiz do site será chamado a view index
# o "path('contato', contato)" indica que quando acessar a rota contato será chamado a view contato