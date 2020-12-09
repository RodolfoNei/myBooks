# Generated by Django 3.0.5 on 2020-12-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20201206_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Already read'), ('w', 'Want to read'), ('r', 'Reading now')], default='w', max_length=1),
        ),
    ]
