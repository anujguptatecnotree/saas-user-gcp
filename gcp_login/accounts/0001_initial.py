# Generated by Django 5.0.3 on 2024-03-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=15)),
                ('email', models.TextField(max_length=30)),
                ('contact', models.IntegerField()),
                ('company', models.TextField(max_length=30)),
                ('account_id', models.IntegerField(blank=True)),
                ('precurement_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
