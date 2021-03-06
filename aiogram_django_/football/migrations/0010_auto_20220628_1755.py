# Generated by Django 3.1.6 on 2022-06-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0009_alter_imageforfootballfield_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='config',
            options={'verbose_name': 'Настройка', 'verbose_name_plural': 'Настройки'},
        ),
        migrations.AlterField(
            model_name='config',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='footballfield',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='imageforfootballfield',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
