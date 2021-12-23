# Generated by Django 3.0.8 on 2021-12-23 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_id', models.CharField(blank=True, max_length=40, null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'phone_number',
                'managed': False,
            },
        ),
    ]
