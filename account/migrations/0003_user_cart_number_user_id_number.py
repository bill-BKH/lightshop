# Generated by Django 5.0.3 on 2024-04-24 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart_number',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='id_number',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]