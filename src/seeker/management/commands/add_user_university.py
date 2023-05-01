from django.core.management.base import BaseCommand

from src.base_user.models import BaseAccount
from src.seeker.models import Seeker, University


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_fake_users()

    def create_university(self):
        for i in range(25):
            university = University.objects.create(
                name=f"YSU{i}",
                location='Yerevan'
            )
            university.save()

    def create_fake_users(self):
        for i in range(1, 26):
            user = Seeker.objects.create(
                full_name=f'Default user_{i}',
                phone_number=f'0938044{i}',
                skills='Somefskills',
                user=BaseAccount.objects.get(id=i + 51),
                languages='some f languages',
                gender='male'
            )

            user.save()

    # def create_base_users(self):
    #     for i in range(25):
    #         user = BaseAccount.objects.create(
    #             email=f'myemail@google{i}.com',
    #         )
    #         user.is_active = True
    #         user.set_password('ad')
    #         user.save()
