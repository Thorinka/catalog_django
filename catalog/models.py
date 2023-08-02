from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='категория')
    category_description = models.TextField(blank=True, null=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='наименование')
    product_price = models.IntegerField(verbose_name='цена')
    product_description = models.TextField(blank=True, null=True)
    product_image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    version_num = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='активна')

    def __str__(self):
        return f'{self.version_name}: {self.version_num}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
