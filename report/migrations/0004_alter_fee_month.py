# Generated by Django 3.2.3 on 2021-09-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_alter_fee_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='month',
            field=models.IntegerField(),
        ),
    ]
