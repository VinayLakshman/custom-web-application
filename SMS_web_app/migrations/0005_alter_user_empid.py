# Generated by Django 3.2.4 on 2021-06-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_web_app', '0004_alter_user_empid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='empid',
            field=models.CharField(default='', max_length=10, verbose_name='Employee ID'),
        ),
    ]
