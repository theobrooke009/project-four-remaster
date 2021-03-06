# Generated by Django 3.2.9 on 2021-11-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.CharField(max_length=400)),
                ('price', models.FloatField()),
                ('platform', models.CharField(max_length=50)),
                ('genre', models.CharField(default='Action', max_length=50)),
                ('full_game', models.CharField(max_length=50)),
                ('game_info', models.CharField(max_length=5000)),
                ('size', models.FloatField()),
                ('release_date', models.DateField()),
                ('developer', models.CharField(max_length=50)),
                ('rating', models.CharField(blank=True, max_length=300)),
                ('is_official', models.BooleanField(default=True)),
            ],
        ),
    ]
