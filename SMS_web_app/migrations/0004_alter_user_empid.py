# Generated by Django 3.2.4 on 2021-06-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_web_app', '0003_alter_user_empid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='empid',
            field=models.CharField(default='', max_length=10, unique=True, verbose_name='Employee ID'),
        ),
    ]
