# Generated by Django 4.1.5 on 2023-01-29 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_estoque_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueitens',
            name='saldo',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
