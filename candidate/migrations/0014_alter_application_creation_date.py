# Generated by Django 5.1.3 on 2025-01-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0013_alter_application_candidate_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
