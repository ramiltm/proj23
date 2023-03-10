# Generated by Django 3.2.16 on 2022-11-21 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0005_alter_property_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='IT_Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('issues', models.CharField(max_length=100)),
                ('service_rendered', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=150)),
                ('action_officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='servOff', to='mr.it_officer')),
                ('prop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='propservice', to='mr.property')),
            ],
        ),
    ]
