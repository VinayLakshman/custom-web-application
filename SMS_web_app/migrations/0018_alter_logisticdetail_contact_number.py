# Generated by Django 3.2.4 on 2021-07-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_web_app', '0017_alter_logisticdetail_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticdetail',
            name='Contact_Number',
            field=models.IntegerField(default='', max_length=100),
        ),
    ]
