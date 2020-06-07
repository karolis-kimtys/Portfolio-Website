import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyProject.settings")

import django
django.setup()

#Fake Pop Script
import random
from first_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games", "Users", "Email"]

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()

        #Create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_user = fakegen.name().split()
        fake_fname = fake_user[0]
        fake_lname = fake_user[1]
        fake_email = fakegen.ascii_email()

        #Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        #Create a fake access records
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

        #Create a fake users
        user = User.objects.get_or_create(first_name = fake_fname,
                                            last_name = fake_lname,
                                            email = fake_email)[0]

if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Populating complete!")
