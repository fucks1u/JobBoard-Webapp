# Generated by Django 4.2.6 on 2023-10-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Companies', '0003_alter_companies_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='description',
            field=models.CharField(max_length=65535),
        ),
    ]