# Generated by Django 3.2.4 on 2021-06-23 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_alter_productincart_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='updated_at',
        ),
    ]