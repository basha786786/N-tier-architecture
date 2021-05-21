from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def display_topic(request):
    topics=Topics.objects.all()
    #topics=Topics.objects.filter(topic_name='Cricket')
    #topics=Topics.objects.exclude(topic_name='Hockey')
    #topics=Topics.objects.all()[1:7]
    #topics=Topics.objects.all().order_by('topic_name')
    #topics=Topics.objects.all().order_by('-topic_name')
    #topics=Topics.objects.all().order_by(Length('topic_name'))
    #topics=Topics.objects.all().order_by(Length('topic_name').desc())
    #topics=Topics.objects.filter(topic_name__startswith='c')
    #topics=Topics.objects.filter(topic_name__startswith='t')
    #topics=Topics.objects.filter(topic_name__endswith='g')
    #topics=Topics.objects.filter(topic_name__icontains='a')
    #topics=Topics.objects.filter(Q(topic_name='Cricket'))
    #topics=Topics.objects.filter(Q(topic_name='Hockey'))
    #topics=Topics.objects.filter(topic_name__regex=r'^[a-zA-Z]{1}a')
    #topics=Topics.objects.filter(name__regex=r'^[a-zA-Z]{3}a')
    return render(request,'display_topic.html',context={'topics':topics})

def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='Cricket')
    #webpages=Webpage.objects.exclude(topic_name='Hockey')
    #webpages=Webpage.objects.all()[1:7]
    #webpages=Webpage.objects.all().order_by('topic_name')
    #webpages=Webpage.objects.all().order_by('-name')
    #webpages=Webpage.objects.all().order_by(Length('name'))
    #webpages=Webpage.objects.all().order_by(Length('name').desc())
    #webpages=Webpage.objects.filter(name__startswith='c')
    #webpages=Webpage.objects.filter(url__startswith='https')
    #webpages=Webpage.objects.filter(url__endswith='.com/')
    #webpages=Webpage.objects.filter(name__icontains='a')
    #webpages=Webpage.objects.filter(Q(topic_name='Cricket'))
    #webpages=Webpage.objects.filter(Q(topic_name='Cricket')&Q(name='William'))
    #webpages=Webpage.objects.filter(Q(topic_name='Cricket')|Q(name='William'))
    #webpages=Webpage.objects.filter(Q(topic_name='Cricket')|Q(name='William')|Q(url='https://simmons.com/'))
    #webpages=Webpage.objects.filter(name__regex=r'^[a-zA-Z]{1}a')
    #webpages=Webpage.objects.filter(name__regex=r'^[a-zA-Z]{3}a')
    return render(request,'display_webpage.html',context={'webpages':webpages})

def display_access(request):
    access=Access_Record.objects.all()
    #topics=Topics.objects.filter(topic_name='laura')
    #access=Access_Record.objects.exclude(name='carlous')
    #access=Access_Record.objects.all()[1:7]
    #access=Access_Record.objects.all().order_by('name')
    #access=Access_Record.objects.all().order_by('-name')
    #access=Access_Record.objects.all().order_by(Length('name'))
    #access=Access_Record.objects.all().order_by(Length('name').desc())
    #access=Access_Record.objects.filter(name__startswith='c')
    #access=Access_Record.objects.filter(name__startswith='t')
    #access=Access_Record.objects.filter(name__startswith='K')
    #access=Access_Record.objects.filter(name__endswith='g')
    #access=Access_Record.objects.filter(name__icontains='a')
    #access=Access_Record.objects.filter(Q(name='Karen'))
    #access=Access_Record.objects.filter(Q(name='Samantha'))
    #access=Access_Record.objects.filter(name__regex=r'^[a-zA-Z]{1}a')
    #access=Access_Record.objects.filter(name__regex=r'^[a-zA-Z]{3}a')
    #access=Access_Record.objects.filter(date__gt='1980-10-03')
    #access=Access_Record.objects.filter(date__year='2010')
    #access=Access_Record.objects.filter(date__month='04')
    #access=Access_Record.objects.filter(date__lt='1970-05-03')
    #access=Access_Record.objects.filter(year__gt='2000')
    #access=Access_Record.objects.filter(date__lte='1980-10-03')
    #access=Access_Record.objects.filter(month__gt='08')
    return render(request,'display_access.html',context={'access':access})

def update_topics(request):
    Topics.objects.filter(topic_name='Hockey').update(topic_name='kabaddi')
    Topics.objects.update_or_create(topic_name='kabaddi',defaults={'topic_name':'Cricket'})
    topics=Topics.objects.all()
    d={'topics':topics}
    return render(request,'display_topic.html',context=d)
  


def update_webpage(request):
    t=Topics.objects.get_or_create(topic_name='volleyball')[0]
    #webpage.objects.filter(topic_name='Cricket').update(name='rohit',topic_name='swimming',url='http://rohit.com')
    Webpage.objects.update_or_create(topic_name='volleyball',defaults={'topic_name':t,'name':'bumrah','url':'http://bumrah.com'})
    w=webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',context=d)

def update_access(request):
    w=Webpage.objects.get_or_create(name='Michael')
    #Access_Record.objects.filter(name='Carlous').update(name='sachin')
    Webpage.objects.update_or_create(name='Michael',defaults={'name':w,'date':'1999-04-25'})
    access=Access_Record.objects.all()
    d={'access':access}
    return render(request,'display_access.html',context=d)
  
  

def display_deletetopics(request):
    topics=Topics.objects.all().delete()
    d={'topics':topics}
    return render(request,'display_topic.html',context=d)
def display_delete(request):
    webpage=Webpages.objects.all().delete()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',context=d)

def display_deleteaccess(request):
    access=Access_Record.objects.all().delete()
    d={'access':access}
    return render(request,'display_access.html',context=d)