# Generated by Django 5.0.6 on 2024-07-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_shopsmodel_photo1_alter_shopsmodel_photo2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopsmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shopsmodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shopsmodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='shopsmodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='shopsmodel',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='shopsmodel',
            name='photo1',
            field=models.ImageField(default='shop_photos/default_image.jpg', upload_to='shop_photos/'),
        ),
        migrations.AlterField(
            model_name='shopsmodel',
            name='photo2',
            field=models.ImageField(default='shop_photos/default_image.jpg', upload_to='shop_photos/'),
        ),
        migrations.AlterField(
            model_name='shopsmodel',
            name='photo3',
            field=models.ImageField(default='shop_photos/default_image.jpg', upload_to='shop_photos/'),
        ),
    ]
