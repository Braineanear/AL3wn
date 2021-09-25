# Generated by Django 3.2.3 on 2021-08-08 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reserve', '0005_alter_teacher_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('uuid', models.CharField(max_length=10)),
                ('start_at', models.DateField()),
                ('end_at', models.DateField(blank=True, null=True)),
                ('time', models.TimeField()),
                ('duration', models.DurationField()),
                ('is_private', models.BooleanField(default=False)),
                ('is_online', models.BooleanField(default=False)),
                ('girls_only', models.BooleanField(default=False)),
                ('semster', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=255)),
                ('days', models.ManyToManyField(to='report.Day')),
                ('students', models.ManyToManyField(related_name='student', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='reserve.teacher')),
                ('work_days', models.ManyToManyField(to='report.WorkDay')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='year', to='reserve.year')),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
    ]