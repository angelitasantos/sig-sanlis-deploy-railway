# Generated by Django 4.1.5 on 2023-01-31 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_estoqueitens_custo_total_estoqueitens_custo_unitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueitens',
            name='custo_total',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='custo_unitario',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='saldo',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
