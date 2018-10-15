# Configure the settings for the project
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
django.setup()

# Fake population script
import random
from faker import Faker
from users.models import User

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(
            first_name=fake_first_name,
            last_name=fake_last_name,
            email=fake_email,
        )[0]

# Check if main
if __name__ == '__main__':
    print('>>> populating script...')
    populate(20)
    print('>>> populating complete!')
