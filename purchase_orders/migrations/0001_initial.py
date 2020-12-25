# Generated by Django 3.1.4 on 2020-12-25 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('value', models.FloatField()),
                ('status', models.CharField(choices=[('EM_VALIDACAO', 'EM_VALIDACAO'), ('APROVADO', 'APROVADO')], default='EM_VALIDACAO', max_length=15)),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]