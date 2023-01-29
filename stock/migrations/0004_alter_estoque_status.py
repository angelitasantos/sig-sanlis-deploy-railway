# Generated by Django 4.1.5 on 2023-01-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_remove_estoqueitens_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='status',
            field=models.CharField(choices=[('1', 'Não Iniciado'), ('2', 'Em Aberto'), ('3', 'Finalizado')], default='3', max_length=1),
        ),
    ]
