# Generated by Django 3.0.4 on 2020-04-01 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino')], max_length=1, verbose_name='Sexo')),
            ],
        ),
    ]
