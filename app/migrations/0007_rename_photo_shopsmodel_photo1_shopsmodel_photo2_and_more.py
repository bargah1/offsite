# Generated by Django 5.0.6 on 2024-06-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_shopsmodel_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopsmodel',
            old_name='photo',
            new_name='photo1',
        ),
        migrations.AddField(
            model_name='shopsmodel',
            name='photo2',
            field=models.FileField(default='default_value', upload_to=''),
        ),
        migrations.AddField(
            model_name='shopsmodel',
            name='photo3',
            field=models.FileField(default='default_value', upload_to=''),
        ),
    ]
