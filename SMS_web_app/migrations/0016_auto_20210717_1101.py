# Generated by Django 3.2.4 on 2021-07-17 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_web_app', '0015_alter_logisticdetail_dc_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticdetail',
            name='DC_Number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='unitdetail',
            name='Serial_Number',
            field=models.CharField(max_length=123, unique=True),
        ),
    ]