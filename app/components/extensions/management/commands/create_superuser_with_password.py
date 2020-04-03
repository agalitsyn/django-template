from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            action='store',
            required=True,
            help='Username for new super user',
        )
        parser.add_argument(
            '--password',
            action='store',
            required=True,
            help='Password',
        )
        parser.add_argument(
            '--email',
            action='store',
            required=True,
            help='Email Address',
        )

    def handle(self, *args, **kwargs):
        user_model = get_user_model()
        try:
            user_model.objects.db_manager().create_superuser(
                username=kwargs['username'],
                password=kwargs['password'],
                email=kwargs['email'],
            )
        # Do not crush on exception, because this command can use several times in CI or test scripts
        except Exception as e:
            self.stdout.write(self.style.WARNING('could not create user: {}'.format(e)))
