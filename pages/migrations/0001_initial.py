# Generated by Django 5.2.2 on 2025-06-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='team_photos/')),
                ('facebook_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('google_plus_link', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
