# Generated by Django 4.0.7 on 2022-09-09 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(blank=True, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('status', models.CharField(choices=[('SEND', 'Send'), ('ACCEPTED', 'Accepted')], default='SEND', max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='AcceptedApplicant',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('applicant.applicant',),
            managers=[
                ('deleted', django.db.models.manager.Manager()),
            ],
        ),
    ]
