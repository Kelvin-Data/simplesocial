# Generated by Django 3.2.7 on 2021-09-12 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='desciption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='desciption_html',
            new_name='description_html',
        ),
    ]
