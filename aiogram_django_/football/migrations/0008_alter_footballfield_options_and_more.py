# Generated by Django 4.0.5 on 2022-06-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0007_config_delete_hello_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footballfield',
            options={'verbose_name': 'Футбольное поле', 'verbose_name_plural': 'Футболные поля'},
        ),
        migrations.AlterField(
            model_name='imageforfootballfield',
            name='image',
            field=models.ImageField(upload_to='D:\\dev\\PyCharmProjects\\aiogram_django_/media/'),
        ),
    ]
