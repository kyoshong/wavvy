# Generated by Django 2.1.5 on 2020-07-18 01:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commu', '0003_auto_20200715_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
