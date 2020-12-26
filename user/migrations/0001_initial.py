# Generated by Django 3.1.4 on 2020-12-26 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
