# Generated by Django 5.0.3 on 2024-03-21 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccounts',
            name='id',
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='account_id',
            field=models.IntegerField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='contact',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='precurement_id',
            field=models.IntegerField(max_length=30, null=True),
        ),
    ]