# Generated by Django 4.0.7 on 2022-09-12 10:00

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcceptedApplicant',
        ),
        migrations.CreateModel(
            name='DeletedApplicant',
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
        migrations.RemoveField(
            model_name='applicant',
            name='slug',
        ),
    ]
