# Generated by Django 4.0.1 on 2022-02-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blawx', '0010_workspace_akoma_ntoso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='akoma_ntoso',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='scasp_encoding',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='xml_content',
            field=models.TextField(blank=True, default=''),
        ),
    ]