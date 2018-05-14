# Generated by Django 2.0.5 on 2018-05-14 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiffRequest',
            fields=[
                ('value', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('occurrences', models.PositiveIntegerField(default=1)),
                ('last_datetime', models.DateTimeField()),
            ],
        ),
    ]
