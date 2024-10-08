# Generated by Django 5.1 on 2024-09-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qurultai', '0004_remove_settings_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='email',
            field=models.TextField(default=1, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='phone_number',
            field=models.TextField(default=1, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='title_end',
            field=models.TextField(default=1, verbose_name='Текст в конце'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='description',
            field=models.TextField(verbose_name='Название компании'),
        ),
    ]
