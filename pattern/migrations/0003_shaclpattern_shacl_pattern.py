# Generated by Django 3.2.13 on 2022-05-16 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0002_shaclpattern'),
    ]

    operations = [
        migrations.AddField(
            model_name='shaclpattern',
            name='shacl_pattern',
            field=models.TextField(default=''),
        ),
    ]