# Generated by Django 4.0.2 on 2022-05-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0004_alter_setuplist_field_name_alter_setuplist_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setuplist',
            name='item_id',
            field=models.CharField(max_length=447),
        ),
    ]