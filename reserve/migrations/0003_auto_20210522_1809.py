# Generated by Django 3.2.3 on 2021-05-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0002_applicant_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(choices=[('Arabic', 'Arabic'), ('English', 'English'), ('biology', 'biology'), ('Geology', 'Geology'), ('Maths', 'Maths'), ('science', 'science'), ('Deutsch', 'Deutsch'), ('French', 'French'), ('Italian', 'Italian'), ('Statistics', 'Statistics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('philosophy', 'philosophy'), ('psychology', 'psychology'), ('Geography', 'Geography'), ('history', 'history'), ('Chinese', 'Chinese'), ('Spanish', 'Spanish'), ('Studies', 'Studies')], max_length=255),
        ),
    ]