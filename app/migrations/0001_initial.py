# Generated by Django 3.1.7 on 2021-04-17 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('topic_name', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('url', models.URLField(max_length=100, unique=True)),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topics')),
            ],
        ),
        migrations.CreateModel(
            name='Access_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, max_length=40)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
    ]
