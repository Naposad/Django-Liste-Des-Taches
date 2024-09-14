# Generated by Django 5.1.1 on 2024-09-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=400)),
                ('date', models.DateTimeField(auto_now=True)),
                ('date_end', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
