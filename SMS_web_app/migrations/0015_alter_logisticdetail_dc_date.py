# Generated by Django 3.2.4 on 2021-07-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_web_app', '0014_alter_logisticdetail_dc_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticdetail',
            name='DC_Date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]