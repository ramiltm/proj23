# Generated by Django 3.2.16 on 2022-10-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
