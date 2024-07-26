from django.shortcuts import render, get_object_or_404
from core.models import Products, Blog

def get_common_context():
    return {
        'olas': ['Olá!! ༼ つ ◕_◕ ༽つ', 'Olá?', '༼ つ ◕_◕ ༽つ'],
        'sobre1': 'Bem-Vindo à Mulier Lepidus, onde a moda celebra a diversidade e a beleza em todas as suas formas. Nossa loja é dedicada a oferecer peças que inspiram e empoderam mulheres de todas as idades, corpos, cores e estilos. Aqui acreditamos que cada mulher é única e merece se sentir encantadora e confiante em qualquer ocasião.',
        'sobre2': 'Na Mulier Lepidus, combinamos elegância, conforto e tendência para criar uma coleção inclusiva e versátil, pensada para realçar a individualidade de cada cliente. Nossos produtos são cuidadosamente selecionados para garantir a máxima qualidade e estilo, desde looks casuais até roupas para eventos especiais.',
        'sobre3': 'Explore nosso catálogo e descubra a peça perfeita para expressar sua personalidade e valorizar sua beleza singular. Na Mulier Lepidus, a moda é mais do que roupas; é uma forma de expressão, um ato de amor-próprio e um convite para abraçar quem você é. Junte-se a nós e sinta-se encantadora todos os dias!',
        'cabecalhos': [
            {'name': 'Home', 'link': 'index'},
            {'name': 'Contato', 'link': 'contato'},
            {'name': 'Sobre', 'link': 'sobre'},
            {'name': 'Lojinha', 'link': 'lojinha'}
        ]
    }

def index(request):
    context = get_common_context()
    context['title'] = 'Mulier Lepidus'
    return render(request, 'index.html', context)

def contato(request):
    context = get_common_context()
    context['title'] = 'Contato Mulier Lepidus'
    return render(request, 'contato.html', context)

def sobre(request):
    context = get_common_context()
    context['title'] = 'Sobre Nós'
    return render(request, 'sobre.html', context)

def lojinha(request):
    products = Products.objects.all()
    context = get_common_context()
    context['products'] = products
    context['title'] = 'Lojinha'
    return render(request, 'lojinha.html', context)

def produto_single(request, id):
    product = get_object_or_404(Products, id=id)
    context = get_common_context()
    context['product'] = product
    context['title'] = 'Brusinha'
    return render(request, 'produto_single.html', context)

def blogs(request):
    blogs = Blog.objects.all()
    context = get_common_context()
    context['blogs'] = blogs
    context['title'] = 'Blogs'
    return render(request, 'blogs.html', context)

def blog_single(request, slug):
    blogs = get_object_or_404(Blog, slug=slug)
    context = get_common_context()
    context['blogs'] = blogs
    context['title'] = 'Blog'
    return render(request, 'blog_single.html', context)
