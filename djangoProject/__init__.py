# __init__.py of your Django app

from django.db.backends.signals import connection_created
from django.dispatch import receiver


@receiver(connection_created)
def setup_postgres_schema(sender, connection, **kwargs):
    if connection.vendor == 'postgresql':
        cursor = connection.cursor()
        cursor.execute("SET search_path TO vln2_assignment_groups_49;")
