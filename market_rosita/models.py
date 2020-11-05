from django.db import models

# Create your models here.
class Brand(models.Model):
    id = models.AutoField('Código', primary_key=True)
    description = models.CharField('Descripción', max_length=20)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class Category(models.Model):
    id = models.AutoField('Código', primary_key=True)
    description = models.CharField('Descripción', max_length=20)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField('Descripción', max_length=100, blank=False, null=False)
    stock = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    unit_measure_purchase = models.CharField('UM Compras', max_length=3, blank=True, null=False)
    unit_measure_sales = models.CharField('UM Ventas', max_length=3, blank=True, null=False)
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Marca')
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'