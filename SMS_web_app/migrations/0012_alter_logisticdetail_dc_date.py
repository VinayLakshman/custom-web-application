# Generated by Django 3.2.4 on 2021-07-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_web_app', '0011_auto_20210717_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticdetail',
            name='DC_Date',
            field=models.DateField(default=''),
        ),
    ]