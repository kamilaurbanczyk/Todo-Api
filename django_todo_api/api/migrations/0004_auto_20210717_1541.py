# Generated by Django 3.2.5 on 2021-07-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210717_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='order',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='url',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
    ]
