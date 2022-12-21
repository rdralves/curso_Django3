from django.db import models


class Categoria(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categoria.choices,
        default=Categoria.GR,
    )
    approvade = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)
    def __str__(self) -> str:
        return self.title

    def full_name(self):
        return self.title + self.sub_title


    def get_category_label(self):
        return self.get_categories_display()

    full_name.admin_order_field = 'title'
