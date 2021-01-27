# Generated by Django 3.1.4 on 2021-01-27 00:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210127_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('writer', models.CharField(choices=[('AMS', 'AMS'), ('AA', 'Ashraf'), ('HA', 'Hala'), ('MM', 'Maryam'), ('MG', 'Gouda')], max_length=255, verbose_name='Writer')),
                ('publisher', models.CharField(choices=[('EE', 'Ehab'), ('GA', 'HerrAli'), ('GM', 'HerrM'), ('AH', 'Halem'), ('GS', 'Shady')], max_length=255, verbose_name='Publisher')),
                ('link', models.URLField(default='http://al3wn.com/', max_length=512)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
