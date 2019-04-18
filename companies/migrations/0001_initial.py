# Generated by Django 2.1.1 on 2018-09-19 12:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Multi_Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(choices=[('USER', 'user'), ('VENDOR', 'vendor')], default='USER', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='mychl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='uploads')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='realestatedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('zip', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=1000)),
                ('beds', models.CharField(max_length=1000)),
                ('baths', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='richtext_field_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
