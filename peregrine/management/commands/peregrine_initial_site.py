from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connections, DEFAULT_DB_ALIAS


INITIAL_FIXTURES = [
    'initial_site',
]


class Command(BaseCommand):
    """
    This loads various fixtures of data to populate an initial Peregrine
    site including help on getting started.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '--database',
            action='store',
            dest='database',
            default=DEFAULT_DB_ALIAS,
            help='The database to use. Default to the "default" database.',
        )

    def handle(self, *args, **options):
        self.verbosity = int(options.get('verbosity'))

        # Get the database we're working with
        db = options.get('database')
        connection = connections[db]

        for fixture in INITIAL_FIXTURES:
            print("Installing {}".format(fixture))
            call_command(
                'loaddata',
                fixture,
                verbosity=self.verbosity,
                database=connection.alias,
                skip_validation=True,
                app_label='peregrine',
                hide_empty=True,
            )
