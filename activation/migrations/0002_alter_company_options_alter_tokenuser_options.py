# Generated by Django 4.1.5 on 2023-01-29 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'empresa', 'verbose_name_plural': 'empresas'},
        ),
        migrations.AlterModelOptions(
            name='tokenuser',
            options={'verbose_name': 'token usuário', 'verbose_name_plural': 'token usuários'},
        ),
    ]
