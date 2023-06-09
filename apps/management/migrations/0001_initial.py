# Generated by Django 4.2 on 2023-04-13 12:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Event title')),
                ('description', models.TextField(verbose_name='Event description/scenario')),
                ('starts_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Starts at')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Last name')),
                ('position', models.CharField(blank=True, max_length=255, verbose_name='Position')),
                ('arrived_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Arrived at')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendances', to='employees.employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Attendance record',
                'verbose_name_plural': 'Attendance records',
            },
        ),
    ]
