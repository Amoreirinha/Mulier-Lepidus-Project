from django.shortcuts import render
from core.models import Products

context={
    'olas':['Olá!! ༼ つ ◕_◕ ༽つ','Olá?', '༼ つ ◕_◕ ༽つ'],
    'sobre1':'Bem-Vindo à Mulier Lepidus, onde a moda celebra a diversidade e a beleza em todas as suas formas. Nossa loja é dedicada a oferecer peças que inspiram e empoderam mulheres de todas as idades, corpos, cores e estilos. Aqui acreditamos que cada mulher é única e merece se sentir encantadora e confiante em qualquer ocasião. ',
    'sobre2':'Na Mulier Lepidus, combinamos elegância, conforto e tendência para criar uma coleção inclusiva e versátil, pensada para realçar a individualidade de cada cliente. Nossos produtos são cuidadosamente selecionados para garantir a máxima qualidade e estilo, desde looks casuais até roupas para eventos especiais.',
    'sobre3':'Explore nosso catálogo e descubra a peça perfeita para expressar sua personalidade e valorizar sua beleza singular. Na Mulier Lepidus, a moda é mais do que roupas; é uma forma de expressão, um ato de amor-próprio e um convite para abraçar quem você é. Junte-se a nós e sinta-se encantadora todos os dias!',
    'cabecalhos':[
        {'name':'Home',
          'link':'/'
        },
        {'name':'Contato',
          'link':'contato'
        },
        {'name':'Sobre',
          'link':'sobre'
        },
        {'name':'Lojinha',
          'link':'lojinha'
        },
        ],
}
def index(request):
    return render(request, 'index.html', context)

def contato (request):
    return render(request, 'contato.html', context)

def sobre (request):
    return render(request, 'sobre.html', context)

def lojinha (request):
    return render(request, 'lojinha.html', context)

def products (request):
    product = Products.objects.all()

    data = {
        'products': product,
    }
    return render(request, 'produtos.html', data)

# Create your views here.
# São funções para as rotas