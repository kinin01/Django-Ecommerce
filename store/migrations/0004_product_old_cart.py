# Generated by Django 5.0.1 on 2024-02-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
