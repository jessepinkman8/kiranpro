# Generated by Django 3.1.7 on 2023-05-24 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_personal_product_wedding'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='personal',
            new_name='abc1',
        ),
        migrations.RenameModel(
            old_name='product',
            new_name='abc2',
        ),
        migrations.RenameModel(
            old_name='wedding',
            new_name='abc3',
        ),
    ]