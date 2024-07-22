# Generated by Django 5.0.6 on 2024-06-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField(max_length=3)),
                ('number', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=25)),
            ],
        ),
    ]
