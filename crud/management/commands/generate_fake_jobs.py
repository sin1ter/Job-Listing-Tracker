import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from crud.models import Job, Recruiter

class Command(BaseCommand):
    help = 'Generate fake job data for all users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        User = get_user_model()
        users = User.objects.all()

        for user in users:
            recruiters = Recruiter.objects.filter(user=user)
            if not recruiters.exists():
                for _ in range(5):  
                    Recruiter.objects.create(
                        user=user,
                        recruiters_name=fake.company(),
                        recruiters_email=fake.email(),
                        slug=fake.slug()
                    )
                recruiters = Recruiter.objects.filter(user=user)

            for _ in range(20):  
                Job.objects.create(
                    user=user,
                    company_name=fake.company(),
                    recruiter=random.choice(recruiters),
                    requirements=fake.text(),
                    job_position=fake.job(),
                    job_link=fake.url(),
                    apply_date=fake.date_this_decade(),
                    status=random.choice([
                        Job.PENDING, Job.REJECTED, Job.REPLIED, Job.GHOSTED, Job.ACCEPTED
                    ]),
                    slug=fake.slug()
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated fake job data for all users'))
