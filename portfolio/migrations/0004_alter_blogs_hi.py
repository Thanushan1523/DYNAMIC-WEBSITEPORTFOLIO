# Generated by Django 4.2.6 on 2023-10-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_img_blogs_hi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='hi',
            field=models.FileField(blank=True, null=True, upload_to='blog'),
        ),
    ]
