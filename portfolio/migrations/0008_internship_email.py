# Generated by Django 4.2.6 on 2023-10-18 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_internshio_internship'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]