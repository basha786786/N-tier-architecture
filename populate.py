import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project16.settings')

import django
django.setup()

from app.models import *
import random
from faker import Faker
f=Faker()
topics=['Cricket','Kabaddi','Running','Chess','Hockey','Volleyball','Badminton','Football']

def add_topic():
    topic_name=random.choice(topics)
    t=Topics.objects.get_or_create(topic_name=topic_name)[0]
    t.save()
    return t

def add_webpage(webpagename,url):
    t=add_topic()
    w=Webpage.objects.get_or_create(topic_name=t,name=webpagename,url=url)[0]
    w.save()
    return w

def add_access(webpagename,url,date):
    name=add_webpage(webpagename,url)
    a=Access_Record.objects.get_or_create(name=name,date=date)[0]
    a.save()

def add_data(n):
    for i in range(n):
        fake_name=f.first_name()
        fake_url=f.url()
        fake_date=f.date()
        add_access(fake_name,fake_url,fake_date)

if __name__=='__main__':
    n=int(input('enter n value:'))
    print('population is starting')
    add_data(n)
    print('population is done successfully')

