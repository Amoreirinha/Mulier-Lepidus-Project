from django.db import models
from django.utils.text import slugify
from django.utils.html import format_html
class Categoria(models.Model):
    cat_name = models.CharField('Nome', max_length=100)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.cat_name)
            slug = base_slug
            counter = 1
            while Categoria.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.cat_name
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
class Products(models.Model):
    name = models.CharField('Nome', max_length=100)
    photo = models.ImageField("Imagem do Produto", upload_to='img/products', null=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    descript = models.TextField('Descrição', null=True)
    stock = models.IntegerField('Quantidade em Estoque')
    slug = models.SlugField(unique=True, blank=True,null=True, max_length=255)
    pro_category = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Products.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
class Blog(models.Model):
    blo_title = models.CharField('Título', max_length=100)
    blo_subtitle = models.CharField('Sub-Título', max_length=100, blank=True, null=True)
    blo_description = models.TextField('Texto do Blog')
    # blo_description = HTMLField('Texto do Blog')
    blo_image = models.ImageField('Imagem de Capa', upload_to='img/blog', blank=True, null=True)
    # image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.blo_title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def mini_image(self):
        if self.blo_image:
            return format_html('<img src="{}" style="height: 100px; width: auto;" />', self.blo_image.url)
        return " "
    mini_image.short_description = 'Imagem de Capa'
    def __str__(self):
       return self.blo_title
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
class CategoryTecnology(models.Model):
    cattec_name = models.CharField('Nome da Categoria da Tecnologia', max_length=100, unique=True) # a chave "unique=True" não permitirá cadastrar 2 valores iguais

    def __str__(self):
        return self.cattec_name

    class Meta:
        verbose_name = "Categoria da Tecnologia"
        verbose_name_plural = "Categorias das Tecnologias"


class Tecnology(models.Model):
    tec_name = models.CharField('Nome', max_length=100)
    tec_description = models.TextField('Texto do Tecnologia')
    #tec_description = HTMLField('Texto do Blog')
    tec_image = models.ImageField('Imagem de Capa', upload_to='images/tecnologia', blank=True, null=True)
    # image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    tec_category = models.ForeignKey(CategoryTecnology, on_delete=models.CASCADE, null=True)
        #Abaixo o slug possui a função de adicionar um sufixo caso já exista com o mesmo nome
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.tec_name)
            slug = base_slug
            counter = 1
            while Tecnology.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
        #mini_image para retornar a imagem em miniatura no painel admin
    def mini_image(self):
        if self.tec_image:
            return format_html('<img src="{}" style="height: 100px; width: auto;" />', self.tec_image.url)
        return " "
    mini_image.short_description = 'Imagem de Capa'
    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
       return self.tec_name
    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"