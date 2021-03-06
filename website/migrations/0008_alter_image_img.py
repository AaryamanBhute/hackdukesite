# Generated by Django 3.2.8 on 2021-10-24 05:44

from django.db import migrations, models
import website.models
import website.storage


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20211023_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.FileField(storage=website.storage.OverwriteStorage(), upload_to=website.models.PathAndRename('images/')),
        ),
    ]
