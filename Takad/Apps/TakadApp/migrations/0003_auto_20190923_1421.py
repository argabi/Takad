# Generated by Django 2.2.5 on 2019-09-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TakadApp', '0002_auto_20190918_1909'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.AddField(
            model_name='users',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]