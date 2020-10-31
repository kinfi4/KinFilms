# Generated by Django 3.1.2 on 2020-10-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201029_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='Category',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='film',
            name='Country',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.Country', verbose_name='Country'),
        ),
    ]