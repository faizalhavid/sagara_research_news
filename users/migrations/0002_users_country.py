# Generated by Django 4.2.4 on 2023-08-16 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='country',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.country'),
            preserve_default=False,
        ),
    ]