# Generated by Django 3.1.7 on 2023-05-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20230524_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abc',
            name='img',
            field=models.ImageField(upload_to='fashion'),
        ),
    ]