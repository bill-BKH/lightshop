# Generated by Django 5.0 on 2024-03-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
