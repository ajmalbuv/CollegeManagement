# Generated by Django 4.2.14 on 2024-07-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0021_alter_marks_name_alter_marksclass_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigntime',
            name='period',
            field=models.CharField(choices=[('8:30 - 9:45', '8:30 - 9:45'), ('9:45 - 10:45', '9:45 - 10:45'), ('11:10 - 12:10', '11:10 - 12:10'), ('12:10 - 1:10', '12:10 - 1:10'), ('1:50 - 2:40', '1:50 - 2:40'), ('2:40 - 3:30', '2:40 - 3:30')], default='11:10 - 12:10', max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='DOB',
            field=models.DateField(default='2001-01-01'),
        ),
    ]