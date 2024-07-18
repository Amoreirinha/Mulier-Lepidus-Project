from django.db import models

# Create your models here.

class Products (models.Model):
    name = models.CharField('Nome', max_length=100)
    photo= models.ImageField("Imagem do Produto", upload_to='products/', null=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    descript = models.TextField('Descrição', null=True)
    stock = models.IntegerField('Quantidade em Estoque')

    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
        return self.name

    # Outra opção de exibição, está comentado abaixo 

    # def __str__(self):
    #     return f"{self.name} - R$ {self.price:.2f}"

    # blank=True é para tirar a obrigatoriedade do campo
    # null=True é para aceitar preenchimentos nulos no banco