# Generated by Django 5.0.3 on 2024-03-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_project_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typedevelop', models.CharField(max_length=255, verbose_name='Какой разработчик')),
                ('years', models.CharField(max_length=255, verbose_name='В каком году начал и закончил')),
                ('location', models.CharField(max_length=255, verbose_name='Где работал')),
            ],
            options={
                'verbose_name': 'Опыт пользователя',
                'verbose_name_plural': 'Опыт пользователей',
            },
        ),
    ]
