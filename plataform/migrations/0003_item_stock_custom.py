# Generated by Django 4.1.5 on 2023-01-31 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0002_alter_brand_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock_custom',
            field=models.FloatField(null=True),
        ),
    ]
