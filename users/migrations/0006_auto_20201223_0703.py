# Generated by Django 3.1.4 on 2020-12-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201211_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='Accepted'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='notes1',
            field=models.TextField(blank=True, null=True, verbose_name='The first person notes'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='notes2',
            field=models.TextField(blank=True, null=True, verbose_name='The second person notes'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='rating1',
            field=models.IntegerField(blank=True, null=True, verbose_name='The first person notes'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='rating2',
            field=models.IntegerField(blank=True, null=True, verbose_name='The second person notes'),
        ),
    ]
