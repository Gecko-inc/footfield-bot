# Generated by Django 4.0.5 on 2022-06-26 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0005_alter_hello_options_alter_hello_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footballfield',
            options={'verbose_name': 'Football Field', 'verbose_name_plural': 'Football Fields'},
        ),
        migrations.CreateModel(
            name='ImageForFootballField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('football_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.footballfield')),
            ],
        ),
    ]