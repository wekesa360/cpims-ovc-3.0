# Generated by Django 4.0.4 on 2022-05-04 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0002_alter_ovcsibling_id_alter_regbiometric_id_and_more'),
        ('cpovc_forms', '0007_alter_ovcbireferral_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovcbireferral',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson'),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='ref_caregiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refferal_caregiver', to='cpovc_registry.regperson'),
        ),
    ]