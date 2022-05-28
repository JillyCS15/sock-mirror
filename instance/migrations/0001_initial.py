# Generated by Django 3.2.13 on 2022-05-28 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pattern', '0003_shaclpattern_shacl_pattern'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatternInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('creator', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shacl_shapes', models.TextField(default='')),
                ('shacl_pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pattern.shaclpattern')),
            ],
        ),
    ]
