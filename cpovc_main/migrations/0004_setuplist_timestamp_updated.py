# Generated by Django 4.0.2 on 2022-05-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0003_remove_setuplist_timestamp_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='setuplist',
            name='timestamp_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]