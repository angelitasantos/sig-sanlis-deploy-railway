# Generated by Django 4.1.5 on 2023-02-02 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_alter_estoqueitens_custo_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoqueitens',
            name='custo_total_registro',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]