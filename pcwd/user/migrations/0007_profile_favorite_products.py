# Generated by Django 5.0.7 on 2024-09-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_baseproduct_id_alter_baseproducttranslation_id_and_more'),
        ('user', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite_products',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='product.scrapedproduct'),
        ),
    ]
