# Generated by Django 4.0.2 on 2022-02-09 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samochody', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochody',
            name='model',
            field=models.PositiveSmallIntegerField(choices=[(1, 'premium'), (2, 'standard')], default=1),
            preserve_default=False,
        ),
    ]
