# Generated by Django 3.0.4 on 2020-04-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donatario', '0003_grantee_atendido'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantee',
            name='cidade',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='grantee',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Qual seu email?'),
        ),
        migrations.AddField(
            model_name='grantee',
            name='estado',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
