# Generated by Django 5.1.3 on 2024-12-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0006_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.IntegerField(default=1), #Correction : removed Maxlength attribute
        ),
    ]