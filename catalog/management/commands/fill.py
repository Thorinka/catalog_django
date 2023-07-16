from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category_list = [
            {'category_name': 'Еда'},
            {'category_name': 'Спорт'},
        ]

        for category in category_list:
            new_cat = Category.objects.create(**category)
            new_cat.save()

        product_list = [
            {'product_name': "Пиво", 'product_price': 5, 'category': Category.objects.get(category_name='Еда')},
            {'product_name': "Рыба", 'product_price': 5, 'category': Category.objects.get(category_name='Еда')},
            {'product_name': "Мяч", 'product_price': 7, 'category': Category.objects.get(category_name='Спорт')},
            {'product_name': "Скакалка", 'product_price': 10, 'category': Category.objects.get(category_name='Спорт')},
        ]

        for product in product_list:
            new_prod = Product.objects.create(**product)
            new_prod.save()

