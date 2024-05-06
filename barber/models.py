from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', args=[self.id])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорий'
        verbose_name_plural = 'Категорий'

class Product(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    image = models.ImageField(upload_to='images/posts/',blank=True,null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id,self.slug])