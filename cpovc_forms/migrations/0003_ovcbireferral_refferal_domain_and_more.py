# Generated by Django 4.0.4 on 2022-05-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0002_ovcbireferral'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovcbireferral',
            name='refferal_domain',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='refferal_service',
            field=models.CharField(max_length=100),
        ),
    ]