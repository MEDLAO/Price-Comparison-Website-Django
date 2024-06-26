# Generated by Django 3.0 on 2024-06-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20240615_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='baseproducttranslation',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='baseproducttranslation',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
