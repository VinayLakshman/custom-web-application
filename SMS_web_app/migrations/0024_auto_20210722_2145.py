# Generated by Django 3.2.4 on 2021-07-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_web_app', '0023_alter_logisticdetail_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='logisticdetail',
            name='Currency_Format',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='logisticdetail',
            name='Unit_Value',
            field=models.CharField(choices=[('', '-'), ('y', 'Yes'), ('n', 'No')], default='', max_length=128),
        ),
    ]
