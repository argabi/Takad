# Generated by Django 2.2.5 on 2019-09-27 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TakadApp', '0024_auto_20190926_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports_result',
            name='is_file',
        ),
        migrations.AddField(
            model_name='reports_result',
            name='sacnName',
            field=models.TextField(default='theNamehahah'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messages',
            name='isRead',
            field=models.BooleanField(default=True),
        ),
    ]
