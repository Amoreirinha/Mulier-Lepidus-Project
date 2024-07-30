from django.urls import path
from core.views import index, contato, sobre, lojinha, produto_single, blogs, blog_single,tecs, tec_single, categoria_tec
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('sobre', sobre, name='sobre'),
    path('lojinha', lojinha, name='lojinha'),
    path('produto/<int:id>/', produto_single, name='produto_single'),
    path('blogs', blogs, name='blogs'),
    path('blog/<slug:slug>/', blog_single, name='blog_single'),
    path('tecs', tecs, name= 'tecs'),
    path('tec/<str:cattec_name>/<slug:slug>/', tec_single, name='tecnologia_single'),
    path('tec/<str:cattec_name>/', categoria_tec, name='categoria_tec'),
]