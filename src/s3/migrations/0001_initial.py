# Generated by Django 5.2 on 2025-04-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('content_type', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
    ]
