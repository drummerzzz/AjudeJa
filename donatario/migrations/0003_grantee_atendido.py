# Generated by Django 3.0.4 on 2020-04-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donatario', '0002_auto_20200401_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantee',
            name='atendido',
            field=models.BooleanField(default=False),
        ),
    ]
