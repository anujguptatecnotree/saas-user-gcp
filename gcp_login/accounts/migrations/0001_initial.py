# Generated by Django 5.0.3 on 2024-03-25 14:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userAccounts',
            fields=[
                ('username', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('company', models.TextField(max_length=30)),
                ('account_id', models.CharField(max_length=30, null=True)),
                ('precurement_id', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
