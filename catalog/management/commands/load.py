from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Produce', 'description': 'Fruits and Vegitables'},
            {'category_name': 'Dairy', 'description': 'Milk Products'},
            {'category_name': 'Deli', 'description': 'Prepared Food'},
        ]

        category_create = []

        for category_item in category_list:
            category_create.append(
                Category(**category_item)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(category_create)
