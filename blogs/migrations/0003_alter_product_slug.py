# Generated by Django 4.2.7 on 2023-12-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_product_slug_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', verbose_name='عنوان در url'),
        ),
    ]
