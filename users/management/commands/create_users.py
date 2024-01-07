from django.core.management import BaseCommand

from users.models import User

values = ['admin', 'user1', 'user2']
domain = 'test.com'


class Command(BaseCommand):

    def handle(self, *args, **options):
        for value in values:
            if not User.objects.filter(email=value + '@' + domain).exists():
                user = User.objects.create(
                    email=value + '@' + domain,
                    first_name=value.title(),
                    last_name=value.title(),
                    role='admin' if value == 'admin' else 'user',
                    is_active=True,
                )
                user.set_password('111')
                user.save()
            else:
                continue
