# Generated by Django 2.1.7 on 2019-04-17 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_delete_mychl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='product',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='user',
        ),
        migrations.RemoveField(
            model_name='phoneandtabletproduct',
            name='User_ID',
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
        migrations.DeleteModel(
            name='PhoneAndTabletProduct',
        ),
    ]
