# Generated by Django 2.1.7 on 2019-04-13 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='artists',
            field=models.ManyToManyField(related_name='artistmovie', to='testapp.artist'),
        ),
        migrations.AlterField(
            model_name='role',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_artist', to='testapp.artist'),
        ),
        migrations.AlterField(
            model_name='role',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_movie', to='testapp.movie'),
        ),
    ]
