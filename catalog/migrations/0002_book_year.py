# Generated by Django 2.2.6 on 2019-10-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
