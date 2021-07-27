# Generated by Django 3.2.4 on 2021-07-17 06:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_web_app', '0022_auto_20210717_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticdetail',
            name='Contact_Number',
            field=models.CharField(default='null', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]