# Generated by Django 4.1.5 on 2023-02-08 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_estoqueitens_custo_total_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoqueitens',
            name='custo_unitario_atual',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]