# Generated by Django 3.2.4 on 2021-07-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_web_app', '0019_alter_logisticdetail_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticdetail',
            name='DC_Date',
            field=models.CharField(max_length=50),
        ),
    ]