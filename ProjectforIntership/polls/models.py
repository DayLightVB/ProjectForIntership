from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User


class Ad(models.Model):

    product_type = models.CharField(max_length=30, verbose_name='Type')
    name = models.CharField(max_length=22, verbose_name='Name')
    model = models.CharField(max_length=25, verbose_name='Model')
    color = models.CharField(max_length=22, verbose_name='Color')
    condition = models.CharField(max_length=22, verbose_name='Condition')
    description = models.TextField(max_length=1523, verbose_name='Description', validators=[MinLengthValidator(100)])
    price = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(9999)], verbose_name='Price')
    date = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=33, verbose_name='Place')
    photo = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return '%s, %s, %s' % (self.model, self.name, self.color)

    def get_absolute_url(self):
        return f'/{self.id}'
